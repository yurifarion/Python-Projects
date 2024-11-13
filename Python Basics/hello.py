#Ask user for that name
name = input("Whats your name?")

#remove whitespace from str
name = name.strip().title()

#Say hello to user
print(f"hello, {name}")