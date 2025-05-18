import pytest
from unittest.mock import Mock
from bank import BankAccount

# Фікстура для створення банківського рахунку
@pytest.fixture
def account():
    return BankAccount()

# Мок для зовнішнього API (наприклад, для перевірки балансу)
class ExternalAPI:
    def get_balance(self):
        # Уявний виклик до зовнішнього сервісу
        pass

@pytest.fixture
def external_api_mock():
    mock = Mock(spec=ExternalAPI)
    mock.get_balance.return_value = 100.0
    return mock

# Параметризовані тести депозиту
@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (100, 100),
    (50.5, 50.5),
    (1, 1),
])
def test_deposit(account, deposit_amount, expected_balance):
    account.deposit(deposit_amount)
    assert account.get_balance() == expected_balance

# Параметризовані тести зняття коштів
@pytest.mark.parametrize("initial_balance, withdraw_amount, expected_balance", [
    (100, 50, 50),
    (200, 100.5, 99.5),
    (50, 50, 0),
])
def test_withdraw(account, initial_balance, withdraw_amount, expected_balance):
    account.deposit(initial_balance)
    account.withdraw(withdraw_amount)
    assert account.get_balance() == expected_balance

# Тест з використанням мока для перевірки взаємодії із зовнішнім API
def test_external_api_balance_check(external_api_mock):
    # Імітуємо виклик зовнішнього API
    balance = external_api_mock.get_balance()
    external_api_mock.get_balance.assert_called_once()
    assert balance == 100.0

# Пропускаємо тест зняття, якщо рахунок порожній
@pytest.mark.skipif(True, reason="Скипаємо тест зняття для порожнього рахунку")
def test_withdraw_skip_if_empty(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(10)

# Тестування помилок на депозит і зняття
def test_deposit_negative_amount_raises(account):
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw_negative_amount_raises(account):
    with pytest.raises(ValueError):
        account.withdraw(-10)

def test_withdraw_insufficient_funds_raises(account):
    account.deposit(10)
    with pytest.raises(ValueError):
        account.withdraw(20)
