#
# assignment 5
#
# Kristofer Hughes
#I worked with Joseph Kovacevic. We worked on all the problems together.
#I had Eddie Dempsey's help using the code on Piazza to solve an issue with my code for the hourglass problem

#This function prints out a triangle made up of characters, and the triangle is moved over a number of spaces depending on the variable inputted
def printTriangle(n,t):
    '''n is the character used to make the triangle and t being the # of spaces the triangle is moved over'''
    if n == 0:
        return 0
    elif c==-1:
        return
    else:
        print (' ' * (t) + '*' * ( n * 2 - 1 ))
        return printTriangle( n - 2, t + 1 )
    

#Prints out an hourglass shape made out of two characters
def recSymPrint(p,b,n,s):
    ''' a = symbol 1, b = symbol 2, n = first row length, s = indentation '''
    if p == '' or b == '':
        return
    else:
        if n < 1:
            return
        else:
            print(s*' ' + n*p)
            recSymPrint(p,b,n-2,s+1)
            print(s*' ' + n*b)

            
    
#Counts number of floating point values in a nested list
def recStrCount(x,lst):
    '''x is the eventual total # of strings in the nested list, and lst is the nested list'''
    x = 0
    for i in lst:
        if type(i) == str:
            x += 1
        elif type(i) is list:
            x += recStrCount(i, lst)
    return(x)
    
#Merges two strings together into one string
def recStrMerge(str1,str2,answer=''):
    '''str1 is the first string to be merged, str2 is the second string to be merged, answer is the result of the merge'''
    if not str1:
        return answer+str2
    if not str2:
        return answer+str1
    return recStrMerge(str1[1:], str2[1:], answer+str1[0]+str2[0])

#Return sum of numbers in a nested list
def recListSum(recLst):
    '''recLst is the nested list with numbers'''
    total = 0  
    for i in recLst:
        if isinstance(i, list): 
            total += recListSum(i)
        else:
            total += i
    return total
    
