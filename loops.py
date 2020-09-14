# Practicing for loops and while loops

print()
print("Printing out Fall Schedule:")

schedule = ["data structures, linear algebra, philosophy"]

for subject in schedule: # Used "class" as the var name, but it's a keyword- 
    print(subject)

print()

print("Printing out STEM classes: ")
for subject in schedule:
    if subject == "philosophy" :
        break
    print(subject)