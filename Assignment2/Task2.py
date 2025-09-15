n = 50

sum = 0
# Using a for loop
# for i in range(1, n + 1):
#     sum += i
# print(f"The sum of numbers from 1 to {n} is: {sum}")

# Using a while loop
while n > 0:
    sum += n
    n -= 1
print(f"The sum of numbers from 1 to 50 is: {sum}")