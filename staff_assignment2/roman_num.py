"""
Procedure:
1. Start with a result of zero
2. Loop through the string of roman numerals
3. if the first symbol is less than the next symbol's value, subtract the first symbol's 
value from the result.
4. otherwise add the first symbol's value to the result
5. After the loop, add the value of the very last symbol, as it wont have been compared 
to the next symbol
"""
# 1st, we get the roman numeral from the user
rom_num_string = input("Enter a roman numeral: ").upper()

# Create a dictionary to match each roman letter to its number
rom_to_int = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

# initialize result to store the final int value
res = 0

# Iterate through the input string rom_num_string using a for loop
for i in range(len(rom_num_string) - 1):
    first_value = rom_to_int[rom_num_string[i]]
    next_value = rom_to_int[rom_num_string[i+1]]
    
    # Check if the subtraction rule applies
    if first_value < next_value:
        res -= first_value
    else:
        res += first_value
        
# finally, add the value of the last character
last_value = rom_to_int[rom_num_string[-1]]
res += last_value

#print the result
print(f"The integer value is: {res}")