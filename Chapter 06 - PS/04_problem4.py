a = input("Enter your name: ")

if(len(a)>10):
    print("It contain more than 10 characters:", len(a))

elif(len(a)==10):
    print("It contain 10 characters:", len(a))

else:
    print("It contain less than 10 characters:", len(a))