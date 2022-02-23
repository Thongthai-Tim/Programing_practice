array = ["beat","tim","mate","jame","bank"]
print("Out of these five words in order start from 1-5. What number of words do you want to choose.:", array)
print("==============================================")
number = input("I want the words:")
number = int(number) - 1
if int(number) == 0:
    print(array[0])
if int(number) == 1:
    print(array[1])
if int(number) == 2:
    print(array[2])
if int(number) == 3:
    print(array[3])
if int(number) == 4:
    print(array[4])