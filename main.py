import pickle
from nltk.stem import PorterStemmer as ps
stemmer = ps()
import construct_invrt_matr as con_inv
from retrieval_task import *

def show_instructions():
    print("-> supported operations: AND, OR, NOT\n")
    print("-> with one operation the style should be: t1 operator t2 operator ...")
    print("e.g. fire AND ice AND NOT wind")
    print("-> for AND-OR search, the recommended search style:\n (t1 OR t2 OR ...) AND t3 AND t4 ...")
    print("(t1 AND t2 AND ...) OR t3 OR t4 ...")
    print("[where ti is either a word or a NOT word]")
    print("e.g. (NOT heaven AND hell) OR earth; (heaven or earth) AND NOT hell\n")
    print("-> kindly keep all the py and txt files (to work on) in the same dict\n")

def database_build():
    try:
        with open('inverted_matrix_dict', 'rb') as infile:
            inverted_matrix = pickle.load(infile)
    except:
        print("no database available, one constructed")
        con_inv.make_the_database()
        with open('inverted_matrix_dict', 'rb') as infile:
            inverted_matrix = pickle.load(infile)
    return inverted_matrix

def wordbag_operation(wordbag, database):
    posting, i = [], 0
    if 'AND' not in wordbag and 'OR' not in wordbag:
        if wordbag[0] == 'NOT':
            return NOT(stemmer.stem(wordbag[1]), database)
        else:
            return find_posting(stemmer.stem(wordbag[0]), database)
    else:
        if 'OR' in wordbag:
            val = 0
        elif 'AND' in wordbag:
            val = 1
        while i < len(wordbag):
            if wordbag[i] == 'NOT':
                posting_n = NOT(stemmer.stem(wordbag[i+1]), database)
                i+=3
            else:
                posting_n = find_posting(stemmer.stem(wordbag[i]), database)
                if i == 0:
                    posting = OR(posting, posting_n)
                i+=2
            if val == 0:
                posting = OR(posting, posting_n)
            elif val == 1:
                posting = AND(posting, posting_n)
        return posting

def show_database():
    database = database_build()
    print(database)

def init_search():
    database = database_build()
    query = input()
    query= process_query(query)
    if '(' in query:
        index_close = query.index(')')
        chunk = query[1:index_close]
        words = query[index_close+2:]
        posting_chunk = wordbag_operation(chunk, database)
        posting_words = wordbag_operation(words, database)
        if query[index_close+1] == 'OR':
            return OR(posting_chunk, posting_words)
        elif query[index_close+1] == 'AND':
            return AND(posting_chunk, posting_words)
    else:
        return wordbag_operation(query, database)


while True:
    print(" 1. search\n 2. instructions\n 3. print the database\n 4. exit")
    inp = int(input())
    if inp == 1:
        result = init_search()
        for i in result:
            print(con_inv.docids[i], end = '\n')
    elif inp == 2:
        show_instructions()
    elif inp == 3:
        show_database()
    elif inp == 4:
        exit()