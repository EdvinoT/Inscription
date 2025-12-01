people = ["Edvino","Anthony","Ed","Robin","Arhum"]
print("Whom do you want to assign this project to?")
print("Your choices are Edvino,Anthony,Ed,Robin,and Arhum")
choice= input()
if choice in people:
    print()
    print(choice,",Has been chosen for this project.")
else:
    print ("Person not avaiable")


