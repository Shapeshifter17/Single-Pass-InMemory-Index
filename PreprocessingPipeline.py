from bs4 import BeautifulSoup
from nltk import word_tokenize
import os

def tokenizeFromFolder(folderPath):
    tokenList = []

    #loop through the reuters files on my computer
    for fileName in os.listdir(folderPath):
        if fileName.endswith(".sgm"):
            filePath = os.path.join(folderPath, fileName)
            with open(filePath, "rb") as file:
                html_doc = file.read()

            soup = BeautifulSoup(html_doc, 'html.parser')
            articleList = soup.find_all('reuters')
            for items in articleList:
                ## this will be our doc ID
                currentID = items.get('newid')

                #inside our text tag we look for Title and Body as per the requirements
                currentText = items.find('text')
                currentTitle = currentText.find('title').get_text() if currentText.find('title') else None
                currentBody = currentText.find('body').get_text() if currentText.find('body') else None        

                #title or body could be empty, we handle it here 
                if currentTitle:
                    titleList = word_tokenize(currentTitle)
                    tokenList.append((titleList, currentID))

                if currentBody:
                    bodyList = word_tokenize(currentBody)
                    tokenList.append((bodyList, currentID))

    return tokenList    