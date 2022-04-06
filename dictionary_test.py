dictionary = {"BBM450AN": 999, "BBM450W": 899, "BBM450X": 1299}
model = input("Enter model code: ").strip().upper()
print(model)

if model in dictionary:
    print("{} is here".format(model))
else:
    print("Sorry, I'm not here ;)")

