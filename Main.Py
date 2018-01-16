def isIn(char, aStr):
    '''
    author: Joe Begley
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return aStr[0] == char
    else:
        length = len(aStr)
        middle = int(length / 2)
        if aStr[middle] == char:
            return True
        elif char > aStr[middle]:
            return isIn(char, aStr[middle + 1:])
        else:
            return isIn(char, aStr[:middle])
char = input('Give Me The Charachter You Want To Find:  ')
aStr = input('Give Me The String You Want To Find It In:  ')
isIn(char, aStr)