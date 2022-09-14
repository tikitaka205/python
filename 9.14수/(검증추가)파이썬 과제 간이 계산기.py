
class cal():

    def __init__(self, num1, num2):
        self.num1= num1
        self.num2= num2

    def plus(self):
        return(self.num1+self.num2)
    

    def minus(self):
        return(self.num1-self.num2)

    def multi(self):
        return(self.num1*self.num2)

    def div(self):
        try:
            print(self.num1/self.num2)
        # except:
        #     print("0이 아닌 숫자로 나눠주세요.")
        except ValueError:
            print("숫자를 입력해주세요")
        except ZeroDivisionError:
            print("나누기 0 불가")
while True:
    try: 
        a,b=map(float, input("두개의 숫자를 입력하세요. : ").split())
        num=cal(a,b)
        calculate=input("계산 방식입력 : ")

        if calculate == "+":
            print(num.plus())
        elif calculate == "-":
            print(num.minus())
        elif calculate == "*":
            print(num.multi())
        elif calculate == "/":
            print(num.div())

    except ValueError:
                print("숫자를 입력해주세요")
    except ZeroDivisionError:
                print("나누기 0 불가")
#여기에 어떻게 브레이크를 넣어야 할까

# if calculate == "+":
#     print(num.plus())
# elif calculate == "-":
#     print(num.minus())
# elif calculate == "*":
#     print(num.multi())
# elif calculate == "/":
#     print(num.div())

# def set_input():
#     num1= input("숫자를 입력하세요")
#     num2= input("숫자를 입력하세요")

# def run():
#     set_input()

# run()

# """
# a=cal()
# a.set
# """     
# num1,num2=map(int, input().split())
# cal.num(num1, num2)    
# a=cal()
# print(a.plus())

# a=cal(20, 문자)
# r=a.div()
# print(r)


