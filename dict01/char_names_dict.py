"""M.Mahaffey Character List Challenge"""

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


char_choice = input("Which character do you want to know about? ")

char_info = input(" What statistic do you want to know about? (real name, powers, archenemy? ")

print(f"{char_choice}'s {char_info} is: {value}")
