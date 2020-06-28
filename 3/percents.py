from decimal import Decimal

deposit_multiplier = Decimal(int(input())) / Decimal(100)
r = Decimal(int(input()))
k = Decimal(int(input()))

deposit = r + k / Decimal(100)

withdraw = deposit + deposit * deposit_multiplier

withdraw_r = int(withdraw)
withdraw_k = (withdraw - int(withdraw)) * 100
withdraw_k = int(withdraw_k)

print(withdraw_r, withdraw_k)
