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

def get_dimensions():
    width=int(input("Enter width: "))
    while width < 0:
        print("Enter a positive number")
    length=int(input("Enter length: "))
    while length < 0:
        print("Enter a positive number")
    area = width*length
    return area
def get_flooring():
    flooring=int(input("Enter flooring: (hardwood,carpet,or tile) "))
    flooring = flooring.lower()
    while flooring != "hardwood" and flooring != "carpet" and flooring != "tile":
        print("Enter either hardwood,carpet, or tile ")
    return flooring
def room_cost(area, flooring):
    if flooring == "hardwood":
        room_cost = area * 1.39
    elif flooring == "carpet":
        room_cost = area * 3.99
    elif flooring == "tile":
        room_cost = area * 4.99
    return room_cost
def total_cost(cost1,cost2,cost3,cost4,cost5):
    total_cost = cost1 + cost2 + cost3 + cost4 + cost5
    print(total_cost)

def main():
    room1 = room_cost(get_dimensions(), get_flooring())









