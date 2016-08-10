'''
Given an integer N as input, return the cube of the N fibonacci numbers
'''

def cube_of_fibonacci():
    '''
    Takes an integer as input from user
    Returns the cube of the fibonacci series for the givevn integer
    
    Example:-
     if input integer is 5,
     fibonacci series will be - [0,1,1,2,3]
     so code has to eturn cube of the above fibonacci series i.e. [0,1,1,8,27]
    '''
    N = int(raw_input("Enter a number :- ").strip())
    fib = []
    for i in range(N):
        fib.append(i if (i==0 or i==1) else fib[i-1]+fib[i-2])
     
    cube = map((lambda x: x**3),fib)
    return cube
   
c = cube_of_fibonacci() 
print "The cube for fibonacci of given number is :- %s" %str(c)
