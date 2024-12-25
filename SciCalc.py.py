import math
class ScientificCalculator:
    def __init__(self):
        print("\tSCIENTIFIC CALCULATOR")
        print("\t~~~~~~~~~~~~~~~~~~~~~")

    def trig(self):
        while True:
            print("\tCHOICES:"
            	  "\n1. SIN Function"
                  "\n2. COS Function"
                  "\n3. TAN Function"
                  "\n4. SIN–¹ Function"
                  "\n5. COS–¹ Function"
                  "\n6. TAN–¹ Function"
                  "\n7. EXIT")
            choice = input("Enter your choice:")


            if choice == "1":
                try:
                    angle = float(input("Enter a angle: "))
                    minutes=int(input("Enter minuits :"))
                    value=angle+minutes/60
                    radian=math.radians(value)
                    value = math.sin(radian)
                    print("The value for the radian is", value)
                    print("\n===============================")
                except ValueError:
                    print("INVALID INPUT,PLEASE ENTER AGAIN")

            elif choice =='2':
                try:
                    angle = float(input("Enter a angle: "))
                    minutes=int(input("Enter minuits :"))
                    value=angle+minutes/60
                    radian=math.radians(value)
                    value = math.cos(radian)
                    print("The value for the radian is", value)
                    print("\n===============================")
                except ValueError:
                    print("INVALID INPUT,PLEASE ENTER AGAIN")
            elif choice =='3':
                try:
                    angle = float(input("Enter a angle: "))
                    minutes=int(input("Enter minuits :"))
                    value=angle+minutes/60
                    radian=math.radians(value)
                    value = math.tan(radian)
                    print("The value for the radian is", value)
                    print("\n===============================")
                except ValueError:
                        print("INVALID INPUT,PLEASE ENTER AGAIN")
            elif choice =="4":
                try:
                    angle = float(input("Enter a angle: "))
                    minutes=int(input("Enter minuits :"))
                    value=angle+minutes/60
                    radian=math.radians(value)
                    value = math.asin(radian)
                    print("The value for the radian is", value)
                    print("\n===============================")
                except ValueError:
                    print("INVALID INPUT,PLEASE ENTER AGAIN")
            elif choice =="5":
                try:
                    angle = float(input("Enter a angle: "))
                    minutes=int(input("Enter minuits :"))
                    value=angle+minutes/60
                    radian=math.radians(value)
                    value = math.acos(radian)
                    print("The value for the radian is", value)
                    print("\n===============================")
                except ValueError:
                    print("INVALID INPUT,PLEASE ENTER AGAIN")
            elif choice =="6":
                try:
                    angle = float(input("Enter a angle: "))
                    minutes=int(input("Enter minuits :"))
                    value=angle+minutes/60
                    radian=math.radians(value)
                    value = math.atan(radian)
                    print("The value for the radian is", value)
                    print("\n===============================")
                except ValueError:
                    print("INVALID INPUT,PLEASE ENTER AGAIN")
            elif choice=="7":
                print("YOU HAVE EXITED FROM THE CHOICE")
                print("\n===============================")
                break
            else:
                print("THE CHOICE IS INVALID! PLEASE ENTER AGAIN!")   
                print("\n========================================")
                 
    def  log(self):
        while True:
            print("\tCHOICES:"
                  "\n1.Log value"
                  "\n2.Square value"
                  "\n3.Square root value"
                  "\n4.factorial"
                  "\n5.ln value"
                  "\n6.x-¹ value"
                  "\n7.Cube value"
                  "\n8.Cube root value"
                  "\n9.Exit")
            c=input("Enter your choice:") 
            try:
                if c=="1":
                    num=float(input("Enter a number:"))
                    log=math.log10(num)
                    print("The value of log=",log)
                    print("\n===============================")
                elif c =="2":
                    num=float(input("Enter a number:"))
                    square=num*num
                    print("The square =",square)
                    print("\n===============================")
                elif c=="3":
                    num=float(input("Enter a number:"))
                    sqrt=math.sqrt(num)
                    print("The square root=",sqrt)
                    print("\n===============================")
                elif c=="4":
                    num=int(input("Enter a number:"))    
                    fact=math.factorial(num)
                    print("The factorial of given number is",fact)
                    print("\n===============================")
                elif c=="5":
                    num=float(input("Enter a number:"))
                    ln=math.log(num)
                    print("The ln value=",ln)
                elif c=="6":
                    num=float(input("Enter a number:"))    
                    value=1/num
                    print("The inverse value=",value)
                elif c=="7":
                    num=float(input("Enter a number:"))
                    cb=num*num*num
                    print("The cube=",cb)
                elif c=="8":
                    num=float(input("Enter a number:"))
                    cbrt=round(num*(1/3),6)
                    print("The cubr root=",cbrt)
                elif c=="9":
                    print("YOU WERE EXITED FROM THE CHOICE!")
                    print("\n===============================")
                    break
                else:
                    print("INVALID EXPRESSION!PLEASE ENTER AGAIN!")
                    print("==========================================")
            except ValueError:
                print("INVALID INPUT!PLEASE ENTER IT AGAIN")
            except ZeroDivisionError:   
                print("CAN'T DIVIDE BY ZERO,PLEASE ENTER AGAIN")
    def arith(self):
        
        expression=0
        while True:
            num=input("Enter any expressions or 'q' to quit or 'c' to clear:")
            if num.lower()=="q":
                print("YOU WERE EXCITED FROM THE CHOICE!")
                print("=================================")
                break
            if num.lower()=="c":
                expression=0
                print("THE EXPRESSION IS CLEARD")
                continue
            try:
                value=eval(num)
                expression += value
                print("The current value:",expression)
                print("===========================")
            except ZeroDivisionError:
                print("CAN'T DIVIDE BY ZERO,PLEASE ENTER AGAIN")
            except (SyntaxError,NameError):
                print("INVALID EXPRESSION!PLEASE ENTER AGAIN")
            
if __name__ == "__main__":
    calculator = ScientificCalculator()
    while True:
        print("\tOPTIONS:"
              "\n1.TRIGNOMETRY AND IT'S INVERSE CALCULATION"
     	     "\n2.LOG AND SOME CALCULATION"
         	 "\n3.ARITHMETIC CALCULATION"
         	 "\n4.EXIT")
    
        option=input("Enter any option:")
        
        if option =="1":
            print("Welcome to TRIGONOMETRY calculation") 
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
       	 
            calculator.trig()
        elif option =="2":
            print("welcome to LOG AND SOME calculation")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            calculator.log()
        elif option=="3":
            print("welcome to ARITHMETIC calculation")    
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            calculator.arith()
        elif option =="4":
            print("YOU HAVE EXITED FROM THE PROGRAM!")
            print("THANK YOU, VISIT AGAIN")
            print("=================================")
            break
        else:
            print("INVALID OPTION!")
            print("===============")
            