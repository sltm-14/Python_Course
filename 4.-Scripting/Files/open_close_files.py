#There's no need to use f.close

with open ('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split (' ')
word_count = len(words)
print(words)
print(word_count)
