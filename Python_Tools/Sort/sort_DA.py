
Msg_List = [
       0x02 
      ,0x284
      ,0x551
      ,0x60D
      ,0x567
      ,0x2B7
      ,0x354
      ,0x355
      ,0x35D
      ,0x4CC
      ,0x563
      ,0x57A
      ,0x5A5
      ,0x5C8
      ,0x5E5
      ,0x5E9
      ,0x5FE
      ,0x635
      ,0x390
      ,0x393
      ,0x1DB
      ,0x4CD
      ,0x4CE
      ,0x4CF
      ,0x55B
      ,0x5B3
      ,0x5BC
	  ]

Msg_List.sort()
i = 0
list_len = len(Msg_List)
print(len(Msg_List))
#for i in Msg_List:
	#print(i)
#print(Msg_List)
cnt = 0
with open('DA收发报文.txt', 'a+') as f:
	print('Msg list：', file=f)
	for i in Msg_List:
		if cnt == list_len-1:
			print('%#x'%i,file=f)
		elif (cnt < list_len - 1) and Msg_List[cnt] != Msg_List[cnt+1]:
			print('%#x'%i,file=f)
		cnt = cnt + 1
f.close()

