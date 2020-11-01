#!/usr/bin/env python3

f = open('sin_wikipedia_2011_100K-sentences_tagged.txt',mode='r')
counter = 0 
for line in f:
    counter += 1 
    line = line.strip()
    print(str(counter) + "\t" + line)
    with open('sin_wikipedia_2011_100K-sentences_tagged_numbered.txt',mode='a') as f2:
        print(str(counter) + "\t" + line, file= f2)
f.close