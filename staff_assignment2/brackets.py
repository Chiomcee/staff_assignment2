"""
Given a string like "([])", which is made up of brackets:
() → parentheses
{} → curly braces
[] → square brackets
Task is to check:
Do all opening brackets have matching closing brackets?
Are they closed in the correct order?
If yes → return True
If not → return False

Example: "([])" is valid:   (matches) and [matches]
"([)]" is not valid: opened (, the [, but closed ) order is wrong

List is used to stimulate a stack in python: push opening brackets on the stack and pop and match them when closing brackets
"""
# Get input from users
bracket_string = input("Enter a string of brackets: ")

# A dictionary to map closing brackets to opening ones
bracket_map = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}

# initialize a list to act as a stack
L1 = []
is_valid = True  # Assume string is valid at start

# iterate through the input string using a for loop
for char in bracket_string:
    # if it's an opening bracket, append it to the list (push onto the stack)
    if char in bracket_map.values():
        L1.append(char)
    #if it's a closing bracket, check if the list is empty or the last element doesn't match
    elif char in bracket_map.keys():
        if not L1 or L1.pop() != bracket_map[char]:
            is_valid = False   # Exit the loop immediately if an invalid pattern is found
            break
if L1:
     # if the string is still valid after the loop
     # and if the list is empty (meaning all brackets were closed)
    is_valid = False

print("The input string is", is_valid)