print()
def pizza(x):
  if x == 1:
    return 'supreme pizza'
  elif x == 2:
    return 'classic meat pizza'
  elif x == 3:
    return 'vegan pizza'
  elif x == 4:
    return 'salty sailor pizza'
  else:
    return 'stinky pete pizza'

def pasta(x):
  if x == 1:
    return 'carbonara'
  elif x == 2:
    return 'shrimp and pesto pasta'
  elif x == 3:
    return 'lasagna'
  elif x == 4:
    return 'chicken and liguini'
  else:
    return 'pasta salad'

def drinks(x):
  if x == 1:
    return 'mango smoothie'
  elif x == 2:
    return 'blueberry slushie'
  elif x == 3:
    return 'water'
  elif x == 4:
    return 'strawberry fresh'
  else:
    return 'pretty in pink'


def set(x):
  if x == 1:
    return 'Supreme pizza, pasta salad'
  elif x == 2:
    return 'salty sailor pizza, lasagna'
  else:
    return 'Classic meat pizza, carbonara'
  
def welcome():
  print("Welcome to Thiri's kitchen! Please choose a category from below! ><")
  print("1. Pizza")
  print("2. Pasta")
  print("3. Coffee")
  print("4. Combos (includes a toy blindbox)")
  menu = int(input("Enter the menu number(1-4): \n"))
  if menu == 1:
    print("1. supreme pizza\n2. classic meat pizza\n3. vegan pizza\n4. salty sailor pizza\n5. stinky pete pizza\n")
    x = int(input("Enter your pizza number(1-5): "))
    print(f"\nYou have ordered a {pizza(x)}! Thank youu.")
  elif menu == 2:
    print("1. carbonara\n2. shrimp and pesto paste\n3. lasagna\n4. chicken and linguini\n5. pasta salad\n")
    x = int(input("Enter your pasta number(1-5): "))
    print(f"\nYou have ordered {pasta(x)}! Thank youu.")
  elif menu == 3:
    print("1. mango smoothie\n2. blueberry slushie\n3. water\n4. strawberry fresh\n5. pretty in pink\n")
    x = int(input("Enter your drinks number(1-5): "))
    print(f"\nYou have ordered {drinks(x)}! Thank youu.")
  elif menu == 4:
    print("1. Supreme set: supreme pizza, pasta salad, and your choice of drink")
    print("2. Sailor set: salty sailor pizza, lasagna, and your choice of drink")
    print("3. Classic set: Classic meat pizza, carbonara, and your choice of drink\n")
    x = int(input("Enter your set number: "))
    print("1. mango smoothie\n2. blueberry slushie\n3. water\n4. strawberry fresh\n5. pretty in pink\n")
    x = int(input("Enter your drinks number(1-5): "))
    print(f"\nYou have ordered {set(x)} with {drinks(x)}! You get a blindbox containing one of these toys: kitty, bee, caterpiller, or bear.\n")
    input("Open the blindbox?\nPress enter..\n\n")
    import random
    toy = random.randint(1,4)
    if toy == 1:
      print(f"You got the kitty!")
    elif toy == 2:
      print(f"You got the bee!")
    elif toy == 3:
      print(f"You got the caterpiller!")
    else:
      print(f"You got the bear!")
    print("Thank you for your purchase. :)")
  else:
    print("invalid choice. Please choose again.")
    menu = int(input("Enter the menu number(1-4): "))
print()
welcome()

