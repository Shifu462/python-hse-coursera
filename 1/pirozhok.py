worth_roubles = int(input())   # A
worth_kopeykas = int(input())  # B
pirozhok_count = int(input())  # N

all_pirozhoks_worth_roubles = worth_roubles * pirozhok_count
all_pirozhoks_worth_kopeykas = worth_kopeykas * pirozhok_count

all_pirozhoks_worth_roubles += all_pirozhoks_worth_kopeykas // 100
all_pirozhoks_worth_kopeykas = all_pirozhoks_worth_kopeykas % 100

print(all_pirozhoks_worth_roubles, all_pirozhoks_worth_kopeykas)
