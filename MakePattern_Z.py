# Print a pattern of 'Z' with the given number of lines

def print_Z_pattern(line_number):
    number = line_number
    # Assign the line number to a temporary variable
    count = number

    while count>0:
        if count == number or count == 1:
            # For last line, print only stars 
            print number*'*'
	    else:
	        # In other lines print star only the respective position
	        # E.g :- if line number is 3 then it will print the * at 3rd position and so on...
            op = (count-1)*(' ')
            op += '*'
            print op
	count -= 1
	

print_Z_pattern(int(raw_input("Enter number of lines for the Z pattern ")))
