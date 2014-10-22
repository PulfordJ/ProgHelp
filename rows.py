"""
rows1.py
program to display rows of characters
created by sands 23/10/10
"""
def printRow(c, length) :
    """
    print a row of identical characters
    arguments:
    c: string: character to be used
    length: int: length of row
    """
    line = c * length
    print(line)
    

printRow('=', 10)
printRow('*', 7)
myChar = input ("Type in the character you wish to print :")
myLen = int(input ("Type in the number of characters "))
stop = myLen
while myLen>0 :
    myLen = myLen - 1
    printRow(myChar[0], myLen+1)
while myLen<stop :
    myLen = myLen + 1
    printRow(myChar[0], myLen )
