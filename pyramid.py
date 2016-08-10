'''
Code to make pyramid

Works for both Python 2.7 and 3.4

author - Pabitra Kumar Pati
'''

import sys

class Pyramid:

    def make_pyramid(self, height):
        """
        Makes the pyramid of given height
        The pyramid starts from 1

        pyramid best shown with height 9
        """
        height = int(height)
        for row in range(1, height+1, 1):
            i = 1
            j = row-1
            for column in range(1, (height-row)+1, 1):
                sys.stdout.write('   ')
            for column in range((height-row)+1, height+1, 1):
                sys.stdout.write(str(i) + '  ')
                i+=1
            for column in range(height+1, height+row, 1):
                sys.stdout.write(str(j) + '  ')
                j-=1
            sys.stdout.write('\n')

    def make_full_pyramid(self, height):
        '''
        Makes the complete pyramid (both up and down)
        '''
        height = int(height)
        print ("Complete Pyramid :- ")

        # call make_pyramid to make upper pyramid
        self.make_pyramid(height)
        # Now make the lower pyramid
        for row in range(height-1, 0, -1):
            i = 1
            j = row-1
            for column in range(1, (height-row)+1, 1):
                sys.stdout.write('   ')
            for column in range((height-row)+1, height+1, 1):
                sys.stdout.write(str(i) + '  ')
                i+=1
            j = i-2
            for column in range(height+1, height+row, 1):
                sys.stdout.write(str(j) + '  ')
                j-=1
            sys.stdout.write('\n')


ob = Pyramid()
height = int(input("Enter height of pyramid :- "))
ob.make_full_pyramid(height)
print ("---------------------------------------")
ob.make_pyramid(height)
print('\n')
