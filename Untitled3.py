#!/usr/bin/env python
# coding: utf-8

# In[52]:


import nltk
from nltk.tokenize import word_tokenize

stop_words = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re", "ve",
    "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn",
    "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn"
]

def count_stop_words(input_text):
    # Initialize a dictionary to store word frequencies
    word_count = {}

    stop_word_count = 0

    # Use regular expression to find words in the input text
    words = re.findall(r'\b\w+\b', input_text.lower())  # Convert to lowercase for case insensitivity

    # Count the frequency of each stop word
    for word in words:
        if word in stop_words:
            stop_word_count += 1

    return stop_word_count



# In[ ]:





# In[53]:


import re
f = open("paragraphs.txt", 'r')
content = f.read()


#print(content)


# In[ ]:


stop_word_count = count_stop_words(content)

print("Number of stop words :", stop_word_count)


# In[ ]:


new_content = re.sub(r'\b(?:{})\b'.format('|'.join(stop_words)), '',content, flags=re.IGNORECASE)


# In[ ]:


stop_word_count = count_stop_words(new_content)

print("Number of stop words :", stop_word_count)


# In[ ]:


frequency = {}
matches = re.findall(r'\b[a-z]{1,30}\b', new_content.lower())

for word in matches:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

for word, freq in frequency.items():
    print(word, freq)


# In[ ]:


with open("output.txt", "w") as file:
    file.write(new_content)


# In[ ]:




