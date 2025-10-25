def goodday(name, ending="Thank you"):   # Yaha pr ending hmne by default save kr diya hai.
    print(f"Good Day, {name}")
    print(ending)


goodday("Vinayak", "Thanks") # yaha pr ending hmne 'thanks' diya to print 'thanks' hi krega.
goodday("Alok")  # But yaha pr ending nhi diya hai to by default wala le lega 'thank you'.