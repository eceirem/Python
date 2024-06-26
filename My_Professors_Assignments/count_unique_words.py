text = "ece seni cok seviyor biliyor musun"

word_count = {}

for word in text:
    if word == " ":
        continue

    else:
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

for word, count in word_count.items():
    if count == 1:
        print(f"{word} is unique in this sentence.")