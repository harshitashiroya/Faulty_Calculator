"""
Design a calculator which will correctly solve all the problems except the following ones:
45*3=555, 56+9=77, 56/6=4
your program should take operator and the two numbers as input form user and then return the result.
Note: Use only if...else statements not use any functions.
"""
print("enter first number:")
num1 = int(input())
print("enter second number:")
num2 = int(input())
print("enter the operator: +,-,*,/,%")
op=input()

if num1==56 and num2==9 and op=="+":
    print("77")
elif num1==45 and num2==3 and op=="*":
    print("555")
elif num1==56 and num2==6 and op=="/":
    print("4")
elif op=="+":
    ans=num1+num2
    print(ans)
elif op=="-":
    ans=num1-num2
    print(ans)
elif op=="*":
    ans=num1*num2
    print(ans)
elif op=="/":
    ans=num1/num2
    print(ans)
elif op=="%":
    ans=num1%num2
    print(ans)
else:
    print("Error! please check your input")




