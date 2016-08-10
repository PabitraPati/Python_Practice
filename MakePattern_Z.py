'''
Print a pattern of 'Z' using '*'  with the given number of lines

Works both for Python 2.7 and 3.4

author - Pabitra Kumar Pati
'''

def print_Z_pattern():
    '''
    Takes the number of lines to make 'Z' pattern with
    And prints the 'Z' pattern in '*'
    '''
    line_number = int(input("Enter number of lines for the Z pattern "))
    # Assign the line number to a temporary variable
    count = line_number

    while (count > 0):
        if count == line_number or count == 1:
            # For last line, print only stars
            print (line_number*'* ')
        else:
            # In other lines print star only the respective position
            # E.g :- if line number is 3 then it will print the * at 3rd position and so on...
            op = (count-1)*('  ')
            op += '*'
            print (op)
        count -= 1

print_Z_pattern()
