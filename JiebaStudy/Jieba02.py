import jieba
from collections import Counter

#创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r').readlines()]
    return stopwords

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('D:\github\python\JiebaStudy\stopwords.txt')
    outstr =''
    for word in sentence_seged :
        if word not in stopwords :
            if word != '\t':
                outstr += word
                outstr += ' '
    return outstr


inputfile = open('3390.txt','r')
outputfile = open('textout.txt','w')
print("input value :",inputfile)
for line in inputfile:
    line_seg = seg_sentence(line)
    outputfile.write(line_seg)

outputfile.close()
inputfile.close()

with open('textout.txt','r') as fr:
    data = jieba.cut(fr.read())
    data = dict(Counter(data))
    print(data)
    fdata = sorted(data.items(), key=lambda x: x[1],reverse=True)
    print(fdata)
    with open('textout2.txt','w') as fw:
        for k,v in data.items():
            fw.write('%s, %d \n' % (k, v))
    with open('textout3.txt', 'w') as tw:
        for i in fdata:
            print("value: ", i[0], i[1])
            if i[0] == ' ':
                continue
            else:
                tw.write('%s, %d \n' % (i[0],i[1]))


