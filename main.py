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

content = """
Hi, {choice}
Hope you enjoy learning python with us!

Best,
The 3l337 AP Computer Science Team
"""
print(content.format(choice=choice))
    

if choice in people:
    file_inscrib= "inscribed.txt"
    with open (file_inscrib, 'w') as fp:
        fp.write(str(content))
else:
    print("No file created")


