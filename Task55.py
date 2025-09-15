# Read data (students, apples)
n=int(input('Enter the number of students: '))
k=int(input('Enter the number of apples: '))

# Calculations (division by whole, remainder)
a=k//n
b=k%n

# Output results
print(f"Each student will receive: {a} apple(s)")
print(f"Will remain in the cart: {b} apple(s)")