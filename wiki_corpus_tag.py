#!/usr/bin/env python3
import re
import collections
import csv

#タグ付きコーパスに含まれる語形とタグをリストにする
f_tagged = open("./tagged_corpus.txt","r")
word =[]

for line in f_tagged:
    line = line.rstrip()
    if re.search("<",line):
        pass
    elif line == "":
        pass
    else:
        word.extend(line.split())
#setにして重複要素をなくす

word_2 = collections.Counter(word)
word_2 = word_2.most_common()
word_2 = [i[0] for i in word_2]

word_1 = set(word)
word_1 = list(word_1)

word_with_tag = []


for i in word_1:
    flag = False
    for j in word_2:
        if flag == False and j.startswith(i):
            flag = True
            word_with_tag.append(j)  

print(word_with_tag)
f_tagged.close

#WikipediaCorpusの語形をタグ付きにする
f_wiki = open('./sin_wikipedia_2011_100K-sentences.txt', 'r')

wiki_tagged = []
for l_wiki in f_wiki:
    l_wiki = l_wiki.rsplit()
    #print(l_wiki)
    #文の最後の語形を除いてfor文
    for w_wiki in l_wiki[1:-1]:
        flag = False
        w＿wiki_2 = w_wiki + '_'
        #wordのリスト内にあれば、タグ付きに置き換える
        for w_tagged in word_with_tag:
            if flag == False and w_tagged.startswith(w_wiki_2):
                flag = True
                ind = word_with_tag.index(w_tagged)
                #print(word_with_tag[ind])
                wiki_tagged.append(word_with_tag[ind])
            elif flag == False and re.search(r'^\d', w_wiki) != None:
                flag = True
                #print(w_wiki + '_QFNUM')
                wiki_tagged.append(w_wiki + '_QFNUM')
        #wordのリスト内になければそのまま        
        if flag == False:
            #print(w_wiki)
            wiki_tagged.append(w_wiki)
    #文の最後の語形について検索  
    w_wiki_last = l_wiki[-1].rstrip(".") + '_'
    flag = False
    for w_tagged in word_with_tag:
        if flag == False and w_tagged.startswith(w_wiki_last):
            flag = True
            ind = word_with_tag.index(w_tagged)
            #print(word_with_tag[ind] + "\n")
            wiki_tagged.append(word_with_tag[ind])
            wiki_tagged.append("\n")
    if flag == False:
        #print(l_wiki[-1] + '\n')
        wiki_tagged.append(l_wiki[-1])
        wiki_tagged.append("\n")
f_wiki.close

with open('sin_wikipedia_2011_100K-sentences_tagged.txt', 'w') as f_wiki_tagged:
    for word_tagged in wiki_tagged:
        f_wiki_tagged.write("%s " % word_tagged)

f_wiki_tagged.close 