#Kristofer Hughes
#I collaborated with Joseph Kovacevic. We worked together on both problems, and fixed errors in the code.

def depthCount(depLst, dep=0):
    if lst==[]:
        return 0
    elif type(lst)==lst:
        return 1+depthCount(lst[0])
    else:
        return depthCount(lst[1:])
    return (depthCount(lst[0]), depthCount(lst[1:]))
    
        
    
def recFloatCount(floatLst):
    if floatLst==[]:
        return 0
    elif type(floatLst[0])==float:
        return 1+recFloatCount(floatLst[1:])      
    elif type(floatLst[0])==list:
        return recFloatCount(floatLst[0])+recFloatCount(floatLst[1:])
    else:
        return recFloatCount([floatLst[1:]])
    
