from PreprocessingPipeline import tokenizeFromFolder
folderPath = "reuters21578/"

tokenList = tokenizeFromFolder(folderPath)
dict = {}

##simple SPIMI 
for tokenStream,docID in tokenList:
    for token in tokenStream:
        if token in dict:
            dict[token].add(docID)
        else:
            dict[token] = {docID}

#print output to file for checking if we are missing something
with open('PrimaryIndex.txt', 'w') as file:
    file.write("This is some text.\n")
    for token in dict:
        file.write("(" + str(token) + ", " + str(dict[token]) + " )" + "\n")
