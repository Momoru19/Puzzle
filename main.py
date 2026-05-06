password = input("Enter access key: ")

if password == "second-level":
    with open("secret.txt") as f:
        print(f.read())
else:
    print("Access denied")
