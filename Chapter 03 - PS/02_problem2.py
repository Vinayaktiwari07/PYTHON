name = input("Enter your name: ")
date = "30 Sept 2024"

print(f"Dear {name},\nYou are selected! \n{date}")


# another way to solve
letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Vinayak").replace("<|Date|>", "24 sept 2025"))