#define functions need, add, sub, mul, div
#print options to user
#ask values
#call the functions
#while loop to continue the program until exit

def add(a,b):
    answer = a + b
    print (f"{a} + {b} = {answer} \n")
    
def sub(a,b):
    answer = a - b
    print (f"{a} - {b} = {answer} \n")

def mul(a,b):
    answer = a * b
    print (f"{a} * {b} = {answer} \n")

def div(a,b):
    answer = a / b
    print (f"{a} / {b} = {answer} \n")

while True:

    print("A, Addition")
    print("B, substraction")
    print("C, multiplication")
    print("D, division")
    print("E, exit")

    choice = input ('input your choice: ')

    if choice == "A" or choice == "a":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a,b)

    elif choice == "B" or choice == "b":
        print("Substraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a,b)

    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mul(a,b)
    
    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a,b)

    elif choice == "E" or choice == "e":
        print("Program ended")
        quit()




