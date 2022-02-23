numbers = [5,2,10,3,6]
total = 0
def max_loop(numbers):
    first = numbers[0]
    for n in numbers:
        if n > first:
            first = n
    return first
print("max: ",max_loop(numbers))
def min_loop(numbers):
    first = numbers[0]
    for n in numbers:
        if n < first:
            first = n
    return first
print("min: ",min_loop(numbers))
for box in numbers:
    total += box
print(float(total)/5)