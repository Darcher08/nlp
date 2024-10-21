import re
import os

""""
Extract all the words of the documents without repeated words and no punctuation symbols
"""

def wordExtractor(doc):
    bagW = []
    allWords = []
    rList = ['.', ',']

    with open(doc, 'r', encoding="utf'8") as dc:

        lines = dc.read().split() #* divides the full document in words
        pattern = re.compile(f"[{''.join(re.escape(r) for r in rList)}]")

        lines = [pattern.sub('', word) for word in lines]
        allWords = list(word.lower() for word in lines)
        bagW = list(set(word.lower() for word in lines))

    return bagW, allWords

"""
Open all the documents and save it in a bag. 
"""
def allDocs(directory):
    
    bagW = []
    allWords = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory,filename)
            bag, words = wordExtractor(filepath) 
            bagW.extend(bag)
            allWords.extend(words)
    return bagW, allWords

#*set the elements of the bag to keys of dictionary with 0 as value
def ocr(bagW):
    ocr = {word: 0 for word in bagW}
    return ocr

def updatedOcr(ocr, allWords):
    for word in allWords:
        if word in ocr:
            ocr[word] += 1
    return ocr

myBag, allWords = allDocs('documentos')
print(allWords)
ocr = ocr(myBag)
print(ocr)

updatedOcr(ocr, allWords)
print(ocr)
