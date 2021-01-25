#Opens input file as read-mode and output file as write-mode in with wrapper
with open('inputFile.txt', 'r') as inStr, open('outputFile.txt', 'w') as outStr:
    sentence = inStr.read()        #Read string value from input file
    sentence = sentence.split()    #Separate words by whitespace into a list
    adjective = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    noun2 = input('Enter an noun: ')
    
    for index, word in enumerate(sentence):
        if word == 'ADJECTIVE':
            sentence[index] = adjective
        elif word == 'NOUN':
            sentence[index] = noun1
            noun1 = noun2
        elif word == 'VERB.':
            sentence[index] = verb + '.'
    
    sentence = ' '.join(sentence)   #Recombine words list into a string
    print(sentence)                 #Display result
    outStr.write(sentence)          #Write result to output file