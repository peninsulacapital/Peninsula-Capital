from enum import Enum
from typing import Annotated, Generic, Literal, TypeVar

from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing_extensions import TypeAliasType

T = TypeVar("T")

CURRENCY_PATTERN = r"^[A-Z]{3}$"


class SchemaModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Status(str, Enum):
    """Situação do dado no texto do cliente.
    stated: dito de forma explícita.
    approximate: dito de forma aproximada ('uns 5 milhões', 'entre 3 e 5', 'jovem').
    ambiguous: dito, mas o texto admite mais de uma leitura.
    absent: o cliente não disse."""

    STATED = "stated"
    APPROXIMATE = "approximate"
    AMBIGUOUS = "ambiguous"
    ABSENT = "absent"


class Declared(SchemaModel, Generic[T]):
    """Um dado como o cliente o declarou. Nunca preencher por inferência: o que não foi dito fica 'absent'."""

    status: Status = Status.ABSENT
    value: T | None = Field(
        None,
        description=(
            "O dado transcrito do texto. Pode mudar a notação (R$ 300MM → 300000000; 'R$ 50 mil' → 50000), "
            "mas nunca fazer conta: combinar dois números do texto é trabalho do Python."
        ),
    )
    excerpt: str | None = Field(
        None,
        description=(
            "Trecho literal do texto do cliente de onde o dado saiu, copiado sem alterar nenhuma palavra. "
            "Só as palavras que sustentam este campo: cada campo tem o seu trecho. Em 'R$ 10MM/ANO EM TERMOS REAIS', "
            "o valor usa 'R$ 10MM', a periodicidade '/ANO' e a base 'EM TERMOS REAIS'. "
            "Obrigatório sempre que o status não for 'absent'."
        ),
    )
    note: str | None = Field(
        None,
        description=(
            "Para 'approximate': a forma aproximada, quando não cabe em 'value' (ex.: uma faixa). "
            "Para 'ambiguous': as leituras possíveis."
        ),
    )

    @model_validator(mode="after")
    def _check_status(self):
        if self.status is Status.ABSENT:
            if self.value is not None or self.excerpt is not None:
                raise ValueError("dado ausente não tem valor nem trecho")
        elif not self.excerpt:
            raise ValueError(f"dado com status '{self.status.value}' exige o trecho de origem")
        elif self.status is Status.STATED and self.value is None:
            raise ValueError("dado informado exige valor")
        return self


class Money(SchemaModel):
    """Quantia em dinheiro."""

    kind: Literal["money"] = "money"
    amount: float = Field(description="Em unidades da moeda (R$ 300MM → 300000000).")
    currency: str | None = Field(
        None,
        pattern=CURRENCY_PATTERN,
        description=(
            "Código ISO 4217 da moeda em que o valor foi dito (BRL, USD). A moeda vem de 'R$', 'reais', 'US$', "
            "'dólares' — nunca de 'em termos reais', que fala de inflação, não de moeda. Nulo se o texto não disser."
        ),
    )


class Share(SchemaModel):
    """Quantia dita como percentual de outra coisa ('4% do que recebeu'). Converter em dinheiro é trabalho do Python."""

    kind: Literal["share"] = "share"
    percent: float = Field(description="Em pontos percentuais: 4% → 4.")
    of_description: str = Field(description="A base do percentual, como o cliente a descreveu.")
    of_ref: str | None = Field(None, description="Id do item do perfil que é a base do percentual, quando houver.")


Quantity = TypeAliasType("Quantity", Annotated[Money | Share, Field(discriminator="kind")])


class CurrencyShare(SchemaModel):
    currency: str = Field(pattern=CURRENCY_PATTERN, description="Código ISO 4217.")
    percent: float = Field(description="Em pontos percentuais: 80% → 80.")
