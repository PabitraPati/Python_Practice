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

author :- Pabitra Kumar Pati

"""

def insertionSort(l_input, order='ascending'):
    '''
    Recieves the list of comma separated integers and
    retuns the sorted list in asked order.

    Inputs :-
    l_input :- comma separated elements (no space in between)
         e.g. :- 7,3,5,9,1
    order :- in which order you want the list to be sorted
         can either be 'descending' or 'ascending'
         If no order provided, by default, list will be sorted in ascending order.
    '''

    if order not in [ 'descending', 'ascending' ]:
        print("Invalid order provided. Please provide 'descending' or 'ascending' as order.")
        exit()
    mlist= [int(elem) for elem in l_input.split(',')]

    for i in range(1,len(mlist)):
        ptr = i-1               
        while mlist[ptr] > mlist[i] and ptr >= 0:
            mlist[ptr], mlist[i] =  mlist[i], mlist[ptr]
            ptr, i = ptr-1, i-1
            # Un-comment the below line to see how insertion sort works
            # print (mlist) 
    # Reverse the list if order is 'descending'
    if order =='descending':
        mlist.reverse()
    return mlist, order

try:
    input = raw_input
except NameError:
    pass

l_input = input("Enter your list :- ")

op,order = insertionSort(l_input)
print ("Your sorted list in {} order :- {}".format(order, op))

op,order = insertionSort(l_input, 'descending')
print ("Your sorted list in {} order :- {}".format(order, op))

