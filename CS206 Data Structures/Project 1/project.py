def create_matrix(fname):
	matrixx1 = open(fname+'.txt').read()
	matrix1 = []
	for item in matrixx1.split('\n'):
		if item:
			matrix1.append(item.split())
	return matrix1

def create_identity_matrix(n):
	c = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		c[i][i] = 1
	return c

def checking_same_matrix(matrix1, matrix2):
	if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
		return False
	else:
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				if (matrix1[i][j] != matrix2[i][j]):
					return False
	return True


def addition_of_matrices(matrix1, matrix2):
	if (len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0])):
		return "Give me a matrices of same sizes!!"
		
	matrix3 = [[0. for i in range(len(matrix1))] for j in range(len(matrix1[0]))]
	for i in range(len(matrix1)):
		for j in range(len(matrix1[0])):
			matrix3[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])
	
	return matrix3

def multiple_of_matrices(matrix1, matrix2):
	if (len(matrix1[0]) != len(matrix2)):
		return "Not appropriate size"
		
	m = len(matrix1)
	n = len(matrix2)
	k = len(matrix2[0])
	c = [[0 for i in range(k)] for j in range(m)]
	for i in range(m):
		for j in range(k):
			for q in range(n):
				c[i][j] += int(matrix1[i][q]) * int(matrix2[q][j])
	return c


def symmetric_matrix(matrix):
	truth = True
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix1[i][j] == matrix1[j][i]:
				truth = True
			else:
				return False
	return truth

def identity_matrix(matrix):
	truth = True
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(i == j and int(matrix1[i][j]) == 1):
				truth = True
			elif (i != j and int(matrix1[i][j]) == 0):
				truth = True
			else:
				truth = False
	return truth

#print (identity_matrix(matrix2))
def transpose_matrix(matrix):
	matrix4 = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			matrix4[i][j] += int(matrix1[j][i])
	return matrix4

def power(matrix, n):
	if n == 1:
		return matrix
	if (n % 2) == 0:
		matrix1 = power(matrix,n // 2)
		return(multiple_of_matrices(matrix1, matrix1))
	else:
		matrix1 = power(matrix, n // 2)
		return multiple_of_matrices(multiple_of_matrices(matrix1, matrix1),matrix)


def main():
	add1 = create_matrix("add1")
	add2 = create_matrix("add2")
	multiple1 = create_matrix("multiple1")
	multiple2 = create_matrix("multiple2")
	inverse1 = create_matrix("inverse1")
	inverse2 = create_matrix("inverse2")
	powerx = create_matrix("power")

	print("Addition of matrices is", addition_of_matrices(add1, add2))
	print("Multiplication of matrices is", multiple_of_matrices(multiple1, multiple2))
	print("It is inverse because multiplication of matrices is Identity matrix", multiple_of_matrices(inverse1, inverse2))
	print("Power of A^10 is", power(powerx, 10))
	
	input("Enter any key to continue")
	
main()