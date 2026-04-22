from is_six_seven import Number

num = Number(66)
num = num.plus(2)
num = num.minus(1)
print(num)
print(num.may.be.six_seven()) # Yes
print()
try:
    num = num + 1
except Exception as e:
    print("ERROR!!!")
    print(f"Exception: {e}")
print()

import random

rand = Number(random.randint(60, 70))

print(f"rand = {rand}")

if rand.am.six_seven() == "No":
    print(f"Oh... no... it's not 67. It's {rand}")
    print("But I can make it 67")
    rand = rand.must.be.six_seven()
    print(f"Now, it is {rand}\n")

if rand.are.six_seven() == "Yes":
    print("AYYYYYY! AY!!!!! SIX SEVEN!!!!!!!!!!")
