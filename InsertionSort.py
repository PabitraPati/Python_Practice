"""
Insertion Sort :-

The sorting is done with the help of a marker.
The left side of the marker is sorted where as right side is not.
If an element in the right of the marker is smaller than the element
immediate left of the marker, then swap them and continue until the
left element is smaller than the current element. Iterate over all the
elements to place them in their correct position.

Pseudocode :-
Procedure InsertionSort (List, First, Last)
    For CurrentPointer <- First + 1 To Last
        Pointer <- CurrentPointer - 1
        While List[Pointer] > List[CurrentPointer] AND Pointer >= 0
            SWAP (List[Pointer+1],  List[Pointer])
            Pointer <- Pointer - 1
            CurrentPointer <- CurrentPointer - 1
        EndWhile
    EndFor
EndProcedure

This code works for both Python 2.7 as well as Python 3.4.
To run this on Python 3.4, you need to uncomment line 42

author :- Pabitra Kumar Pati

"""

def insertionSort(mlist):
    for i in range(1,len(mlist)):
        ptr = i-1               
        while mlist[ptr] > mlist[i] and ptr >= 0:
            mlist[ptr], mlist[i] =  mlist[i], mlist[ptr]
            ptr, i = ptr-1, i-1
            # Un-comment the below line to see how insertion sort works
            # print (mlist) 
    return mlist

l_input = input("Enter your list :- ")
# Un-comment the below line for Python3
# l_input= [int(elem) for elem in l_input.split(',')]

op = insertionSort(list(l_input))
print ("Your sorted list :- %s" %(str(op)))

