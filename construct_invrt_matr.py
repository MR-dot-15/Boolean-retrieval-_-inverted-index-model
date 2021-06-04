import pickle
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer as ps


# defining the punctuation list
# ord() and chr()
punc_marks = ['?', ',', '!', '.', '-', ':', ';', '/', chr(8216), chr(8217), chr(8220), chr(8221), '(', ')']

# constructing the docID matrix first
docids = dict()
_id = 1
with os.scandir("files/") as entries:
    for entry in entries:
        docids[_id] = entry.name
        _id+=1
        
def make_the_database():
    # the core inverted matrix, defined as a dictionary
    inverted_list = dict()

    for i in range(1,_id):
        path_new = 'files/' + docids[i]
        # opening and reading the txt file content
        with open(path_new, encoding="utf8") as f:
            temp_store = f.read()
        # tokenization
        temp_store = word_tokenize(temp_store)

        # removing stop words
        stop_words = list(stopwords.words("english"))
        filtered_store = [element for element in temp_store if element.casefold() not in stop_words]

        # removing punctuations
        filtered_store = [element for element in filtered_store if element not in punc_marks]
        
        # stemming (using Porter stemmer)
        stemmer = ps()
        stemmed_store = [stemmer.stem(element) for element in filtered_store]

        # creating the inverted matrix 
        for element in stemmed_store:
            if element not in list(inverted_list.keys()):
                inverted_list[element] = [1, i]
            else:
                inverted_list[element][0] += 1
                if inverted_list[element][-1] != i:
                    inverted_list[element].append(i)
        
        # the final dictionary is not sorted alphabetically 

    with open('inverted_matrix_dict', 'wb') as outfile:
        pickle.dump(inverted_list, outfile)