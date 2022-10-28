# 40 min outside of class
# 1 hr approx. for makeSentence()
# 10 minutes

import random

# def makeMarkovDict(filename):
#   m = {}
#   filename = filename.split()
#   for i in range(len(filename)-2):
#       temp = filename[i] + ' ' + filename[i+1]
#       if temp not in m:
#         m[temp] = [filename[i+2]]
#       else:
#         m[temp] += [filename[i+2]]
#   return m

def makeMarkovDict(filename):
    m = {}
    with open(filename, encoding="utf8") as s:
        text = s.read()
        words = text.strip().replace("--"," ").replace("---"," ").split();
        for i in range(len(words)-2):
            key = words[i]+" "+words[i+1]
            if not key in m:
                m[key] = []
            m[key].append(words[i+2])
    return m
# mine worked but I forgot to strip hyphens
# and forgot to write in the code reading the file
# since I had only tested it on a sentence prior and forgot to account for those scenarios in a larger .txt file

def makeSentence(m):
    autoNew = ''
    switch = 1
    for i in m:
        if switch == 1:
            auto = i + ' ' + random.choice(m[i])
            switch = 0
    auto = auto.split()
    while (auto[len(auto)-2] + ' ' + auto[len(auto)-1]) in m:
        temp = (auto[len(auto)-2] + ' ' + auto[len(auto)-1])
        auto += [random.choice(m[temp])]
    for i in auto:
        autoNew += i + ' '
    return autoNew

# https://www.gutenberg.org/ebooks/16

# 1. You need not grudge him. As his eyes were sparkling, and a boy did drop on the knuckles.
# 2. “Yes, my little man,” said Peter, who was the colour of milk; but the beginning of fairies.
# 3. That is all that sort of a bottle, and she flew back and formed a ring around them.

# PARAGRAPH (seperated into lines for viewing purposes)
# “The Wendy lady lives.” Then Peter tried slow and distinct. “What—are—you—quacking—about?” and so in still more offensive language.
# They ought to be confused with the look of pride upon his perilous quest. He laughed, but in a garden, and she distinctly heard his sigh of relief.
# “Peter,” she said, faltering, “are you a thimble.” “But why?” “Why, Tink?” Again Tink replied, “You silly ass!” cried Tinker.
# Smee reflected. “I can’t come,” she said to Wendy, because those rampagious boys of hers gave her complete ease of mind. To Michael the loneliness was dreadful.

print(makeMarkovDict('peter.txt'))
print(makeSentence(makeMarkovDict('peter.txt')))
