"""""Calculate of words in text file
Author: T.Wasowicz"""

with open("makbet.txt") as f:
    data = f.read()
data.replace(",", " ").replace("|", "")
data = data.upper()

words_freq = {}
words = data.split()

for word in words:          #na rozmowie, jak czesto litera
    if word in words_freq:
        words_freq[word] +=1
    else:
        words_freq[word]=1

print(words_freq.values())

#czestosc = list(words_freq.values())
#czestosc.sort()
#print(czestosc[-10:])