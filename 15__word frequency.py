# 15.Count frequency of each word in a text using dictionary.
text = "this is a test this is only a test"

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequencies:")
for word in freq:
    print(word, ":", freq[word]