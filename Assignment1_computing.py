# ASSIGNMENT - 1 #


# 1. Average of three numbers #

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

print("The average of given numbers is ", (num1+num2+num3)/3)

# 2. Program for calculating income tax #

income=float(input("Enter your total income:"))
members=int(input("Enter your none earning family members:"))

taxable_income=float(income-10000-members*3000)

income_tax=taxable_income/5

if income_tax<0:
    print("You don't have to pay income tax.")

else:    
   print("Income tax to be paid is ", income_tax)


# 3. Storing data in form of list #

SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your Gender-(M,F,U) -  ")
course=input("Enter the course name-")
cgpa=float(input("Enter the CGPA-"))

Student=[SID,name,gender,course,cgpa]

print(Student)


# 4. Sorting marks of 5 students #

M1=float(input("Enter your marks:"))
M2=float(input("Enter your marks:"))
M3=float(input("Enter your marks:"))
M4=float(input("Enter your marks:"))
M5=float(input("Enter your marks:"))

Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)


# 5.1 Removing certain element from a list #


colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove('Black')
print(colour)

# 5.2 Overwriting elements of a list #

colour[3:5]=["Purple"]
print(colour)























