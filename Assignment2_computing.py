## Question 1
a='Python is a case sensitive language'

## (a) Length of string
print("Length of the given string is ", len(a))

## (b) Reversing a string
print("When written backwards the string becomes ", a[len(a)::-1])

## (c) slicing
b=a[10:26]
print(b)

## (d) replacing some part with other input 
print(a.replace("a case sensitive", "object oriented"))

## (e) index of substring
print(a.index('a'))

## (f) removing white spaces from given input
print(a.replace(" ", ""))
    



## question 2
## storing data using string formatting

name=str(input("Enter your name-"))
sid=int(input("Enter your student ID-"))
department=str(input("Enter your opted branch/program-"))
cgpa=float(input("Enter the CGPA:"))
print('''Hey, %s Here!
      My SID is %d
      I am from %s department and my CGPA is %f'''%(name,sid,department,cgpa))


## question 3
## using bitwise operater to simplify binary claculations of given numbers

a=56
b=10

print("a&b = ", a & b)
print("a|b = ", a | b)
print("a^b = ", a^b)
print("On shifting the binary representation of 56 leftwards twice, it becomes", a<<2)
print("On shifting the binary representation of 10 leftwards twice, it becomes", b<<2)
print(a>>2)
print(b>>4)



## question 4
## Comparing 3 numbers entered by user and giving the largest as output

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
temp=0      ## temporary no. to store the value of largest number

if(num1>num2 & num1>num3):
    temp=num1
elif(num2>num3):
        temp=num2
else:
            temp=num3

print("The largest number entered by you is ", temp)


## Question 5
## checking whether 'word' is present among the characters entered by user

sentence=str(input("Type the input:"))
if "name" in sentence:
    print("Yes")
else:
        print("No")


## Question 6
## checking whether the given three sides can form a triangle        


a=int(input("Enter the length of first side of triangle:"))
b=int(input("Enter the length of second side of triangle:"))
c=int(input("Enter the length of third side of triangle:"))


if((a+b)>c and (b+c)>a and (c+a)>b): 
    print("Yes")
else:
        print("No")


















        
    

           
