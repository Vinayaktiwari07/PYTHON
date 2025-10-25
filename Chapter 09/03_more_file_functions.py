f = open("file.txt")
# Ye comlete file read krega single command me.
# lines = f.readlines()
# print(lines, type(lines))

# Ye line by line read krega multiple command dena hoga.
# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 == "")

# While loop ka use kr ke print krenge
line  = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()