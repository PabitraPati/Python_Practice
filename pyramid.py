import sys

class Pyramid:

    def make_pyramid(self, height):
        """
        Makes the pyramid of given height
        The pyramid starts from 1

        pyramid best shown with height 9
        """
        height = int(height)
        #row = column = 1
        for row in range(1, height+1, 1):
            i = 1
            j = row-1
            for column in range(1, (height-row)+1, 1):
                sys.stdout.write('   ')
            for column in range((height-row)+1, height+1, 1):
                #i = 1
                sys.stdout.write(str(i) + '  ')
                i+=1
            #j = i-2
            for column in range(height+1, height+row, 1):
                #j = row-1
                sys.stdout.write(str(j) + '  ')
                j-=1
            sys.stdout.write('\n')

    def make_full_pyramid(self, height):
        '''
        Makes the complete pyramid (both up and down)
        '''
        height = int(height)

        # call make_pyramid to make upper pyramid
        self.make_pyramid(height)
        # Now make the lower pyramid
        for row in range(height-1, 0, -1):
            i = 1
            j = row-1
            #print row
            for column in range(1, (height-row)+1, 1):
                #print column
                sys.stdout.write('   ')
            for column in range((height-row)+1, height+1, 1):
                #print column
                sys.stdout.write(str(i) + '  ')
                i+=1
            j = i-2
            for column in range(height+1, height+row, 1):
                #print column
                sys.stdout.write(str(j) + '  ')
                j-=1
            sys.stdout.write('\n')


ob = sorting()
height = raw_input("Enter height of pyramid")
ob.make_full_pyramid(height)
print "---------------------------------------"
ob.make_pyramid(height)
