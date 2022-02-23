import random


life = 3
print("life:",life)
while True:
    mynumber = input("Choose number between 1-10:")
    number = random.randint(1,10)
    if mynumber == "exit":
        break
    try:
        mynumber = int(mynumber) # beat
    except:
      print("==================")
      print("Must be number!!")
      print("==================")
      continue

    if int(mynumber) > 10:
        print("Choose number between 1-10!!!")
        print("life:",life)
    elif int(mynumber) < 1:
        print("Choose number between 1-10!!!")
        print("life:",life)
    elif int(mynumber) != number:
        life -= 1
        print("noob")
        print("life:",life)

    # if int(mynumber) != int(mynumber):
    #     print("Number not letter!!!")
    if life <= 0:
        print("noob\n""number is",number)
        life = 3
        print("again")
    if int(mynumber) == number:
        print("bansai\n""notbad\n""life:",life)