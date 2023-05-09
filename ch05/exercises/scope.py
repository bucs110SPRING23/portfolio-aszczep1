

def multiply(num1, num2): 
    product = 0 
    for i in range(num2):
        product += num1
    return product 

def exponent(num1, num2): 
    answer = 1
    for i in range(num2): 
        answer *= num1  
    return answer 

def square(num1): 
    return multiply(num1, num1)

def main(): 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = multiply(num1, num2) 
    print(result)
    result = exponent(num1, num2)
    print(result) 

main()



