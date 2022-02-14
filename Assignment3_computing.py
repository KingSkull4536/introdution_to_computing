## Question1


input_string = input("Enter the string: ").lower().replace(","," ").split()                         
if len(input_string) == 1:
    input_string = input_string[0]
occurences = {}
for i in input_string:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
print("The occurence(s) of:")
for i in occurences:
    print("'%s' is/are %d" % (i,occurences[i]))



##question2

          
def is_leap_year(year: int) -> bool:                                                     #Checking whether the given year is leap year or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print("Kindly enter natural numbers only. If fractional number is added then it will be rounded of to lesser integer")
    
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))



##Question3


input_list=eval(input("Enter the list of integers separated by commas:"))
output=[]
for i in input_list:
    output.append((i,i**2))
print("The list with their squares-",output)


## Question4


given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         
    grade_point = eval(input("Enter the grade of student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                             
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))
            break



##Question5

        
string="ABCDEFGHIJK"
i=0
while len(string)-i*2>0:
    print(" "*i+string[0:len(string)-i*2])
    i+=1



##Question6

    
dict1 = {}
while True:                                                                                                         
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? Enter Y if yes otherwise enter N")
        if more_data in ("N","n"):
            more_data = 0
            break
        elif more_data in ("Y","y"):
            more_data = 1
            break
        else:
            print("\nPlease enter Y or N only")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")                                                                                     
for i in dict1:
    print("The SID of %s is %d" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       
for i in dict2:
    print("The SID of %s is %d" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                   
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        
for i in dict3:
    print("The SID of %s is %d" % (dict3[i],i))
print("\nd. ", end="")                                                                                              
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is %s" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue



##Question7


a = 0
b = 1
sum = 0
while True:                                                                                                         
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break

##Question8

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)

