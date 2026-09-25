from enum import Enum

from pydantic import Field, model_validator

from agente.schemas.base import CurrencyShare, Declared, Money, Quantity, SchemaModel, Share


class Firmness(str, Enum):
    """Quão decidida é uma vontade do cliente.
    firm: vontade declarada ('quer', 'vai', 'decidiu', 'deseja'). O quê não está em discussão; o analista decide só a forma.
    open: possibilidade ou preferência ('poderia', 'pensa em', 'talvez', 'prefere'). O analista pode recomendar a favor ou contra.
    Ausente (cliente não se posicionou): a decisão é nossa, do analista — não é lacuna a perguntar ao cliente."""

    FIRM = "firm"
    OPEN = "open"


class FamilyRole(str, Enum):
    """Papel na família, em relação à pessoa principal (a pessoa central do atendimento)."""

    PRINCIPAL = "principal"
    SPOUSE = "spouse"
    CHILD = "child"
    PARENT = "parent"
    SIBLING = "sibling"
    OTHER = "other"


class Jurisdiction(str, Enum):
    BRAZIL = "brazil"
    ABROAD = "abroad"


class HoldingStructure(str, Enum):
    """Como o bem é detido. direct: em nome da pessoa física."""

    DIRECT = "direct"
    HOLDING_COMPANY = "holding_company"
    OFFSHORE_VEHICLE = "offshore_vehicle"
    OTHER = "other"


class AssetCategory(str, Enum):
    """Natureza econômica do ativo. A categoria só agrupa; o que importa são os atributos.
    financial_investment: aplicações financeiras e dinheiro em conta.
    real_estate: imóvel urbano ou rural, inclusive terra produtiva.
    business_stake: participação em empresa ou negócio.
    pension_plan: previdência privada (PGBL, VGBL, fundo de pensão).
    personal_property: bens de uso pessoal (veículos, arte, joias)."""

    FINANCIAL_INVESTMENT = "financial_investment"
    REAL_ESTATE = "real_estate"
    BUSINESS_STAKE = "business_stake"
    PENSION_PLAN = "pension_plan"
    PERSONAL_PROPERTY = "personal_property"
    OTHER = "other"


class FinancialSubtype(str, Enum):
    CASH = "cash"
    FIXED_INCOME = "fixed_income"
    EQUITY = "equity"
    FUND = "fund"
    OTHER = "other"


class AssetUse(str, Enum):
    """Para que o ativo serve hoje.
    own_residence: moradia da família.
    personal_use: uso próprio que não é moradia (casa de veraneio, carro).
    productive: gera renda operando (fazenda em atividade, empresa).
    investment: mantido para valorizar ou gerar renda passiva (imóvel alugado, aplicações)."""

    OWN_RESIDENCE = "own_residence"
    PERSONAL_USE = "personal_use"
    PRODUCTIVE = "productive"
    INVESTMENT = "investment"


class LiabilityCategory(str, Enum):
    """Natureza econômica do passivo.
    productive_credit: crédito para atividade produtiva (rural, capital de giro).
    tax_obligation: imposto devido ou parcelado.
    guarantee_given: aval ou fiança dados a terceiros — não é dívida hoje, mas pode virar."""

    REAL_ESTATE_FINANCING = "real_estate_financing"
    PRODUCTIVE_CREDIT = "productive_credit"
    PERSONAL_LOAN = "personal_loan"
    TAX_OBLIGATION = "tax_obligation"
    GUARANTEE_GIVEN = "guarantee_given"
    OTHER = "other"


class Indexer(str, Enum):
    """fixed: prefixada. fx: variação cambial."""

    FIXED = "fixed"
    CDI = "cdi"
    IPCA = "ipca"
    FX = "fx"
    OTHER = "other"


class FlowDirection(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class FlowCategory(str, Enum):
    """labor_income: salário, pró-labore, honorários.
    asset_income: renda gerada por um ativo (aluguel, dividendos, resultado da fazenda, juros).
    benefit: aposentadoria, pensão, benefício.
    transfer: transferência entre pessoas (mesada, ajuda a parentes).
    living_expense: gasto de vida.
    asset_cost: custo de manter um ativo.
    debt_payment: parcela de dívida."""

    LABOR_INCOME = "labor_income"
    ASSET_INCOME = "asset_income"
    BENEFIT = "benefit"
    TRANSFER = "transfer"
    LIVING_EXPENSE = "living_expense"
    ASSET_COST = "asset_cost"
    DEBT_PAYMENT = "debt_payment"
    OTHER = "other"


class Periodicity(str, Enum):
    MONTHLY = "monthly"
    ANNUAL = "annual"
    OTHER = "other"


class ValueBasis(str, Enum):
    """real: em termos reais, isto é, descontada a inflação (poder de compra de hoje). Não tem relação com a moeda real (R$).
    nominal: sem desconto da inflação."""

    REAL = "real"
    NOMINAL = "nominal"


class GrossNet(str, Enum):
    GROSS = "gross"
    NET = "net"


class EventKind(str, Enum):
    """relocation: mudança de domicílio ou de residência fiscal."""

    ASSET_SALE = "asset_sale"
    ASSET_PURCHASE = "asset_purchase"
    DONATION = "donation"
    INHERITANCE = "inheritance"
    RETIREMENT = "retirement"
    RELOCATION = "relocation"
    OTHER_INFLOW = "other_inflow"
    OTHER_OUTFLOW = "other_outflow"
    OTHER = "other"


class RiskStatementKind(str, Enum):
    """loss_tolerance: quanto aceita perder.
    experience: com o que já investiu, ou nunca investiu.
    reaction_to_loss: como reagiu a perdas passadas.
    attitude: postura geral diante de risco ('ficou mais conservador').
    comparative: risco que aceita em relação a outra pessoa."""

    LOSS_TOLERANCE = "loss_tolerance"
    EXPERIENCE = "experience"
    REACTION_TO_LOSS = "reaction_to_loss"
    ATTITUDE = "attitude"
    COMPARATIVE = "comparative"


class AggregateKind(str, Enum):
    """composition: fatia do todo ('75% imobilizado em terra', '100% no Brasil')."""

    TOTAL_WEALTH = "total_wealth"
    TOTAL_INCOME = "total_income"
    TOTAL_SPENDING = "total_spending"
    COMPOSITION = "composition"
    OTHER = "other"


class ProfileSection(str, Enum):
    PEOPLE = "people"
    ASSETS = "assets"
    LIABILITIES = "liabilities"
    FLOWS = "flows"
    EVENTS = "events"
    GOALS = "goals"
    OTHER = "other"


class Rate(SchemaModel):
    indexer: Indexer
    value: float = Field(
        description=(
            "Em pontos percentuais ao ano. Prefixada: a própria taxa (12% → 12). "
            "Indexada: o spread sobre o indexador (IPCA + 5% → 5), ou o percentual do indexador "
            "quando 'percent_of_indexer' for verdadeiro (120% do CDI → 120)."
        )
    )
    percent_of_indexer: bool = False


class Holding(SchemaModel):
    person_id: str
    percent: float | None = Field(None, description="Participação em pontos percentuais. Nulo se não dita.")


class Item(SchemaModel):
    id: str = Field(
        description=(
            "Identificador único no perfil, estável entre as rodadas do loop de esclarecimento: "
            "a resposta do cliente atualiza o item pelo id."
        )
    )
    description: str = Field(description="Resumo curto do item, fiel ao que o cliente disse.")
    excerpt: str = Field(description="Trecho literal do texto em que o item aparece.")


class Person(Item):
    role: FamilyRole
    age: Declared[int] = Field(default_factory=Declared[int])
    occupation: Declared[str] = Field(default_factory=Declared[str])
    tax_residence: Declared[str] = Field(default_factory=Declared[str], description="País de residência fiscal atual.")


class Asset(Item):
    """Um bem do cliente. Renda e custos do ativo vão em 'flows' (com asset_id); venda ou compra vão em 'events'."""

    category: AssetCategory
    financial_subtype: Declared[FinancialSubtype] = Field(
        default_factory=Declared[FinancialSubtype], description="Só para 'financial_investment'."
    )
    current_value: Declared[Money] = Field(
        default_factory=Declared[Money], description="Valor atual (avaliação, saldo, valor de mercado)."
    )
    acquisition_cost: Declared[Money] = Field(
        default_factory=Declared[Money], description="Quanto custou; base do imposto sobre ganho de capital."
    )
    use: Declared[AssetUse] = Field(default_factory=Declared[AssetUse])
    holders: Declared[list[Holding]] = Field(default_factory=Declared[list[Holding]], description="Donos.")
    structure: Declared[HoldingStructure] = Field(default_factory=Declared[HoldingStructure])
    jurisdiction: Declared[Jurisdiction] = Field(default_factory=Declared[Jurisdiction])


class Liability(Item):
    """Uma dívida ou obrigação do cliente. Parcelas vão em 'flows' (debt_payment, com liability_id)."""

    category: LiabilityCategory
    balance: Declared[Money] = Field(default_factory=Declared[Money], description="Saldo devedor.")
    rate: Declared[Rate] = Field(default_factory=Declared[Rate])
    term_end: Declared[str] = Field(default_factory=Declared[str], description="Quando termina, como dito.")
    collateral_asset_id: Declared[str] = Field(
        default_factory=Declared[str], description="Id do ativo dado em garantia."
    )
    prepayable: Declared[bool] = Field(
        default_factory=Declared[bool],
        description="Se pode ser quitada antes do prazo. Multa, se dita, vai em 'note'.",
    )
    holders: Declared[list[Holding]] = Field(default_factory=Declared[list[Holding]], description="Devedores.")
    jurisdiction: Declared[Jurisdiction] = Field(default_factory=Declared[Jurisdiction])


class Flow(Item):
    """Entrada ou saída recorrente de dinheiro. Movimentos pontuais vão em 'events'."""

    direction: FlowDirection
    category: FlowCategory
    amount: Declared[Quantity] = Field(default_factory=Declared[Quantity])
    periodicity: Declared[Periodicity] = Field(default_factory=Declared[Periodicity])
    basis: Declared[ValueBasis] = Field(default_factory=Declared[ValueBasis])
    gross_net: Declared[GrossNet] = Field(default_factory=Declared[GrossNet])
    currency_mix: Declared[list[CurrencyShare]] = Field(
        default_factory=Declared[list[CurrencyShare]],
        description=(
            "Em que moedas o dinheiro é gasto ou recebido ('cesta de gastos 80% em reais e 20% em dólares'). "
            "Diferente da moeda em que o valor foi dito."
        ),
    )
    people: Declared[list[str]] = Field(
        default_factory=Declared[list[str]],
        description="Ids das pessoas que recebem (receita) ou arcam com (despesa) o fluxo.",
    )
    end: Declared[str] = Field(default_factory=Declared[str], description="Até quando dura (data, idade, evento), como dito.")
    asset_id: str | None = Field(None, description="Ativo que gera o fluxo ou cujo custo ele é.")
    liability_id: str | None = Field(None, description="Passivo cuja parcela ele é.")


class Event(Item):
    """Movimento pontual de dinheiro ou mudança de vida: venda, doação, herança, aposentadoria, mudança de domicílio."""

    kind: EventKind
    firmness: Declared[Firmness] = Field(default_factory=Declared[Firmness])
    when: Declared[str] = Field(default_factory=Declared[str], description="Data ou prazo, como dito.")
    amount: Declared[Quantity] = Field(default_factory=Declared[Quantity])
    asset_id: str | None = Field(None, description="Ativo vendido ou comprado.")
    actors: Declared[list[str]] = Field(
        default_factory=Declared[list[str]],
        description="Ids de quem realiza (quem vende, doa, se aposenta, se muda).",
    )
    beneficiaries: Declared[list[str]] = Field(
        default_factory=Declared[list[str]], description="Ids de quem recebe, em doações e heranças."
    )


class Goal(Item):
    """Resultado que o cliente quer alcançar (organizar a sucessão, um filho aprender a lidar com patrimônio, viver de renda). Movimentos concretos vão em 'events'."""

    people: Declared[list[str]] = Field(default_factory=Declared[list[str]], description="Ids de quem o objetivo é.")
    horizon: Declared[str] = Field(default_factory=Declared[str], description="Prazo, como dito.")
    amount: Declared[Quantity] = Field(default_factory=Declared[Quantity])


class Belief(Item):
    """Afirmação do cliente sobre como as coisas funcionam ou vão funcionar, que pode ser verificada ('a renda disso cobre os gastos dela'). Não é fato: o analista confirma ou refuta."""

    holders: list[str] = Field(description="Ids de quem afirma.")


class Preference(Item):
    """Restrição ou preferência sobre o plano ('não quero dólar', 'não pretendemos deixar o Brasil'). firm = restrição; open = preferência."""

    people: list[str] = Field(description="Ids de quem expressa.")
    firmness: Firmness


class RiskStatement(Item):
    """O que o cliente disse sobre sua relação com risco, registrado como dito. Classificar o perfil de risco é da validação."""

    person_id: str
    kind: RiskStatementKind
    relative_to: str | None = Field(None, description="Para 'comparative': id da pessoa com quem se compara.")
    max_loss_percent: float | None = Field(
        None, description="Para 'loss_tolerance': o limite de perda, se dito, em pontos percentuais."
    )


class AggregateStatement(Item):
    """Número global dito pelo cliente (patrimônio total, gasto total, '75% imobilizado'). Não se soma aos itens: serve para a validação conferir."""

    kind: AggregateKind
    quantity: Quantity
    periodicity: Periodicity | None = None


class NegativeStatement(Item):
    """O cliente disse que algo NÃO existe ('não temos dívidas', 'nenhum dos dois tem renda de trabalho'). Diferente de ausência: aqui não há o que perguntar."""

    section: ProfileSection
    people: list[str] = Field(default_factory=list, description="Ids de a quem a negativa se refere.")


class ClientProfile(SchemaModel):
    """Tudo o que o cliente disse sobre si, traduzido sem julgamento. Coerência e completude são checadas depois, pela validação."""

    people: list[Person] = Field(default_factory=list)
    assets: list[Asset] = Field(default_factory=list)
    liabilities: list[Liability] = Field(default_factory=list)
    flows: list[Flow] = Field(default_factory=list)
    events: list[Event] = Field(default_factory=list)
    goals: list[Goal] = Field(default_factory=list)
    beliefs: list[Belief] = Field(default_factory=list)
    preferences: list[Preference] = Field(default_factory=list)
    risk_statements: list[RiskStatement] = Field(default_factory=list)
    aggregates: list[AggregateStatement] = Field(default_factory=list)
    negatives: list[NegativeStatement] = Field(default_factory=list)
    unstructured: list[str] = Field(
        default_factory=list, description="Trechos literais do texto que não couberam em nenhum campo."
    )

    @model_validator(mode="after")
    def _check_references(self):
        items: list[Item] = [
            *self.people, *self.assets, *self.liabilities, *self.flows, *self.events, *self.goals,
            *self.beliefs, *self.preferences, *self.risk_statements, *self.aggregates, *self.negatives,
        ]
        ids = [item.id for item in items]
        repeated = sorted({i for i in ids if ids.count(i) > 1})
        if repeated:
            raise ValueError(f"ids repetidos: {repeated}")

        person_refs = [
            *(h.person_id for a in self.assets for h in _values(a.holders)),
            *(h.person_id for l in self.liabilities for h in _values(l.holders)),
            *(p for f in self.flows for p in _values(f.people)),
            *(p for e in self.events for p in _values(e.actors) + _values(e.beneficiaries)),
            *(p for g in self.goals for p in _values(g.people)),
            *(p for b in self.beliefs for p in b.holders),
            *(p for r in self.preferences for p in r.people),
            *(s.person_id for s in self.risk_statements),
            *(s.relative_to for s in self.risk_statements if s.relative_to),
            *(p for n in self.negatives for p in n.people),
        ]
        asset_refs = [
            *(f.asset_id for f in self.flows if f.asset_id),
            *(e.asset_id for e in self.events if e.asset_id),
            *(a for l in self.liabilities for a in _values(l.collateral_asset_id)),
        ]
        liability_refs = [f.liability_id for f in self.flows if f.liability_id]
        quantities = [
            *(q for x in [*self.flows, *self.events, *self.goals] for q in _values(x.amount)),
            *(s.quantity for s in self.aggregates),
        ]
        share_refs = [q.of_ref for q in quantities if isinstance(q, Share) and q.of_ref]

        for kind, refs, valid in (
            ("pessoa", person_refs, {p.id for p in self.people}),
            ("ativo", asset_refs, {a.id for a in self.assets}),
            ("passivo", liability_refs, {l.id for l in self.liabilities}),
            ("item", share_refs, set(ids)),
        ):
            missing = sorted(set(refs) - valid)
            if missing:
                raise ValueError(f"referência a {kind} inexistente: {missing}")
        return self


def _values(declared: Declared) -> list:
    if declared.value is None:
        return []
    return declared.value if isinstance(declared.value, list) else [declared.value]
