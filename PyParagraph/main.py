import re
fname =  "paragraph_3.txt"
with open(fname, 'r') as f:
    paragraph = f.read()
    word_count = len(re.split(' ', paragraph))
sentence_count = len(re.findall(r'\.', paragraph))
print("Paragraph Analysis")
print("-" * 25)
print("Approximate word count: " +str(word_count))
print("Approximate sentence count: " +str(sentence_count))
print("Average Letter Count:" +str((len(paragraph)+1)/word_count))
print("Average sentence length:" + str(word_count/sentence_count))