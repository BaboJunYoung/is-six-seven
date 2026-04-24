# `is-six-seven` by BaboJunYoung
A python package checking 67

### Usage
Look `main.py` or `is_six_seven` library code
```python
from is_six_seven import Number

number = Number(67)
number = number.plus(67).minus(67)

print(number.is_six_seven()) # Yes
print(number.can.be.six_seven()) # Yes
print(number.could.be.six_seven()) # Yes
print(number.may.be.six_seven()) # Yes
print(number.might.be.six_seven()) # Yes
print(number.can.NOT.be.six_seven()) # No
print(number.am.six_seven()) # Yes
print(number.are.six_seven()) # Yes
print()
print(number.will.be.six_seven()) # 67
print(number.would.be.six_seven()) # 67
print(number.must.be.six_seven()) # 67
print(number.will.be.able.to.be.six_seven()) # 67

try:
    number = number.must.NOT.be.six_seven()
except Exception as e:
    print(e) # Then why do you use this?

try:
    number += 67
except Exception as e:
    print(e) # Use .plus() method

try:
    number -= 67
except Exception as e:
    print(e) # Use .minus() method

number *= 67
print(number) # 4489

number /= 67
print(number) # 67.0

number = int(number)
print(number) # 67

print(number == Number(67)) # Yes
print(number == Number(6767)) # No
```