# Corpus Tagging 
## Purpose: Tagging Leipzig Wikipedia Corpus 
The purpose of this scripts is to tag each word in Wikipedia Corpus, which is available from https://wortschatz.uni-leipzig.de/en/download/sinhala#sin_wikipedia_2011
## Method: Using UCSC tagged corpus
For this purpose, this scripts utilize UCSC tagged corpus. In this corpus, all words are manually tagged by linguists.\n
1: This scripts list all the words in the UCSC corpus with their POS tags.\n
2: This scripts compare words in Wikipedia Corpus and words in the list.\n
3: If the word is same, then the word in Wikipedia Corpus will be replaced by the corresponding one in the list.\n
4. Elif the word in Wikipedia Corpus has no corresponding word in the list, then the word in Wikipedia Corpus will remain unmodified.\n
## Result: Moderately useful tagged corpus
The resulted tagged corpus are relatively useful one. Impressionally about 80% of the words are automatically tagged.
