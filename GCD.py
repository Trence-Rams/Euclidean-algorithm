print("This program implements euclidean's algorithm to determine the greatest common divisor of two numbers.")
print("")
num1=int(input("Enter any positive integer value: "))
num2=int(input("Enter any positive integer value: "))
bignum=max(num1,num2)
smallnum=min(num1,num2)
while smallnum !=0:
    product=0
    num=0 
    while product<=bignum:  
         num+=1
         product=num*smallnum 
    product=smallnum*(num-1)
    smallnum=bignum-product
    bignum=product/(num-1)
print("The GCD is", int(bignum))
    
  


