#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_new(d, v):
    list1 = list()
    for k in d:
        if d[k] == v:
            list1.append(k)
        else:
            pass
    return list1


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
def histogram_new(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt', 'r') as fin:
        text = fin.read()
        text1 = "".join(c for c in text if c not in ('!','.',':'))
        pledge_list = list(text1.split())
        sorted(pledge_list)
    return pledge_list

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, 1)
    print reverse_lookup_new(pledge_histogram, 9)
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
