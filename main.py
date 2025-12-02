people = ["Edvino","Anthony","Ed","Robin","Arhum"]
print("Who is signing in?")
print("Is this Edvino,Anthony,Ed,Robin,or Arhum?")
choice= input()
if choice in people:
    print()
    print("Welcome,",choice)
else:
    print ("Person not avaiable")
print()

def content():
    print("Hi,",choice)
    print("Hope you enjoy learning python with us!")
    print()
    print("Best,")
    print("The 3l337 AP Computer Science Team")
    return content()

file_inscrib= "inscribed.txt"
with open(file_inscrib,"e" ) as file
