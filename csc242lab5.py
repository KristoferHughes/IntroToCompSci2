# Lab 6
#
# Kristofer Hughes
# I colloborated with Joseph Kovacevic. We discussed to how to fix eachothers errors.

def sublstCount(l):
    count = 0
    for e in l:
        if isinstance(e, list):
            count = count + 1 + sublstCount(e)
    return count

    

def itemCount(l):
    if type(l) == list:
        return sum(itemCount(subitem) for subitem in l)
    else:
        return 1
    
