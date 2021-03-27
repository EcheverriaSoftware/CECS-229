import numpy as np
# function name: per_to_dec
# inputs: mat - n x n numpy array with percentages
# output: n x n numpy array where percentages are converted to decimal numbers
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def per_to_dec(mat):
    arr = np.ndarray(shape=(len(mat), len(mat[0])), dtype=float)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            arr[i][j] = (mat[i][j] * 0.01)
    return arr


# function name: sig_change
# inputs: oldmat - n x n numpy array (decimal form)
		# newmat - n x n numpy array (decimal form)
# output: True if there is at least one element in newmat that is at least 0.0001 away
			# from its respective counterpart in oldmat
		# False otherwise
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def sig_change(oldmat, newmat):
	for i in range(len(oldmat)):
		for j in range(len(oldmat[i])):
			if ((newmat[i][j] - oldmat[i][j]) > 0.0001):
				return True
	return False



# function name: prob_x
# inputs: mat - n x n numpy array with PERCENTAGES
		# x - number of iterations
# output: n x n numpy array that represents the probability matrix after x stages
		# Use per_to_dec here
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
			#  x>= 1
def prob_x(mat, x):
	probMat = per_to_dec(mat)
	for i in range(0, x):
		probMat = probMat.dot(per_to_dec(mat))
	return probMat


# function name: long_run_dist
# inputs: mat - n x n numpy array with PERCENTAGES
# output: n x n numpy array where percentages are converted to decimals
		# USE sig_change and per_to_dec
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def long_run_dist(probs):
	longRun_matrix = per_to_dec(probs)
	prev_matrix = longRun_matrix
	while(sig_change(prev_matrix, longRun_matrix)):
		temp = longRun_matrix.dot(longRun_matrix)
		prev_matrix = longRun_matrix
		longRun_matrix = temp
	return longRun_matrix







#**********************************************************************
# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
#**********************************************************************
