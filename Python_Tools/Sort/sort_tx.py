
Msg_List = [
       0x280 
      ,0x2de
      ,0x355
      ,0x4f8
      ,0x5c5
      ,0x5e3
      ,0x602
      ,0x567
      ,0x5a5
      ,0x5e5
      ,0x5fe
      ,0x635
	  ]

Msg_List.sort()
i = 0
list_len = len(Msg_List)
print(len(Msg_List))
#for i in Msg_List:
	#print(i)
#print(Msg_List)
cnt = 0
with open('发送报文.txt', 'a+') as f:
	print('Msg list：', file=f)
	for i in Msg_List:
		if cnt == list_len-1:
			print('%#x'%i,file=f)
		elif (cnt < list_len - 1) and Msg_List[cnt] != Msg_List[cnt+1]:
			print('%#x'%i,file=f)
		cnt = cnt + 1
f.close()

