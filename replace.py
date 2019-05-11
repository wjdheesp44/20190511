b = input("염기서열(A, T, C, G) 입력 : ")
c = ""
idx = len(b) - 1
i = 0
while idx >= i:
	if b[i] == 'A':
		c += 'T'
	elif b[i] == 'T':
		c += 'A'
	elif b[i] == 'C':
		c += 'G'
	else:
		c += 'C'
	i += 1
print(c)
