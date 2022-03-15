from art import logo



#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1*n2

#Division
def divide(n1, n2):
  return n1/n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))  
  
  should_continue = True
  while should_continue == True:
  
    num2 = float(input("What's the next number? "))
    
    for symbol in operations:
      print(symbol)
    
    opr = input("Pick an operation from the above! ")
    func_name = operations[opr]
    answer = func_name(num1, num2)
    print(f"{num1} {opr} {num2} = {answer}")
    continue_ = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
  
    if continue_ == 'y':
      num1 = answer
    else: 
      should_continue = False
      calculator()

calculator()
