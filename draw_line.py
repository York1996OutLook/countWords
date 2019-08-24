from visdom import Visdom
vis=Visdom(env="123")
import time
import numpy as np
from collections import defaultdict
def readAllText(path)   :
    with open(path,"r") as f:
        text=f.read()
    return text
def draw_grows():
    txt = readAllText("./grows.txt")
    arr = txt.split("\n")
    numbers = list()
    for count in arr:
        count = int(count)
        time.sleep(500 / count)
        print(count)
        numbers.append(count)
        vis.line(numbers, X=[i for i in range(len(numbers))], win="1",
                 opts={'xlabel':'当前论文数量：%d，单词数量：%d'%(len(numbers),count)})
def draw_distribution():
    txt = readAllText("./allwords.txt")
    arr = txt.split("\n")
    # numbers = list()
    grid_dict=defaultdict(int)
    grid_size=200
    thresh1 = 2
    thresh2 = 3
    thresh3=100

    for line in arr:
        word_freq=line.split("~")
        # if len(word_freq)!=2 :
        word,freq=word_freq
        freq=int(freq)

        if freq<thresh1:
            grid_dict[1] += 1
        elif freq<thresh2:
            grid_dict[2]+=1
        elif freq < thresh3:
            grid_dict[3] += 1
        else:
            grid_dict[4]+=1

    values=list(grid_dict.values())
    # values.reverse()
    vis.pie(values,win="2", opts=dict(legend=["大于等于100次", '出现3到99次','出现两次','出现一次',]))

    # print(count)

        # vis.line(numbers, X=[i for i in range(len(numbers))], win="1",
        #          opts={'xlabel': '当前论文数量：%d，单词数量：%d' % (len(numbers), count)})


if __name__ == '__main__':
    draw_distribution()