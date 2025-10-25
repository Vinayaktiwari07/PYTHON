p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message),(p2 in message),(p3 in message),(p4 in message)):
    print("This is a spam comment")

else:    
    print("This is not a spam comment")
