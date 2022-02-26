import random

c = 0
boxes = []
while True:
    number = random.randint(1,10)
    if number not in boxes: 
        boxes.append(number)
        c += 1
    print(boxes)
    # if len(boxes) == 10:
    if c == 10:
        boxes.sort()
        print(boxes)
        break