# Read the data of moment 1 and 2 (hours, minutes, seconds)
print(f"Enter the time of moment 1")
h1=int(input('Hours: '))
m1=int(input('Minutes: '))
s1=int(input('Seconds: '))

print(f"Enter the time of moment 2")
h2=int(input('Hours: '))
m2=int(input('Minutes: '))
s2=int(input('Seconds: '))

# Calculations (create a formula)
T=((h2*3600)+(m2*60)+s2)-((h1*3600)+(m1*60)+s1)

# Output result
print(f"Difference between moments 1 and 2: {T}")
