txt = input()
votes_dict = {}
def oylari_say(txt,votes_dict):
    for word in txt.split(','):
        if word in votes_dict:
            votes_dict[word] += 1
        else:
            votes_dict[word] = 1
    print(f"{'word':<12}count")
    for word, count in sorted(votes_dict.items()):
       print(f"{word:<12}{count}")
    return
oylari_say(txt,votes_dict)