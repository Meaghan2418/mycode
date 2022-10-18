#!/usr/bin/env python3
""" M.Mahaffey Lists Challenge """

# import random module
import random

def listsChallenge():

    # enter variable data
    wordbank = ["indentation", "spaces"]
    tlgstudents = ["Meaghan", "Larry", "Joseph",
                  "Shalese", "Ryanne", "Latoya",
                  "Eric", "Brendan", "Jairo",
                  "Greg", "Darryl", "Nilantha",
                  "Rochelle", "Malcolm", "Chap",
                  "Tray", "Victor", "Changming"]

    # print the tlg list as shown above.
    # This helps to compare differences.
    print(tlgstudents)

    # append the integer 4 to the wordbank list and then print the new list
    wordbank.append(4)
    print(wordbank)

    #Bonus 2
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]


    print(f"The student you picked was {name}!")
    # print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    # Bonus 1
    name = random.choice(tlgstudents)
    print(f"{name}")

listsChallenge()


