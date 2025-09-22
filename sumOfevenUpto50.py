# Q1. Write a prg to find a sum of all the even numbers 

sum=0
for i in range (1,51):
    if i % 2 == 0:
        sum+=i
        print(sum)
print("The sum of all the even number upto 50 is : ", sum)        
