# insertion sort
A = [6,3,9,0]

for j in range(1, len(A)):
	chave = A[j]
	i = j-1

	while i>=0 and A[i] > chave:
		A[i+1] = A[i]
		i = i-1
	A[i+1] = chave

print(A)