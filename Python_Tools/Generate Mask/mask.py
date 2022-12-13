def get_mask(id):
	m = 0; sum = 0
	for i in id:
		m = m + 1
		for j in id[m:]:
			sum |= i ^ j
	return hex(~sum & 0xffffffff)

id = [0x218, 0x240, 0x245
]
for i in range(len(id)):
	print("%#x"%id[i], end = ',')
print(get_mask(id))