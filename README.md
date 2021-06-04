# Boolean-retrieval-inverted-index-model
### Part of 2021 summer project. A basic Boolean retrieval system using the inverted index method.
---
## Components
1. main.py <br />
Takes user unput and initiates searching process based on a Boolean query.
2. construct_invrt_matr.py <br />
Assigns doc IDs to files inside the directory named *files*, creates the inverted list.
3. retrieval_task.py <br />
Contains Boolean operators: *and*, *or*, *not*. Supports *main.py* in the searching process.
---
## Requirements
1. Python 3.x
2. nltk
---
## How to use
* Create a new directory and keep the above mentioned files inside the same.
* Create ```/files``` storing the documents to perform the retrieval task on.
* Run ```main.py``` from the main directory. Refer to the instructions.
---
## Fixes needed
* Porter stemmer
* Strict query syntax
* DocID vs file name directory database
