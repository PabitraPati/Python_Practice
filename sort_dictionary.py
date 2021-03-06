'''
This file shows the ways to sort a dictionary on the basis of key or value.

This runs both on Python 2.7 and Python 3.4

Author - Pabitra Kumar Pati
'''

def sort_dict_by_keys(mydict):
    '''
    Sort a given dictionary by the key
    and returns the key value pairs in a list
    '''
    res = [] 
    for i in sorted(mydict):
        res.append(tuple([i,mydict[i]]))
    return res


def sort_dict_by_values(mydict):
    '''
    Sort a given dictionary by the values
    and returns the key value pairs in a list

    Techniques to sort by values :-
     1. for i in sorted(mydict, key=mydict.get):
        ... print(i, mydict[i])

     2. for i in sorted(mydict, key=lambda x: mydict[x]):
        ... print(i, mydict[i])

     3. [sorted([(value, key) for (key,value) in mydict.items()])
        This will return the value and key pair, not key value pair

     4. for v in sorted(mydict.values()):
        ... print(mydict.keys()[mydict.values().index(v)], v)
      
    NOTE :- If multiple keys in the dictionary have same values, then those keys will be sorted as well if used method 3.
            Method 1 & 2 will sort the dictinary, but the keys with same values won't be sorted.
            Method 4 will not work if multiple keys have same values

    '''
    res = [] 
    for i in sorted(mydict, key=mydict.get):
        res.append(tuple([i, mydict[i]]))
    return res



mydict = {'carl':29, 'alan':56, 'bob':96, 'danny':78}

print("\n Sorting by keys :- {}".format(sort_dict_by_keys(mydict)))
print("\n Sorting by vaules:- {}".format(sort_dict_by_values(mydict)))
