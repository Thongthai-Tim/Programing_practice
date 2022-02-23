names = ["Hu Tao","Ganyu","Raiden","Eula"]
while True:
    name = input("name: ")
    if(name) == "exit": 
        print("bye")
        break
    names.append(name)
    print(names)