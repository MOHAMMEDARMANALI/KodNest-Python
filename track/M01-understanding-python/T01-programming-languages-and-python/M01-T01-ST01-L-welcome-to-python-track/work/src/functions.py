# def add():
#     print(10+10)
# add()

# def square():
#     print(5**2)
# square()

# def Largest():
#     a=10
#     b=20
#     if a>b:
#         print(a)
#     else:
#         print(b)
# # Largest()

# def square1():
#     a=5
#     print(a**2)
# square1()

# def square2():
#     a=6
#     return a**2
# print(square2())

# def square3(a):
#     print(a**2)
# square3(7)

# def square4(a):
#     return a**2
# print(square4(8))
age=int(input("Enter the age"))
if age >= 18:
    print("Eligible to vote")

age=int(input("Enter the age"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible")  

marks=int(input("Enter the marks"))
if marks>90:
    print("Grade A")
elif marks>70:
    print("Grade B")
elif marks>50:
    print("Grade C")
elif marks>35:
    print("Grade D")
else:
    print("Fail")

Iam_free=input("Are you free?(Yes/No)")
Friends_free=input("Friends are free?(Yes/No)")
if Iam_free == "yes":
    if Friends_free == "yes":
        print("Go to the party")
    else:
        print("Watch a movie")
else:
    print("Do homework")

day=int(input("Enter the day"))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid day number")

month=int(input("Enter the number"))
match month:
    case 1|2: print("Autum")
    case 3|4|5 : print("Summer")
    case 6|7|8 : print("Rainy")
    case 9|10|11|12 : print("Winter")
    case _: print("Invalid month number")


