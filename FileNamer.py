import os
import sys
import re
def main():
    folder= sys.argv[1] # new parent folder of the files
    newName=sys.argv[2] # new names of the files
    
    #files=os.listdir(folder)
    y=0
    for x in os.listdir(folder):
        y=y+1
        os.rename(folder+'\\'+x,folder+'\\-'+newName+str(y)+'.jpg')  
main()