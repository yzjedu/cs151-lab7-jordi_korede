# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

* Purpose: To get the dimensions of the room
* Name: get_dimensions
* Parameters: None
* Return: Total area of the room
* Algorithm:
  1. Ask the user the width of the room
  2. While width is not a positive integer
     1. Output an error message and user the width of the room
  3. Ask the user the length of the room
  4. While length is not a positive integer
     1. Output an error message and user the length of the room
  5. Multiply length by width
  6. Return area

* Purpose: To get the type of flooring
* Name: get_flooring
* Parameters: None
* Return: Type of flooring
* Algorithm:
  1. Ask user to input the type of flooring they want
  2. Convert input to lower
  3. While input doesn't equal hardwood, carpet, or tile
     1. Output error message and ask the user to input the flooring they want\

* Purpose: Calculate of flooring for room
* Name: room_cost
* Parameters: Type of flooring and the total area of the room
* Return: Cost of room
* Algorithm:
  1. If type of flooring is hardwood
     1. Multiply area by 1.39
  2. Otherwise, if type of flooring is carpet
     1. Multiply area by 3.99
  3. Otherwise, if type of flooring is tile
     1. Multiply area by 4.99
  4. Print the cost of flooring for the room
  5. Return cost of flooring for room

* Purpose: Add all the rooms together
* Name: total_cost
* Parameters: All the cost of flooring for all the rooms
* Return: Total cost
* Algorithm:
  1. Add all the cost flooring for all rooms
  2. Print the total cost for all rooms