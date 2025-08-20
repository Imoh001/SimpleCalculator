import math
print("Please note this is a simple calculator")
print("Use / for division")
print("Use * for multiplication")
print("Use + for addition")
print("Use - for substraction")
print("Use ** for raise to power")
print("Use % for looking for remainder")
print("You can also do some stuffs like find inequalities")
def calcu():
 calc = print(eval(input("Enter your operations: ")))
 if calc == True:
  return calc
again = "yes"
while again.lower() == "yes":
 calcu()
 again = input("Do you want to calculate again? yes or no: ")
