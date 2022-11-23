
Msg_List = [0x174
      ,0x180
      ,0x218
      ,0x245
      ,0x280
      ,0x284
      ,0x351
      ,0x354
      ,0x355
      ,0x358
      ,0x385
      ,0x421
      ,0x502
      ,0x551
      ,0x580
      ,0x602
      ,0x625
      ,0x02A
      ,0x11A
      ,0x11B
      ,0x2B1
      ,0x2B7
      ,0x2C8
      ,0x2C9
      ,0x2DE
      ,0x35D
      ,0x4CB
      ,0x4CC
      ,0x4F8
      ,0x54C
      ,0x57A
      ,0x58A
      ,0x5C5
      ,0x5C8
      ,0x5E4
      ,0x5E9
      ,0x60D
      ,0x628
      ,0x629
      ,0x6E2
      ,0x160
      ,0x260
      ,0x510
      ,0x513
      ,0x50D
      ,0x559
      ,0x5A9
      ,0x5B3
      ,0x5E3
      ,0x5F7
	  ,0x240
	  ]

Msg_List.sort()
i = 0
list_len = len(Msg_List)
print(len(Msg_List))
#for i in Msg_List:
	#print(i)
#print(Msg_List)
cnt = 0
with open('仪表收发报文.txt', 'a+') as f:
	print('Msg list：', file=f)
	for i in Msg_List:
		if cnt == list_len-1:
			print('%#x'%i,file=f)
		elif (cnt < list_len - 1) and Msg_List[cnt] != Msg_List[cnt+1]:
			print('%#x'%i,file=f)
		cnt = cnt + 1
f.close()

