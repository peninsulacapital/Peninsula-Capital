import pytest
from pydantic import ValidationError

from agente.schemas import (
    AggregateKind,
    AggregateStatement,
    Asset,
    AssetCategory,
    Belief,
    ClientProfile,
    CurrencyShare,
    Declared,
    Event,
    EventKind,
    FamilyRole,
    Firmness,
    Flow,
    FlowCategory,
    FlowDirection,
    Money,
    NegativeStatement,
    Periodicity,
    Person,
    ProfileSection,
    Quantity,
    RiskStatement,
    RiskStatementKind,
    Share,
    Status,
    ValueBasis,
)

STATED = Status.STATED


def brl(amount: float) -> Money:
    return Money(amount=amount, currency="BRL")


def test_not_said_is_absent_by_default():
    assert Declared[int]().status is Status.ABSENT


def test_declared_value_requires_excerpt():
    with pytest.raises(ValidationError, match="trecho"):
        Declared[int](status=STATED, value=60)


def test_stated_requires_value():
    with pytest.raises(ValidationError, match="exige valor"):
        Declared[int](status=STATED, excerpt="O PAI, 60")


def test_absent_rejects_value():
    with pytest.raises(ValidationError, match="ausente"):
        Declared[int](status=Status.ABSENT, value=60)


def test_approximate_may_have_no_value():
    age = Declared[int](status=Status.APPROXIMATE, excerpt="A FILHA — JOVEM", note="jovem, idade não dita")
    assert age.value is None


def main_case_fragment() -> ClientProfile:
    return ClientProfile(
        people=[
            Person(
                id="p1", description="o pai, produtor rural", excerpt="O PAI, 60 — PRODUTOR RURAL EM GOIÁS",
                role=FamilyRole.PRINCIPAL,
                age=Declared[int](status=STATED, value=60, excerpt="O PAI, 60"),
            ),
            Person(
                id="p2", description="a filha", excerpt="A FILHA — JOVEM, SEM FAMÍLIA CONSTITUÍDA",
                role=FamilyRole.CHILD,
                age=Declared[int](status=Status.APPROXIMATE, excerpt="A FILHA — JOVEM", note="jovem"),
            ),
        ],
        assets=[
            Asset(
                id="a1", description="fazenda de grãos em Goiás", excerpt="FAZENDA DE GRÃOS EM GOIÁS",
                category=AssetCategory.REAL_ESTATE,
                current_value=Declared[Money](status=STATED, value=brl(300e6), excerpt="AVALIADA EM R$ 300MM"),
                acquisition_cost=Declared[Money](
                    status=STATED, value=brl(20e6), excerpt="CUSTO DE AQUISIÇÃO R$ 20MM"
                ),
            ),
        ],
        flows=[
            Flow(
                id="f1", description="renda líquida da fazenda", excerpt="A FAZENDA GERA R$ 10MM/ANO LÍQUIDOS",
                direction=FlowDirection.INCOME, category=FlowCategory.ASSET_INCOME, asset_id="a1",
                amount=Declared[Quantity](status=STATED, value=brl(10e6), excerpt="GERA R$ 10MM/ANO LÍQUIDOS"),
                periodicity=Declared[Periodicity](status=STATED, value=Periodicity.ANNUAL, excerpt="R$ 10MM/ANO"),
            ),
            Flow(
                id="f2", description="gasto da família", excerpt="A FAMÍLIA — R$ 10MM/ANO EM TERMOS REAIS",
                direction=FlowDirection.EXPENSE, category=FlowCategory.LIVING_EXPENSE,
                amount=Declared[Quantity](status=STATED, value=brl(10e6), excerpt="R$ 10MM"),
                periodicity=Declared[Periodicity](status=STATED, value=Periodicity.ANNUAL, excerpt="/ANO"),
                basis=Declared[ValueBasis](status=STATED, value=ValueBasis.REAL, excerpt="EM TERMOS REAIS"),
                currency_mix=Declared[list[CurrencyShare]](
                    status=STATED,
                    value=[CurrencyShare(currency="BRL", percent=80), CurrencyShare(currency="USD", percent=20)],
                    excerpt="CESTA DE GASTOS 80% EM REAIS E 20% EM DÓLARES",
                ),
                people=Declared[list[str]](
                    status=Status.AMBIGUOUS, excerpt="A FAMÍLIA — R$ 10MM/ANO",
                    note="não fica claro se inclui os gastos da filha",
                ),
            ),
            Flow(
                id="f3", description="gasto anual da filha", excerpt="OS GASTOS ANUAIS DELA, DE 4% EM TERMOS REAIS",
                direction=FlowDirection.EXPENSE, category=FlowCategory.LIVING_EXPENSE,
                amount=Declared[Quantity](
                    status=STATED,
                    value=Share(percent=4, of_description="os R$ 25MM destinados a ela", of_ref="e1"),
                    excerpt="DE 4%",
                ),
                basis=Declared[ValueBasis](status=STATED, value=ValueBasis.REAL, excerpt="EM TERMOS REAIS"),
                periodicity=Declared[Periodicity](status=STATED, value=Periodicity.ANNUAL, excerpt="GASTOS ANUAIS"),
                people=Declared[list[str]](status=STATED, value=["p2"], excerpt="OS GASTOS ANUAIS DELA"),
            ),
        ],
        events=[
            Event(
                id="e1", description="doação à filha", excerpt="O PAI QUER DESTINAR A ELA R$ 25MM",
                kind=EventKind.DONATION,
                firmness=Declared[Firmness](status=STATED, value=Firmness.FIRM, excerpt="O PAI QUER DESTINAR"),
                amount=Declared[Quantity](status=STATED, value=brl(25e6), excerpt="DESTINAR A ELA R$ 25MM"),
                actors=Declared[list[str]](status=STATED, value=["p1"], excerpt="O PAI QUER DESTINAR"),
                beneficiaries=Declared[list[str]](status=STATED, value=["p2"], excerpt="DESTINAR A ELA"),
            ),
            Event(
                id="e2", description="venda da fazenda, com proposta firme de compra",
                excerpt="COM PROPOSTA FIRME DE COMPRA", kind=EventKind.ASSET_SALE, asset_id="a1",
            ),
        ],
        beliefs=[
            Belief(
                id="b1", description="a renda dos R$ 25MM cobre os gastos da filha",
                excerpt="ACREDITA QUE A RENDA DISSO COBRE OS GASTOS ANUAIS DELA", holders=["p1"],
            ),
        ],
        risk_statements=[
            RiskStatement(
                id="s1", description="a filha aceita mais risco que o pai", excerpt="ACEITA MAIS RISCO QUE O PAI",
                person_id="p2", kind=RiskStatementKind.COMPARATIVE, relative_to="p1",
            ),
        ],
        aggregates=[
            AggregateStatement(
                id="t1", description="patrimônio total", excerpt="PATRIMÔNIO R$ 400 MM",
                kind=AggregateKind.TOTAL_WEALTH, quantity=brl(400e6),
            ),
        ],
        negatives=[
            NegativeStatement(
                id="n1", description="ninguém tem renda de trabalho",
                excerpt="NEM O PAI NEM A FILHA TÊM RENDA DE TRABALHO", section=ProfileSection.FLOWS,
                people=["p1", "p2"],
            ),
        ],
    )


def test_main_case_fragment_survives_json_round_trip():
    profile = main_case_fragment()
    assert ClientProfile.model_validate_json(profile.model_dump_json()) == profile


def test_undecided_sale_has_absent_firmness():
    sale = next(e for e in main_case_fragment().events if e.kind is EventKind.ASSET_SALE)
    assert sale.firmness.status is Status.ABSENT


def test_rejects_reference_to_unknown_person():
    data = main_case_fragment().model_dump()
    data["beliefs"][0]["holders"] = ["p9"]
    with pytest.raises(ValidationError, match="pessoa inexistente"):
        ClientProfile.model_validate(data)


def test_rejects_share_based_on_unknown_item():
    data = main_case_fragment().model_dump()
    data["flows"][2]["amount"]["value"]["of_ref"] = "e9"
    with pytest.raises(ValidationError, match="item inexistente"):
        ClientProfile.model_validate(data)


def test_rejects_repeated_ids():
    data = main_case_fragment().model_dump()
    data["assets"][0]["id"] = "p1"
    with pytest.raises(ValidationError, match="ids repetidos"):
        ClientProfile.model_validate(data)


def test_rejects_fields_outside_the_schema():
    data = main_case_fragment().model_dump()
    data["people"][0]["perfil_risco"] = "conservador"
    with pytest.raises(ValidationError):
        ClientProfile.model_validate(data)
