# calculate Hamlet v1
def getText():
    txt = open('.\some_doc\hamlet.txt','r').read()
    txt = txt.lower()
    for ch in '''~!@#$%^&*()_+:"<>?`-=[];',./|''':
        txt = txt.replace(ch,' ')
    return txt

hamletTxt = getText()
words = hamletTxt.split() #convert to list
counts = {} #create a dictionary
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True) #选择第二个元素作为排序标准， reverse = True降序
for i in range(10):
    word, count = items[i]
    print(word, count)