# CPSC 351
# Assignment 2
# Myanna Harris

import re
import codecs
def q1():
    # find and print the bird species names
    #... open file, get text, close file ...
    file = codecs.open("pg25973.txt","r", "utf-8")
    text = file.read()
    file.close()
    #... find and print matches ...
    for m in re.finditer("_([A-Z]\w+|[A-Z]\.)\s\w+_", text):
        pString = ''.join((m.group(0)).split('_'))
        print(pString,"(",m.start(),",",m.end(),")")
    
def q2(string):
    # nd all lower-case words that contain two consecutive
    # vowels(a, e, i, o, or u), exactly 6 characters, and
    # end in either \ly" or \ing". 
    #... open file, get text, close file ...
    file = codecs.open(string,"r", "utf-8")
    text = file.read()
    file.close()
    #... find and print matches ...
    for m in re.finditer(r"(?=\b\w{6}\b)\b[a-z]*[aeiou]{2}[a-z]*(([l][y])|([i][n][g]))\b", text):
        print(m.group(0),"(",m.start(),",",m.end(),")")
    
def q3(string):
    # dentify street addresses involving numbered streets
    #... open file, get text, close file ...
    file = codecs.open(string,"r", "utf-8")
    text = file.read()
    file.close()
    #... find and print matches ...
    for m in re.finditer("\d+\s\w*(\.?)\s*\d+[A-Z][A-Z]\s\w+", text):
        print(m.group(0),"(",m.start(),",",m.end(),")")
    
def main():
    #... call q1 through q3 ...
    print("\"Birds of the Rockies\" by L. Sylvester Keyser\n")
    q1()
    print("\n")
    print("\"The Time Machine\" by H.G. Wells \n")
    q2("pg35.txt")
    print("\n")
    print("\"Armour's Monthly Cook Book\" edited by M.J. McClure\n")
    q3("pg26005.txt")
    
if __name__ == '__main__':
    main()
