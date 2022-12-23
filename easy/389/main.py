# 10/05/2021

import random


alice, bob, carol, dave, erin, frank, gina = (0,) * 7

for prize in random.choices((1, 2, 3), k=1000):
    alice += prize == 1

for prize in random.choices((1, 2, 3), k=1000):
    bob += prize != 1

for prize in random.choices((1, 2, 3), k=1000):
    pick = random.randint(1, 3)
    show = random.choice(tuple({1, 2, 3} - {prize, pick}))
    pick = random.choice(tuple({1, 2, 3} - {show}))
    carol += prize == pick

for prize in random.choices((1, 2, 3), k=1000):
    pick = random.randint(1, 3)
    dave += prize == pick

for prize in random.choices((1, 2, 3), k=1000):
    pick = random.randint(1, 3)
    erin += prize != pick

for prize in random.choices((1, 2, 3), k=1000):
    show = random.choice(tuple({2, 3} - {prize}))
    pick = 2 if show != 2 else 1
    frank += prize == pick

strat = 1
for prize in random.choices((1, 2, 3), k=1000):
    gina += strat * (prize == 1) + (not strat) * (prize != 1)
    strat = prize == 1


print(f"alice: {alice / 1000}")
print(f"bob:   {bob / 1000}")
print(f"carol: {carol / 1000}")
print(f"dave:  {dave / 1000}")
print(f"erin:  {erin / 1000}")
print(f"frank: {frank / 1000}")
print(f"gina:  {gina / 1000}")
