a=int(input("enter a number"))

def  prime(a):   

    if (a<= 1):    
         return False    
 
    for i in range(2,a): 
        if (a % i) == 0:       
         return False    
  return True  
  
 if (prime(a)): 
     print(a,"is a prime number") 
else : 
     print(a,"is not a prime number") 