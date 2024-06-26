from collections import Counter
text = ("to be or not to be that is the question")
counter = Counter(text.split())
counter = dict(counter)
for word,count in counter.items():
    print(word,count,end="  ")