marks = {
    "Vinayak": 100,
    "Rupesh": 99,
    "Alok": 99,
    0: "Abhi"
}

print(marks.items()) # Ye dictionary ko tuple ke form me dega.
print(marks.keys())  # Ye dictionary me use ki gyi keys dega.
print(marks.values())  # Ye dicttionary me use ki gyi values ko dega.


marks.update({"Vinayak": 99, "Raj": 77})  # Ye update bhi krta hai agr koi keys ya values nhi rhega to add bhi krega.
print(marks)

print(marks.get("Vinayak"))  # Ye dictionary se  keys ka value dega or agr keys nhi rhega to 'none' dega.


print(marks.get("Vinayak")) # Ye dono me difference ye hai ki Agr kays nhi rhega to ye 'NONE' dega
print(marks["Vinayak"])    # Or te 'ERROR' dega