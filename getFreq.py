import nltk
from nltk.corpus import wordnet
import time
from collections import defaultdict
import os

from spellchecker import SpellChecker

# start=time.time()
# # nltk.download('wordnet')
# if  wordnet.synsets("acc"):
#     print(True)
# if  wordnet.synsets("flowef"):
#     print(True)
# print(time.time()-start)
# # nltk.download('punkt')
# with open("1.txt",encoding="utf-8") as f:
#     txt=f.read()
# words=nltk.word_tokenize(txt)
def isEnglishWord(_word):
    illegal_chars="1234567890:.+-"
    for c in illegal_chars:
        if c in _word:
            return False
    return True

if __name__ == '__main__':
    print("start")
    word_grow = list()
    main_path = "./out"
    files = os.listdir(main_path)
    word_dict = defaultdict(int)
    # lens=list()
    typo = SpellChecker()

    print_log=False

    for idx, file in enumerate(files):
        with open(os.path.join(main_path, file), "r", encoding="utf-8") as  f:
            txt = f.read()

        # txt = repalace(txt)

        arr = nltk.word_tokenize(txt)
        n = 0
        for word in arr:
            word = word.lower()
            # print(idx)
            # if word=="the":
            #     print(1)

            if len(word)==1:
                if print_log:print("%s is not a English word."%word)
                continue
            if word.isnumeric():
                if print_log:print("%s is not a English word."%word)
                continue

            if not isEnglishWord(word):
                if print_log: print("%s is not a English word." % word)
                continue

            if word in word_dict:
                word_dict[word] += 1
                if print_log:print("%s is a English word."%word)
                continue
            if len(typo.unknown([word]))!=1:#代表拼写正确
                word_dict[word] += 1
                if print_log:print("%s is a English word."%word)
            else:
                if print_log:print("%s is not a English word."%word)
        word_grow.append(len(word_dict))
        print(idx)
    grows=""
    for current_len in word_grow:
        grows+="%d\n"%current_len
    with open("./grows.txt","w") as f:
        f.write(grows.strip())

    all_words=""
    word_dict=sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    for key,value in word_dict:
        all_words+="%s~%d\n"%(key,value)
    with open("./allwords.txt","w") as f:
        f.write(all_words.strip())