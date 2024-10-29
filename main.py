# Programmers: Korede and Jordi
# Course:  CS151, Dr.Yalew
# Due Date: 10/31/2024
# Lab Assignment: 7
# Problem Statement: Your friend just bought a new house, but all the rooms have carpet or laminate that is horribly dirty and gross.
# They need your help to know how much it will cost to re-do all the floors!
# They want to put hardwood, carpet, or tile in each of the rooms of their house.
# They have all the dimensions of the rooms, which are conveniently all rectangles!
# Data In: The dimensions of each room (length and width), The type of flooring they desire (hardwood,carpet, or tile)
# Data Out: The cost of each room and the total cost for the house
# Credits: Class

# Gets the dimensions of the r
def get_dimensions(room_display):
    width = int(input("Enter the width of Room " + str(room_display) + ": "))
    while width < 0:
        width = int(input("Invalid width. Please try again with a positive number. "))
    length = int(input("Enter the length of Room " + str(room_display) + ": "))
    while length < 0:
        length = int(input("Invalid length. Please try again with a positive number. "))
    area = width * length
    return area

def get_flooring(room_display):
    flooring = str(input("What flooring will be used for Room " + str(room_display)  + "? (Please choose between hardwood, carpet, or tile flooring) "))
    flooring = flooring.lower()
    while flooring != "hardwood" and flooring != "carpet" and flooring != "tile":
        flooring = str(input("Invalid option. Please choose between hardwood, carpet, or tile flooring. "))
    return flooring

def room_cost(area, flooring):
    this_room = 0
    if flooring == "hardwood":
        this_room = area * 1.39
    elif flooring == "carpet":
        this_room = area * 3.99
    elif flooring == "tile":
        this_room = area * 4.99
    return this_room


def main():
    add_room = 0
    final_cost = 0
    keep_count = 1
    print("Hello! Welcome to our flooring price calculator!\n"
          "In this program, we'll be calculating the amount your flooring will cost!\n"
          "All you need to do is enter the dimensions of each room and the\n"
          "flooring for each one.\n"
          "Let's get started!")
    while add_room < 5:
        print("")
        print("Room " + str(keep_count))
        current_room = room_cost(get_dimensions(keep_count), get_flooring(keep_count))
        print("Room " + str(keep_count) + f" will cost ${current_room:.2f}")
        final_cost += current_room
        add_room += 1
        keep_count+=1
    print("")
    print("Alright, we've gotten all we need and we have your final cost!")
    print(f"The final cost for all the flooring you need is: ${final_cost:.2f}")
    print("")
    print("")
    print("Thank you for using our flooring price calculator! :)")
    print("")


main()