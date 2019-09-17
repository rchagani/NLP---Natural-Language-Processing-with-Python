# Introduction to Python

sen = "I love Avengers\n"
print(sen)
print(sen*4)

# If statement

marks = 90

if marks > 90:
    print("Grade O")
elif marks > 80:
    print("Grade E")
elif marks > 70:
    print("Grade A")
elif marks > 60:
    print("Grade B")
else:
    print("Failed")
    
number1 = 45
number2 = 5

if (number1 % number2 == 0):
    print("Divisible")
else:
    print("Not Divisible")
    
    
# While loop
    
i = 1

while i<=10:
    print(i)
    i +=1    
    
# For loop
    
for i in range(1,11):
    print(i)
    
      
# Nested loop
    
for i in range(1,6):
    for j in range(1,6):
        print(j, end="")
    print()
    
# Two types of loops
    
# Break
    
for i in range(1,11):
    if i>5:
          break
    print(i)  
    
    
# Continue
for i in range(1,11):
    if i>=4 and i<=7:
          continue
    print(i)  
    
# Pass    
    
i = 1
if (i==1):
    pass
else:
    pass


# List (Non homogeneous collection of elements)[]

list1 = [12,12.8,"Hi", 1]

# Printing a list
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

list1.append(50)

print(list1)

list1.insert(0, 0)
print(list1)

list1.insert(1, "One")
print(list1)

# Updating the list

list1[1] = 20

# Deleting a  list elements
list1.pop() # last one will be deleted

del list1[3]  # Position 3 will be deleted

# Length of a list
print(len(list1))

for index in range(0,len(list1)):
        print(list1[index]) # will print the index



for index in range(0,len(list1)):
        list1[index] = 13 # replace all the index with 13


for item in list1:
    print(item) # will print the value. Same like index
    
    # Tuple()
# Same as list but immutable
# You can only view and print it
# You cannot change it. it's like read only. 
    
tuple1 = (12, "This is a string", 12.5, "one more string") # , will indicate that this is a tuple
tuple2 = (12, 90.2)

print(tuple1)
print(tuple1[1])

tuple3 = tuple1 + tuple2
    
print(len(tuple3))  
    
for i in range(0,len(tuple3)):
    print(tuple3[i])  
    
for item in tuple3:
    print(item)    
    
  
# Dictionary   - Key value pairs {}

dict1 = {}  

dict1["apple"] = "Apple is a fruit"
dict1["orange"] = "Orange is a fruit"
dict1["Mango"] = "Mango is the king of fruit"


print(dict1)
print(dict1['apple'])


print(dict1.get('apple'))
print(dict1.get('Python', "Does not exist"))

del dict1["apple"]

print(len(dict1))


listOfKeys = list(dict1.keys())
listOfValues = list(dict1.values())

for key in dict1.keys():
    print(dict1[key]) # will print values
    
    
for key in dict1.keys():
    print(key) # will print keys
    

for value in dict1.values():
    print(value) # will print values # print(dict1[value]) will give an error.




# Console I/O
    
inp = input("Enter a number:")
number1 = int(inp)

inp = input("Enter a number:")
number2 = int(inp)
print(number1+number2)


# How to create and write to a file.

inp = input("Write Something Stupid:") # As you want you want to do

with open("textFile.txt", "w") as f:
    f.write(inp) # "w" will write to a new file


with open("textFile.txt", "a") as f:
    f.write(inp) # "a" will append to a new file. it will remove old data and load new


with open("textFile.txt", "r") as f:
    print(f.read())# "r" will read what is there in the fikle


# writing your own function
# BLock of meaniful code

def functionName(arg1, arg2):
    print(arg1, arg2)

functionName('This number is',12)    
    

def sumOfNumbers(num1, num2):
    return(num1+num2)
    
print(sumOfNumbers(12,15))    


# Length function 

def length(l):
    count = 0
    for item in l:
        count += 1
    return count
    
print(length([12,13,16]))


# Classes and objects
class Fish:
    def swim(self):
        print("Fish is swimming")
    def run(self):
        print("Fish is running")

fish = Fish()
fish.swim()
fish.run()        

# Override Constructor
class Game:
    def __init__(self,name):
        self.name = name
    def start(self):    
        print(self.name,"has started")
    def stop(self):
        print(self.name,"has stopped")
         
game = Game("Counter Strike")
game.start()
game.stop()       
         

# Regular expression
# Importing library
import re

sentence = "I was born in 1998"
re.sub(r"\d","",sentence) # \d is number
re.match(r".*", sentence) # .* all characters in a sentence
re.match(r".+", sentence) # .+ almost same like *
re.match(r"[a-zA-Z]+", sentence) # any character from a to z and A to Z
re.match(r"I?", sentence) # look for I and anything after w?
# match function will only look for the first word. 

# Search function
re.search(r"was*", sentence) 

# Start function. ^ It will only check when your senetnce starts with 1998
if re.match(r"^1998", sentence):
    print("Match")
else:
    print("No Match")

# Ends function. Never use match function. use search. $ It will only check when your senetnce starts with 1998
if re.search(r"1998$", sentence):
    print("Match")
else:
    print("No Match")


# Replace your words from the sentence
    
sentence1 = "I love to play"

print(re.sub(r"play","PLAY",sentence1)) # Number will be replaced. first search, second replace and third is feature
print(re.sub(r"[a-z]","0",sentence1)) # Changes all small a to z to 0
print(re.sub(r"[a-z]","0",sentence1,flags=re.I)) # Changes all a to z to 0. flags=re.I will not consider small or capital letters
print(re.sub(r"[a-z]","0",sentence1,1,flags=re.I)) # first 3 patterns will only change
  
 # Shorthand 

sentence1 = " Welcome to the year 2018"
sentence2 = "Just wait %^%.,$^# watch for 2018"
sentence3 = "I       love      you" 
sentence4 = "I love Jack's class"
    
sentenceModified =  (re.sub(r"[%^\.#,$]","",sentence2))  
    
sentenceModified2 =  (re.sub(r"\w"," ",sentence2)) # \w contains a-z A-Z 0-9    
sentenceModified3 =  (re.sub(r"\W"," ",sentence2)) # \W Does not contains a-z A-Z 0-9     
sentenceModified4 =  (re.sub(r"\s+"," ",sentence3)) # \s+ will replace multiple space with one space      
    

sentenceModified5 =  (re.sub(r"[%^\.#,'$]"," ",sentence4))  
sentenceModified6 =  (re.sub(r"\s+[a-zA-Z]\s+"," ",sentenceModified5)) 

# Working with a list

X = ["I Love %food",
     " People are stu*pid",
     " I hate playing with #bat and     ball",
     " Remeber my name s are funny 2"]

# Lets use for statment to clean the data

for i in range(len(X)):
    X[i] = re.sub(r"\W"," ", X[i]) # \W will remove @#$%^&*() etc
    X[i] = re.sub(r"\d"," ", X[i]) # \d replace all numbers
    X[i] = re.sub(r"\s+[a-z]\s+"," ", X[i],flags=re.I) # \s+(space) a to z \s+(space) flags=re.I (small and capital)
    X[i] = re.sub(r"\s+"," ", X[i]) # Extra space with one space
    X[i] = re.sub(r"^\s","", X[i]) # Space in the start of the sentence
    X[i] = re.sub(r"\s$","", X[i]) # Space at the end of the sentence


## NLTK
import nltk

Paragraph = """Thank you all so very much. Thank you to the Academy, thank you to all of you in this room. I have to congratulate the other incredible nominees this year for their unbelievable performances. The Revenant was the product of the tireless efforts of an unbelievable cast and crew I got to work alongside. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your fierce talent on screen can only be surpassed by your friendship off screen. To Mr. Alejandro Innaritu, as the history of cinema unfolds, you have forged your way into history these past 2 years... thank you for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency…my entire team. I have to thank everyone from the very onset of my career…to Mr. Jones for casting me in my first film to Mr. Scorsese for teaching me so much about the cinematic art form. To my parents, none of this would be possible without you. And to my friends, I love you dearly, you know who you are.

And lastly I just want to say this: Making The Revenant was about man's relationship to the natural world. A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our children’s children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much.""" 

sentences = nltk.sent_tokenize(Paragraph)

works = nltk.word_tokenize(Paragraph)

#Stemming and Lemmatization

from nltk.stem import PorterStemmer

sentences = nltk.sent_tokenize(Paragraph)

stemmer = PorterStemmer()

#Stemming meaningless words can come up but it is faster than lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    newwords = [stemmer.stem(word) for word in words]
    sentences[i] = " ".join(newwords)


# Lemmatization gives meaning to your word
from nltk.stem import WordNetLemmatizer    
Paragraph = """Thank you all so very much. Thank you to the Academy, thank you to all of you in this room. I have to congratulate the other incredible nominees this year for their unbelievable performances. The Revenant was the product of the tireless efforts of an unbelievable cast and crew I got to work alongside. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your fierce talent on screen can only be surpassed by your friendship off screen. To Mr. Alejandro Innaritu, as the history of cinema unfolds, you have forged your way into history these past 2 years... thank you for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency…my entire team. I have to thank everyone from the very onset of my career…to Mr. Jones for casting me in my first film to Mr. Scorsese for teaching me so much about the cinematic art form. To my parents, none of this would be possible without you. And to my friends, I love you dearly, you know who you are.

And lastly I just want to say this: Making The Revenant was about man's relationship to the natural world. A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our children’s children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much.""" 

sentences = nltk.sent_tokenize(Paragraph)
lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    newwords = [lemmatizer.lemmatize(word) for word in words]
    sentences[i] = " ".join(newwords)



# Stop word removal using NLTK 
# Remove stopwords
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

sentences = nltk.sent_tokenize(Paragraph)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    newwords = [word for word in words if word not in stopwords.words("english")]
    sentences[i] = " ".join(newwords)

# Parts Of Speech Tagging
import nltk   

Paragraph = """Thank you all so very much. Thank you to the Academy, thank you to all of you in this room. I have to congratulate the other incredible nominees this year for their unbelievable performances. The Revenant was the product of the tireless efforts of an unbelievable cast and crew I got to work alongside. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your fierce talent on screen can only be surpassed by your friendship off screen. To Mr. Alejandro Innaritu, as the history of cinema unfolds, you have forged your way into history these past 2 years... thank you for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency…my entire team. I have to thank everyone from the very onset of my career…to Mr. Jones for casting me in my first film to Mr. Scorsese for teaching me so much about the cinematic art form. To my parents, none of this would be possible without you. And to my friends, I love you dearly, you know who you are.

And lastly I just want to say this: Making The Revenant was about man's relationship to the natural world. A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our children’s children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much.""" 

words = nltk.word_tokenize(Paragraph)

tagged_words = nltk.pos_tag(words)    

word_tags = []
for tw in tagged_words:
    word_tags.append(tw[0]+"_"+tw[1])

tagged_paragraph = " ".join(word_tags)

# Named Entity Recognition
import nltk

Paragraph = """The Taj Mahal was built by Emperor Shah Jahan"""

words = nltk.word_tokenize(Paragraph)

tagged_words = nltk.pos_tag(words)    

namedEnt = nltk.ne_chunk(tagged_words) # You will not be able to see this properly so we will use namedEnt.draw() to view it
namedEnt.draw()

# BOW Model
import nltk  
import re

Paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""

dataset = nltk.sent_tokenize(Paragraph)

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W',' ', dataset[i])
    dataset[i] = re.sub(r"\s+"," ", dataset[i])

# Bag of words model 

# Creating the histogram
    
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] =  1
        else:
            word2count[word] +=  1

# Selecting best 100 features        
import heapq
frequent_words = heapq.nlargest(100,word2count,key=word2count.get)

X = []
for data in dataset:
    vector = []
    for word in frequent_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    X.append(vector)
            
import numpy as np 
X = np.asarray(X)


#########
# Text Modelling using TF-IDF Model

# TF = Term Frequency
# IDF = Inverse Documment Frequency

# TF-IDF = TF * IDF
 
# TF-IDF

# BOW Model
import nltk  
import re

Paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""

dataset = nltk.sent_tokenize(Paragraph)

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W',' ', dataset[i])
    dataset[i] = re.sub(r"\s+"," ", dataset[i])

# Bag of words model 

# Creating the histogram
    
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] =  1
        else:
            word2count[word] +=  1

# Selecting best 100 features        
import heapq
frequent_words = heapq.nlargest(100,word2count,key=word2count.get)   
    
# IDF Matrix
import numpy as np 

word_idfs = {}
for word in frequent_words:
    doc_count = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count += 1
    word_idfs[word] = np.log((len(dataset) / doc_count)+1)
            
# TF Matrix

tf_matrix = {}
for word in frequent_words:
    doc_tf = []
    for data in dataset:
        frequency = 0
        for w in nltk.word_tokenize(data):
            if w == word:
               frequency += 1
        tf_word = frequency/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf
        
# TF-IDF Calculation
    
tfidf_matrix = []
for word in tf_matrix.keys():
    tfidf = []
    for value in tf_matrix[word]:
        score = value * word_idfs[word]
        tfidf.append(score)
    tfidf_matrix.append(tfidf)
    
# Transpose to two dimension array for model building
    
X = np.asarray(tfidf_matrix) # (100,21)

# need to transpose to (21,100)

X = np.transpose(X)

# Now to can do model building with this data.

# New model N-Gram Model
import random












    
    








     


    
    
    
    
    
    
    




















