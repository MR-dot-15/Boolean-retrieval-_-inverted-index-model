from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# tokenization and stemming of query
def process_query(phrase):
    query = word_tokenize(phrase)
    return query 

# finding the posting list
def find_posting(term, inverted_matrix):
    for key in inverted_matrix.keys():
        if key == term: #or key == term[:len(key)]
            return inverted_matrix[key][1:]
    return []

# defining the AND operation
def AND(posting1, posting2):
    len1, len2 = len(posting1), len(posting2)
    intersection = []
    i, j = 0, 0
    while i < len1 and j < len2:
        if posting1[i] == posting2[j]:
            intersection.append(posting1[i])
            i+=1
            j+=1
        elif posting1[i] < posting2[j]:
            i+=1
        elif posting1[i] > posting2[j]:
            j+=1
    return intersection


# defining the OR operation
##def OR(posting1, posting2):
##    len1, len2 = len(posting1), len(posting2)
##    union = []
##    i, j = 0, 0
##    while i < len1 or j < len2:
##        try:
##            if posting1[i] == posting2[j]:
##                union.append(posting1[i])
##                i+=1
##                j+=1
##            elif posting1[i] < posting2[j]:
##                union.append(posting1[i])
##                i+=1
##            elif posting1[i] > posting2[j]:
##                union.append(posting2[j])
##                j+=1
##        except:
##            if j < len2:
##                union.append(posting2[j])
##                j+=1
##            elif i < len1:
##                union.append(posting1[i])
##                i+=1
##    return union
def OR(posting1, posting2):
    return list(set(posting1 + posting2))

# defining the not-this_word function
def NOT(term, inverted_matrix):
    posting = find_posting(term, inverted_matrix)
    return [i for i in range(1,6) if i not in posting]
