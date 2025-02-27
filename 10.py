a=int(input("Enter a number "))
count=0
for i in range (1,a+1):
    if a%i==0:
        count=count+1
    if count>2:
        print("its not a prime number")
        break
              
if count==2:
        print("its a prime number")
        
    