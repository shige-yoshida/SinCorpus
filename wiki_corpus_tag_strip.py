#!/usr/bin/env python3

f = open('sin_wikipedia_2011_100K-sentences_tagged.txt',mode='r')
for line in f:
    line = line.strip()
    with open('sin_wikipedia_2011_100K-sentences_tagged_strip.txt',mode='a') as f2:
        print(line, file= f2)
f.close
f2.close