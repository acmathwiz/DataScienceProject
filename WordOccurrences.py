# You are given a list of words. Some words may repeat. For each word, output the number of times it occurs.
#
# The order of output should correspond to the order of first appearance of each word in the input.

print("Please enter no. of words:")
no_of_words = int(input())
wordcount = {}
words = []

for i in range(no_of_words):
    word = input().strip()
    words.append(word)
    wordcount[word] = wordcount.get(word, 0) + 1
distinct_words = list(dict.fromkeys(words))
print(len(distinct_words))
print(distinct_words)
print(" ".join(str(wordcount[w]) for w in distinct_words))
print(wordcount)






