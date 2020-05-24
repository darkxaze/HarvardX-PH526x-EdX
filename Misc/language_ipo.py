text = "This is my test text. We're keeping this text short to keep things manageable."

def count_words(text):
    text = text.lower()
    skips = [".", ",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = {}
    for word in text.split(" "):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        # unknown word
        else:
            word_counts[word] = 1
    return word_counts

from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = Counter(text.split(" "))
    return word_counts

print("COUNT_WORDS", count_words(text))
print("COUNT_WORDS_FAST", count_words_fast(text))
print("Results equal is ", count_words(text) == count_words_fast(text))
print("length", len(count_words("This comprehension check is to check for comprehension.")))
print("again check if results equal", count_words(text) is count_words_fast(text))

def read_book(title_path):
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text
text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt") 
print("Length  of Romeo and Juliet", len(text))  
ind = text.find("What's in a name?") 
print("index returned by find method", ind)
sample_text = text[ind : ind+1000]
print("sample text starting from whats in a name", sample_text)

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique,counts)

word_counts = count_words_fast(text)
(num_unique,counts) = word_stats(word_counts)
print("english", num_unique, sum(counts))

text = read_book("./Books/German/shakespeare/Romeo und Julia.txt")
word_counts = count_words_fast(text)
(num_unique,counts) = word_stats(word_counts)
print("german", num_unique, sum(counts))    

import os
book_dir = "./Books/"
print("book_dir", os.listdir(book_dir))

import pandas as pd
stats = pd.DataFrame(columns = ("language","author","title","length","unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            #print("inputfile", inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
            title_num += 1

#print(stats)
print(stats.head(), stats.tail())
print(stats.length, stats.unique)

''' Example of using pandas with age and name table'''
# import pandas as pd
# table = pd.DataFrame(columns = ("name","age"))
# table.loc[1] = "James", 22
# table.loc[2] = "Jess", 32
# print(table)
# print(table.columns)
######################################################

import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")

print(stats[stats.language == "English"])

plt.figure(figsize = (10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")