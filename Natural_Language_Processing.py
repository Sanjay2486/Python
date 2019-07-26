#Natural Language Processing : is manily used to process free text or content or any kind of document to understand the person's 
#thoughts and thinking. Basically analysing sentences and words of any person.

#before you start , please download nltk entire supporting packages. 
# install nltk package
# > pip install nltk
# cmd > nltk.download()
# this will pop-up a window with releated packages. Select all packages and click on download.

# Buzz words:
    #1. Tokenize : breaking of sentences into words or breaking of words into character
    #2. CORPORA  : collection of text or documents
    #3. LEXICON  : Its like a dictionary of words with its contextual meanning

import nltk
#importing tokenize which is of two type : sentence (breaking of sentence into words) and word (breaking of words into characters)
from nltk.tokenize import word_tokenize, sent_tokenize

#importing stop words using CORPUS module
from nltk.corpus import stopwords

#Importing stemming : it help to cummiulate words with same meaning into 1 word. like: if there two wrods eat and eating are there in your content
#then is model will help us making onw word which is : eat
from nltk.stem import PorterStemmer 

#Part of Speach tagging: its like tagging each and every word
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


#creating sample content
Sample_content = "Hi i am learning NLPL with Mr. Sanjay"                  

#now tokenize word 
Get_Words = word_tokenize(Sample_content)
#print(Get_Words)

#Tokenize sentence
Get_Sentence = sent_tokenize(Sample_content)
#print(Get_Sentence)

# STOPWORDS :  identifying/removing words which are not required for our analysis

#initialize variable with list of stopwords
Get_StopWords = set(stopwords.words("english"))

#Now, we check if any english stopwords are there in our Get_Words which is already tokenized.

#print tokenized words to comparision with stop word. i:e, to check if stopwords are removed are not
print(f"Atual Sentence: {Get_Words}")

#loop to run words in Get_Santence and print without stopwords
for word in Get_Words:
    if word not in Get_StopWords:
        print(word)

#**********stemming example******************
#sample content2
Sample_content2 = "He eat what he was eating yesterday at the eatery"

#Initialize stemming in new varibale
Get_PortStemming = PorterStemmer()

#Now stemm the words
for word in word_tokenize(Sample_content2):
    print(Get_PortStemming.stem(word))

#*******************Speach Tagging*************

# Sample Content3
Train_Sample = state_union.raw("2005-GWBush.txt")
Sample_content3 = state_union.raw("2006-GWBush.txt")

Custome_Sent_Tokenizer = PunktSentenceTokenizer(Sample_content3)

tokenized = Custome_Sent_Tokenizer.tokenize(Sample_content3)

def process_Content():
    try:
        for i in tokenized:
            Words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(Words)
            print(tagged)

            #Chunking of words
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>|<NN>?}"""

            ChunkParser = nltk.RegexpParser(chunkGram)
            Chunked = ChunkParser.parse(tagged)

            print(Chunked)

    except Exception as Err:
        print(str(Err))

process_Content()
