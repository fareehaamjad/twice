'''
Created on Jan 28, 2014

@author: fa45
'''
import re

'''
A node structure to hold all the values in for easy retrieval
A node has: letter, upto 26 children nodes, word end indicator variable 
'''
class Node(object):
    def __init__(self, letter, end):
        # letter
        self.letter = letter
        if letter != '':
            ascii = ord(self.letter)
            #ascii of the letter
            self.ascii = ascii - 97
        #26 possible children
        self.children = [None]*26
        #boolean end that indicates the end of the word
        self.end = end

    def isEnd(self, end):
        self.end = end

'''
This function forms the tree
It takes in the root node, the word to insert and a 0 index as arguments
'''
def insert(node, word, index):
    if len(word) == index:
        return
    tempNode = Node(word[index], None)
    
    if (tempNode.ascii < 0 or tempNode.ascii >= 26):
        #print "skipped"
        return
    else:
        if (node.children[tempNode.ascii] == None):
            node.children[tempNode.ascii]= tempNode
            if len(word) == (index+1):
                tempNode.isEnd(True)
        elif (len(word) == (index+1)):
            node.children[tempNode.ascii].isEnd(True)
    insert(node.children[tempNode.ascii], word, index+1)
   
'''
This function forms the permutations of the word and stores the valid words in a list
It takes in the root node, an empty string, the word to insert and a list as arguments
'''    
def allWords(node, used, unused, list):
    if (node.end == True):
        list.append(used)
   
    for i in range(len(unused)):
        nextWord = unused[i]
        ascii = ord(nextWord)
        position = ascii - 97
        if (node.children[position] != None):
            newUsed = used+nextWord
            newUnused = unused.replace(nextWord, "", 1)
            allWords(node.children[position], newUsed, newUnused, list)
       
'''
This function reads the file containing all the words
It takes in the address of the file and a root node as arguments
'''            
def readFile(address, root):
    with open(address,'r') as f:
        for line in f:
            for word in line.split():
                insert(root, word, 0)
                
           



root = Node('', None)
readFile('words.txt', root);
arr = []
word = raw_input("The word list can be found here:\nhttp://www.curlewcommunications.co.uk/wordlist.html\n" 
                 +"This program only handles alphabets\n"+"Enter a word: ")

word = word.lower()

for char in word:
    ascii = ord(char)
    ascii = ascii - 97
    if (ascii < 0 or ascii >= 26):
        word = word.replace(char, "")


allWords(root, "", word, arr)
print list(set(arr))
