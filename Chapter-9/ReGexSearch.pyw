import os, re
from pathlib import Path

fileSearch = re.compile(r'.+\.txt')   #File name filter for *.txt files
userSearch = re.compile(input('Enter Regex: '))   #Prompt user Regex pattern
result = []    #Initialize result container for later use

# List all files in current directory using pathlib
basepath = Path(os.getcwd())    #Only process files in current directory
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())    #Throw subfolders
#files_in_basepath is a list of windowsPath object, need to convert to single string first
filteredFile = fileSearch.findall('\n'.join([item.name for item in files_in_basepath]), re.MULTILINE)

if len(filteredFile):    #Is *.txt files found?
    print('Found txt files:')
    print(filteredFile)
    print()
    for item in filteredFile:    #Process .txt files
        with open(item, 'r') as inFile:    #Open the file using with wrapper
            inFileSearch = '\n'.join(str.split(inFile.read()))    #Convert to single string
            inFileSearch = userSearch.findall(inFileSearch, re.MULTILINE)  #Commence Regex search
            if len(inFileSearch):    #Is pattern match found?
                result.append(inFileSearch)    #Save into result
else:
    print('No .txt file present in current folder')

print('Regex result for in-text file search:')
print(result)