class Number:
    def __init__(self, number: int | float, isQuestion: str = "Yes", isNot: str = "No"):
        self.__number = number
        self.__isQuestion = isQuestion
        self.__isNot = isNot

        # self(isQuestion="No")
        # RecursionError
        # self.will = Number(number=self.__number, isQuestion="No", isNot=self.__isNot)
        # self.would = Number(number=self.__number, isQuestion="No", isNot=self.__isNot)
        # self.must = Number(number=self.__number, isQuestion="No", isNot=self.__isNot)

        self.can = self
        self.could = self
        self.may = self
        self.might = self
        self.able = self
        self.going = self
        self.to = self
        
        # self.NOT = self(isNot = not self.__isNot)
        # RecursionError
        # self.NOT = Number(number=self.__number, isQuestion=self.__isQuestion, isNot="Yes" if self.__isNot=="No" else "No")
        self.be = self
        self.are = self
        self.am = self
    @property
    def will(self):
        return Number(number=self.__number, isQuestion="No", isNot=self.__isNot)
    @property
    def would(self):
        return Number(number=self.__number, isQuestion="No", isNot=self.__isNot)
    @property
    def must(self):
        return Number(number=self.__number, isQuestion="No", isNot=self.__isNot)
    @property
    def NOT(self):
        return Number(number=self.__number, isQuestion=self.__isQuestion, isNot="Yes" if self.__isNot=="No" else "No")

    def is_six_seven(self) -> bool | Number:
        if self.__isQuestion == "Yes":
            if self.__isNot == "Yes": return self.__returnBool(not(self.__number == 67 or self.__number == -67))
            else: return self.__returnBool(self.__number == 67 or self.__number == -67)
        else: return Number(67)
    # def is_six(self) -> bool: return self.__returnBool(self.number == 6)
    # def is_seven(self) -> bool: return self.__returnBool(self.number == 7)

    # Number(4).must.be.six_seven()
    def six_seven(self) -> bool | Number:
        if self.__isQuestion == "Yes":
            if self.__isNot == "Yes": return self.__returnBool(not(self.__number == 67 or self.__number == -67))
            else: return self.__returnBool(self.__number == 67 or self.__number == -67)
        else:
            if self.__isNot == "Yes": raise Exception("Then why do you use this?")
            else: return Number(67)

    # def es(self) -> Number: return self # 스페인어는 애매함
    # Number(67).can().be().
    # def are(self) -> Number: return self
    # def be(self) -> Number: return self
    # def will(self) -> Number: return self
    # def can(self) -> Number: return self
    # def could(self) -> Number: return self
    # def may(self) -> Number: return self
    # def might(self) -> Number: return self
    # def should(self) -> Number: return self
    
    def plus(self, number) -> Number:
        if isinstance(number, Number): value = self.__number + number.__number
        else: value = self.__number + number
        return Number(value)

    def minus(self, number) -> Number:
        if isinstance(number, Number): value = self.__number - number.__number
        else: value = self.__number - number
        return Number(value)

    # 그냥 .plus().plus().plus().plus().plus().... 하세요;;
    # def multiply(self, number) -> Number:
    #     return Number * number

    # def divide(self, number) -> Number:
    #     return Number / number
    

    def __returnBool(self, bool) -> str:
        if bool: return "Yes"
        else: return "No"


    # 개 시바꺼 노가다 와다ㅏ다다다다다다다다다다다다ㅏ다다다다다ㅏ다
    def __str__(self) -> str:
        return str(self.__number)

    def __int__(self) -> int:
        return self.__number

    def __add__(self, other):
        # if isinstance(other, Number): value = self.__number + other.number
        # else: value = self.__number + other
        
        # return Number(value)
        raise Exception("Use .plus() method")

    def __sub__(self, other):
        # if isinstance(other, Number): value = self.__number - other.number
        # else: value = self.__number - other
        
        # return Number(value)
        raise Exception("Use .minus() method")
    def __rsub__(self, other):
        # if isinstance(other, Number): value = other.number - self.__number
        # else: value = other - self.__number

        # return Number(value)
        raise Exception("Use .minus() mothod")

    def __mul__(self, other):
        if isinstance(other, Number): value = self.__number * other.number
        else: value = self.__number * other

        return Number(value)
    
    def __truediv__(self, other):
        if isinstance(other, Number): value = self.__number / other.number
        else: value = self.__number / other

        return Number(value)
    def __rtruediv__(self, other):
        if isinstance(other, Number): value = other.number / self.__number
        else: value = other / self.__number

        return Number(value)

    def __floordiv__(self, other):
        if isinstance(other, Number): value = self.__number // other.number
        else: value = self.__number // other

        return Number(value)
    def __rfloordiv__(self, other):
        if isinstance(other, Number): value = other.number // self.__number
        else: value = other // self.__number

        return Number(value)

    def __eq__(self, other):
        if isinstance(other, Number): value = self.__number == other.number
        else: value = self.__returnBool(self.__number == other)

        return value

    def __lt__(self, other):
        if isinstance(other, Number): value = self.__number < other.number
        else: value = self.__returnBool(self.__number < other)

        return value
    def __le__(self, other):
        if isinstance(other, Number): value = self.__number <= other.number
        else: value = self.__returnBool(self.__number <= other)
        
        return value
    
    def __gt__(self, other):
        if isinstance(other, Number): value = other.number < self.__number
        else: value = self.__returnBool(other < self.__number)
        
        return value
    def __ge__(self, other):
        if isinstance(other, Number): value = other.number <= self.__number
        else: value = self.__returnBool(other <= self.__number)

        return value