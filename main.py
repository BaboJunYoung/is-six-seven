from is_six_seven import Number

age = Number(int(input("Input your age: ")))

adult_flag = True
for teen in range(67 - 0, 67 - 20, -1):
    if age.plus(teen).IS.six_seven() == "Yes":
        print("You are not adult.")
        adult_flag = False

if adult_flag:
    print("You are adult. You can enter.")