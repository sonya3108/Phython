from class_data import Bank, MIN_CAPITAL
import pytest


@pytest.fixture()
def bank_creation_payload() -> dict:
    payload = Bank(name='Poly', stakeholders=['Vinnyk'], capital=MIN_CAPITAL)
    return payload


@pytest.fixture()
def bank() -> Bank:
    bank = (Bank
        (name='Poly',
        stakeholders=['Vinnyk'],
         capital=MIN_CAPITAL))
    return bank
