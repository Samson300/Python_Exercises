# Hotel check in, check out
hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}
print(hotel)
# Display a menu asking whether to check in or check out.
check_input = input("Do you want to check in or check out?: ")
# Prompt the user for a floor number, then a room number.
floor_num_input = input("What floor number?: ")
room_num_input = input("What room number?: ")
# If checking in, ask for the number of occupants and what their names are.
# Do not allow anyone to check into a room that is already occupied.
if check_input == "check in".lower(): 
    if room_num_input in hotel.get('3') or room_num_input in hotel.get('2') or room_num_input in hotel.get('1'):
        print("That room is already taken.")
    else:
        num_occupants = input("How many occupants?:")
        names = input("What are their names?").split()
        for i in names:
          # i = names
          hotel[floor_num_input][room_num_input] = names
# If checking out, remove the occupants from that room.
# Do not allow checking out of a room that isn't occupied
if check_input == "check out".lower(): 
    if room_num_input in hotel.get('1') or room_num_input in hotel.get('2') or room_num_input in hotel.get('3'):
      del hotel[floor_num_input][room_num_input]
      print("You are all checked out!")
    else:
      print('There is no one in that room')
    
print(hotel)