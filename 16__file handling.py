#16.Read a file and count number of lines, words, and characters.
file = open("sample.txt", "r")

lines = file.readlines()

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count = word_count + len(words)
    char_count = char_count + len(line)

file.close()

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)