boxes = []
count = 0
number = input("quantity:")
while True:
    count += 1    
    text = input()
    boxes.append(text)
    if count == int(number):
         break

print(boxes)