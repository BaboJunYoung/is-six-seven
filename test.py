from is_six_seven import Number

number = Number(67)
number = number.plus(67).minus(67)

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
    number = number.must.NOT.be.six_seven() # Error
except Exception as e:
    print(e)