from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.transactions.append(Amount(amount, "DEPOSIT"))
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.transactions.append(Amount(amount, "WITHDRAWAL"))
            self.balance -= amount
        else:
            print("Недостаточно средств!")

    def print_transaction_history(self):
        if not self.transactions:
            print("Нет транзакций.")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account: {self.account_holder}, Balance: {self.balance}"

# Ввод данных
account_holder = input("Введите имя владельца счета: ")
account_number = input("Введите номер счета: ")
account = PersonalAccount(account_number, account_holder)

# Меню
while True:
    print("\n1. Пополнить счет\n2. Снять средства\n3. Баланс\n4. История\n5. Выйти")
    choice = input("Выберите операцию: ")

    if choice == '1':  # Пополнение
        try:
            amount = float(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        except ValueError:
            print("Ошибка: введите число.")
    elif choice == '2':  # Снятие
        try:
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        except ValueError:
            print("Ошибка: введите число.")
    elif choice == '3':  # Баланс
        print(f"Баланс: {account.get_balance()}")
    elif choice == '4':  # История
        account.print_transaction_history()
    elif choice == '5':  # Выход
        break
    else:
        print("Неверный выбор.")
