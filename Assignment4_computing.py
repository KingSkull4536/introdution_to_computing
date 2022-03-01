def TowerOfHanoi(n , initial, final, spare):
    if n == 0:
        return
    TowerOfHanoi(n-1, initial, spare, final)
    print("Move disk",n,"from rod",initial,"to rod",final)
    TowerOfHanoi(n-1, spare, final, initial)

print("Please enter natural number only :)")    
n=int(input("Enter the number of discs:"))
TowerOfHanoi(n, 'A', 'B', 'C')

##question 2

n = int(input("Enter the number of rows in Pascal's Triangle: "))

# using recursions


def pascal(n, orgnum=n):
    if n == 0:
        return

    pascal(n - 1, orgnum)

    
    print('  ' * (orgnum - n), end='')

   
    entry = 1
    for i in range(1, n + 1):
        print(entry, end='   ')

       
        entry = entry * (n - i) // i
    print()


pascal(n)

# using iteration
print("\nUsing loops:\n")
for line in range(1, n + 1):

    print('  ' * (n - line), end='')

    x = 1
    for i in range(1, line + 1):
        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")


# Question 3
print("Question 3")
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))


while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non zero number : "))

Q, R = divmod(a, b)
m = [Q, R]


def division():
    Q, R = divmod(a, b)
    print(f"Quotient:{Q}\nRemainder:{R}")


division()

print('a)')
print(callable(division))

print('b)')
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

print('c)')
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
filtered = filter(lambda n: n > 4, m)
print("Values greater than 4 are : ", list(filtered))

print('d)')
s = set(m)
print(s)

print('e)')
f_s = frozenset(s)
print("Immutable set : ", f_s)

print('f)')
m = max(f_s)
print(hash(str(m)))

print('\n')
# Question 4


class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")



student1 = Student("Prashant jyoti", 21105072)
print("Object created")


print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

# deleting object
del student1


# Question 5
print("Question 5")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name} record deleted")


a = Employee("Mehak", 40000)
b = Employee("Ashok", 50000)
c = Employee("Viren", 60000)

# a)

a.salary = 70000
print(f"The updated salary of the employee {a.name} is {a.salary}")

# b)

del c
print("Records of Viren are deleted")

print("\n")

# Question-6

gword = input("Enter the first word: ")

# Barbie's word
bword = input("Enter a new meaningful word to test your friendship: ")


def count_in_dict(gword):
    count = {}
    list1 = list(gword.lower())

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
# shopkeeper's input

ans = input("Is the word meaningful?(y or n)")

# test
if count_in_dict(gword) != count_in_dict(bword):
    print("The letters aren't exact, friendship is fake!!")




elif ans == 'y':
        print("Mission passed. Respect++")
elif ans == 'n':
        print("The word is meaningless, friendship is fake!!\n\n")

