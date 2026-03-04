#write a program to input two number and display their sum,differences,product and quotients
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("sum:",a+b)
print("Difference:",a-b)
print("product:",a*b)
print("Quotient:",a/b)

#program2
l = float(input("Enter length: "))
w = float(input("Enter width: "))
print("Area:", l * w)
print("Perimeter:", 2 * (l + w))

# Program 3
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Program 4
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Using a third variable
temp = x
x = y
y = temp
print("After swap (with temp): x =", x, "y =", y)

# Without using a third variable
x, y = y, x
print("After swap (without temp): x =", x, "y =", y)

# Program 5
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

 # Program 6
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Program 7
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Program 8
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

 # Program 9
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))

si = (p * r * t) / 100
print("Simple Interest:", si)

# Program 10
for i in range(1, 101):
    print(i, end=" ")

 # Program 11
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

 # Program 12
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)

# Program 13
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            print(num, "is not Prime")
            break
    else:
        print(num, "is Prime")
else:
    print(num, "is not Prime")

# Program 14
n = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

 # Program 15
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

# Program 16
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print(num, "is Palindrome")
else:
    print(num, "is not Palindrome")

# Program 17
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum of digits:", sum_digits)

# Program 18 - Directly print 4 rows
rows = 4

for i in range(1, rows + 1):
    print("*" * i)

# Program 19
text = input("Enter a string: ").lower()
vowels = "aeiou"
v_count = c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

# Program 20
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Program 21
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

# Program 22
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

# Program 23
s = input("Enter a string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Character frequencies:", freq)


# Program 24
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("String without duplicates:", result)


# Program 25
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())


# Program 26
s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

if sorted(s1) == sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")


 # Program 27
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest element:", max(lst))


# Program 28
lst = list(map(int, input("Enter numbers separated by space: ").split()))
unique = list(set(lst))
print("List without duplicates:", unique)


# Program 29
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Ascending:", sorted(lst))
print("Descending:", sorted(lst, reverse=True))


# Program 30
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of elements:", sum(lst))


# Program 31
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

merged = lst1 + lst2
print("Merged list:", merged)


# Program 32
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

common = list(set(lst1) & set(lst2))
print("Common elements:", common)


# Program 33
t = tuple(map(int, input("Enter tuple elements: ").split()))
print("Tuple:", t)
print("Sliced tuple (first 3 elements):", t[:3])


# Program 34
t = tuple(map(int, input("Enter tuple elements: ").split()))
element = int(input("Enter element to count: "))

print("Occurrence of", element, ":", t.count(element))


# Program 35
n = int(input("Enter number of students: "))
marks = {}

for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))
    marks[name] = score

highest = max(marks, key=marks.get)
print("Highest scorer:", highest, "with", marks[highest], "marks")


# Program 36
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print("Merged dictionary:", merged)


# Program 37
def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

n = int(input("Enter a number: "))
print(n, "is Prime" if is_prime(n) else "is not Prime")


# Program 38
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))


# Program 39
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD of", x, "and", y, "is", gcd(x, y))


# Program 40
def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string: ")
print("Palindrome" if is_palindrome(text) else "Not Palindrome")


# Program 41
def list_sum(lst):
    return sum(lst)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Sum:", list_sum(numbers))


# Program 42
def max_of_three(a, b, c):
    return max(a, b, c)

x, y, z = map(int, input("Enter three numbers: ").split())
print("Maximum:", max_of_three(x, y, z))


# Program 43
with open("students.txt", "w") as f:
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        f.write(name + " " + marks + "\n")

print("Student information written to students.txt")


# Program 44
with open("students.txt", "r") as f:
    content = f.read()
    print("File contents:\n", content)


    # Program 45
with open("students.txt", "r") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)


# Program 46
with open("students.txt", "a") as f:
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    f.write(name + " " + marks + "\n")

print("Data appended to students.txt")


# Program 47
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


    # Program 48
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found")

    