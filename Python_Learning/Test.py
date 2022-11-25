#  Hamlet 词频统计 v1
# def getText():
#     txt = open('.\some_doc\hamlet.txt','r').read()
#     txt = txt.lower()
#     for ch in '''~!@#$%^&*()_+:"<>?`-=[];',./|''':
#         txt = txt.replace(ch,' ')
#     return txt

# hamletTxt = getText()
# words = hamletTxt.split() #convert to list
# counts = {} #create a dictionary
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# items = list(counts.items())
# items.sort(key = lambda x:x[1], reverse = True) #选择第二个元素作为排序标准， reverse = True降序
# for i in range(10):
#     word, count = items[i]
#     print(word, count)

# 《三国演义》词频统计 v1
# import jieba
# txt = open('./some_doc/threekingdoms.txt','r', encoding='utf-8').read()
# words = jieba.lcut(txt)
# counts = {} #创建一个字典
# for word in words:
#     if len(word) == 1:
#         continue
#     else:
#         counts[word] = counts.get(word, 0) + 1
# items = list(counts.items())
# items.sort(key = lambda x:x[1], reverse=True)
# for i in range(100):
#     word, count = items[i]
#     print('{:<10}{:>5}'.format(word, count))


# 《三国演义》人物出现次数统计
# import jieba
# txt = open('./some_doc/threekingdoms.txt', 'r', encoding='utf-8').read()
# excludes = {'将军', '却说', '二人', '不可', '荆州', '不能', '如此', '商议', '如何', '主公', '军士', '左右', '军马', '引兵', '次日', '大喜', '天下', '东吴', 
# '于是','今日','不敢','魏兵','陛下','一人','都督','人马','不知','汉中','只见','众将','后主'}
# words = jieba.lcut(txt)
# counts = {}
# for word in words:
#     if len(word) == 1:
#         continue
#     elif word == '诸葛亮' or word == '孔明' or word == '孔明曰':
#         rword = '孔明'
#     elif word == '关公' or word == '云长':
#         rword = '关羽'
#     elif word == '玄德' or word == '玄德曰':
#         rword ='刘备'
#     elif word == '孟德' or word == '丞相':
#         rword = '曹操'
#     else:
#         rword = word
#     counts[rword] = counts.get(rword, 0) + 1 #####
# for word in excludes:
#     del counts[word]
# items = list(counts.items())
# items.sort(key=lambda x:x[1], reverse=True)
# for i in range(20):
#     word, count = items[i]
#     print('{:<5}{:>5}'.format(word, count))

#字段key：value反转后输出
# s = input()
# try:
#     d = eval(s)
#     e = {}
#     for k in d:
#         e[d[k]] = k
#     print(e)
# except:
#     print('输入错误')

#输出词频最高的大于1个的字符
# import jieba
# txt = open('./some_doc/沉默的羔羊.txt','r', encoding ='utf-8').read()
# ls = jieba.lcut(txt)
# d = {}
# for word in ls:
#     if len(word) >= 2:
#         d[word] = d.get(word, 0) + 1
# maxc = 0
# maxw = ""
# for k in d:
#     if d[k] > maxc :
#         maxc = d[k]
#         maxw = k
#     elif d[k] == maxc and k > maxw:
#         maxw = k
# print(maxw)

s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''

# import jieba
# jieba.lcut(s)
# d = {}
# for word in s:
#     d[word] = d.get(word, 0) + 1
# d.pop(' ')
# max_value = 0
# max_key = ""
# for k in d:
#     if d[k] > max_value :
#         max_value = d[k]
#         max_key = k
# print(max_key)

# s = s.split()
# count = {}
# for word in s:
#     if len(word)==1:
#         continue
#     else:
#         count[word]=count.get(word,0)+1
# item=list(count.items())
# item.sort(key=lambda x:x[1],reverse = True)
# word,count=item[0]
# print(item[0])


# import turtle as t
# t.title('自动轨迹绘制')
# t.setup(800,800,0,0)
# t.pencolor('red')
# t.pensize(5)
# #读取数据
# datals = []
# f = open("./some_doc/data.txt")
# for line in f:
#     line = line.replace('\n','') #line此时就是一个字符串
#     datals.append(list(map(eval,line.split(','))))
# f.close()
# #自动绘制
# for i in range(len(datals)):
#     t.pencolor(datals[i][3],datals[i][5],datals[i][5])
#     t.fd(datals[i][0])
#     if datals[i][1]:
#         t.right(datals[i][2])
#     else:
#         t.left(datals[i][2])


#绘制词云英文
# import wordcloud
# txt = "life is short, you need python"
# w = wordcloud.WordCloud(background_color = 'white')
# w.generate(txt)
# w.to_file('test.png')

#绘制词云中文
# import jieba #中文分词库
# import wordcloud 
# txt = '程序设计语言是计算机能够理解和识别用户操作意图的一种\
# 交互体系，他按照特定规则组织计算机指令，使计算机能够自动进行\
# 各种运算处理'
# w = wordcloud.WordCloud( width = 1000, height = 700, \
#                          font_path = 'msyh.ttc') #msyh.ttc表示字体使用微软雅黑
# w.generate(' '.join(jieba.lcut(txt))) #jieba.lcut(txt)首先对中文进行分词，生成一个列表变量，' '.join()将列表中的每个元素之间加入空格
# w.to_file('test.png')

#绘制词云：政府工作报告
import jieba
import wordcloud
txt = open('./some_doc/新时代中国特色社会主义.txt', 'r').read()
w = wordcloud.WordCloud( width = 1000, height = 1000, \
                         font_path = 'msyh.ttc', background_color='white') #msyh.ttc表示字体使用微软雅黑
w.generate(' '.join(jieba.lcut(txt))) #jieba.lcut(txt)首先对中文进行分词，生成一个列表变量，' '.join()将列表中的每个元素之间加入空格
w.to_file('新时代中国特色社会主义.png')












