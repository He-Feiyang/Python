Msg_List = [
0x180,
0x551,
0x240,
0x58A,
0x2c8,
0x50D,
0x5B3,
0x260,
0x559,
0x5A9,
0x218,
0x421,
0x351,
0x35D,
0x5F7,
0x54C,
0x569,
0x354,
0x245,
0x284,
0x5E4,
0x02A,
0x625,
0x358,
0x60D,
0x385,
0x2B1,
0x4CB,
0x2B7,
0x4CC,
0x628,
0x629,
0x580,
0x160,
0x57A,
0x5E9,
0x2C9,
0x510,
0x1F9,
0x559,
0x60D,
0x572,
0x563,
0x35A,
0x351,
0x352,
0x5E9,
0x50D,
0x510,
0x17C,
0x50A,
0x551,
0x421,
0x245,
0x002,
0x625,
0x57A,
0x160,
0x240,
0x5C8,
0x5C9,
0x5CA,
0x5CB,
]

Msg_List = list(set(Msg_List)) #set(list)是将list转换为集合。 集合：一个包含不重复元素的无序序列。 list(set()) list是将集合转换为列表
Msg_List.sort() 

with open('output.txt','w+') as f:
      print('The number of METER messages is:%d' %len(Msg_List), file = f)
      for i in Msg_List:
            print('%#x'%i,file = f)

'''
cnt = 0
with open('output.txt', 'a+') as f:
	print('Msg list：', file=f)
	for i in Msg_List:
		if cnt == list_len-1:
			print('%x'%i,file=f)
		elif (cnt < list_len - 1) and Msg_List[cnt] != Msg_List[cnt+1]:
			print('%x'%i,file=f)
		cnt = cnt + 1
f.close()
'''
