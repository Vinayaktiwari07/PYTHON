s1 = int(input("Enter your marks of subject 1: "))
s2 = int(input("Enter your marks of subject 2: "))
s3 = int(input("Enter your marks of subject 3: "))

# Check for total percentage
total_percentage = (100*(s1 + s2 + s3))/300

if(s1>=33 and s2>=33 and s3>=33 and  total_percentage>=40):
    print(" You are Passed", total_percentage)

else:
    print("You are Failed", total_percentage)


