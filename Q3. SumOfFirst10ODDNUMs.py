#Q3. write a program to find sum of first 10 odd numbers. Using While loop

sum=0
n=0
while n<=20:
    if n % 2 != 0:
        sum += n
    n += 1
print("The sum of first 10 odd numbers is : ", sum)        
