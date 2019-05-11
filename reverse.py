b = input("염기서열(A, T, C, G) 입력 : ")
c = ""
length = len(b) - 1
while length > -1:
	c += b[length]
	length -= 1
print(c)
