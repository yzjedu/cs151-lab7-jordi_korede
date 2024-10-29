# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

* Purpose: To get the dimensions of the room
* Name: get_dimensions
* Parameters: The room that the user is currently finding dimensions for
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
* Parameters: The room that the user is currently providing the flooring for
* Return: Type of flooring
* Algorithm:
  1. Ask user to input the type of flooring they want
  2. Convert input to lower
  3. While input doesn't equal hardwood, carpet, or tile
     1. Output error message and ask the user to input the flooring they want
  4. Return type of flooring


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


* Purpose: Runs the entire function
* Name: main
* Parameters: None
* Return: None
* Algorithm:
  1. Define variables
     1. add_room which equals 0
     2. final_cost which equals 0
     3. keep_count which equals 1
  2. While add_room is less than 0
     1. Output what room the user is on
     2. Create variable current_room which calls the function, room_cost with the following parameters
        1. get_dimensions using keep_count as its parameter