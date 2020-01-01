#Hedge unlock system 
import random

print ("Hedge it's starting...")
print ("Inserting lockpick into the keyhole...")

# We could use different approaches for this 
# like uploading a .txt file with a list of colors 
# or a true or false statement
# to difference green from red, but a simple list will do
# I'm going to populate it with different colors but red.
  
color_list = ['Red', 'Crimson Red', 'Cadmium Yellow', 'Green', 'Magenta', 'Blue', 'Purple', 'Periwinckle', 'Black', 'Titanium White']

number = 1
while number <= 100:
  
  light_color = random.choice(color_list)
  
  if light_color == "Green":
    print ("It's open: ", light_color, ". In position: ", number) 
    break
  else:
    print ("It's close: ", light_color)
    number += 1
