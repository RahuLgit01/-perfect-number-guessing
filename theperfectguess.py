import random
n = random.randint(1,100)
a= -1
guesses =1
while(a !=n):
    
    a = int(input("enter guess the number : "))
    if(a>n):
        print("lower number plz : ")
    elif(a<n):
        print("higher number plz : ") 
        guesses +=1
   
        
print(f"right guress{n} in {guesses} attempts")        
    