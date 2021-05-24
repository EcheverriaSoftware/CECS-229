import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# function name: least_sq
# inputs: file_name- name of the csv file
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):
	N = 0
	x_sum = 0
	x_squared_sum = 0
	y_sum = 0
	xy_sum = 0
	df = pd.read_csv(file_name, sep = ',')
	for index, row in df.iterrows():
		N += 1
		x_sum += row['x']
		x_squared_sum += row['x'] * row['x']
		y_sum += row['y']
		xy_sum += row['x'] * row['y']
	m = ((N * xy_sum) - (x_sum * y_sum)) / ((N * x_squared_sum) - (x_sum * x_sum))
	b = (y_sum - m * x_sum) / N
	return round(m, 4), round(b, 4)

# function name: mat_least_sq
# inputs: file_name- name of the csv file
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):
	df = pd.read_csv(file_name, sep = ',')
	np_x = np.array(df['x'])
	X = np.column_stack((np_x, np.array(np.ones(len(df['x'])))))
	Y = np.array(df['y'])
	Tranpose_X = X.T
	X_Tranpose_X_Dot = np.dot(Tranpose_X, X)
	X_Tranpose_X_Dot_Inverse = np.linalg.inv(X_Tranpose_X_Dot)
	X_Tranpose_Y_Dot = np.dot(Tranpose_X, Y)
	result = np.dot(X_Tranpose_X_Dot_Inverse, X_Tranpose_Y_Dot)
	return round(result[0], 4), round(result[1], 4)

# function name: plot_reg
# inputs: mat - file_name- name of the csv file
		# using_matrix: True if you are plotting the linear equation from mat_least_Sq
		# 				False if you are plotting the linear equation from least_sq
# output: NA
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
	#	your graph should have the following: labeled x and y axes, title, legend
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
	if(using_matrix):
		df = pd.read_csv(file_name, sep=',')
		np_x = df['x'].to_numpy()
		np_y = df['y'].to_numpy()
		plt.plot(np_x, np_y, 'o', label="data points")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.title("Using Matrix Least Squares")
		slope, intercept = mat_least_sq(file_name)
		lineTitle = "y = " + str(slope) + "x + " + str(intercept)
		plt.plot(np_x, slope * np_x + intercept, label = lineTitle)
		plt.legend()
		plt.show()
	else:
		df = pd.read_csv(file_name, sep=',')
		np_x = df['x'].to_numpy()
		np_y = df['y'].to_numpy()
		plt.plot(np_x, np_y, 'o', label = "data points")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.title("Using Algebra Least Squares")
		slope, intercept = least_sq(file_name)
		lineTitle = "y = " + str(slope) + "x + " + str(intercept)
		plt.plot(np_x, slope * np_x + intercept, label = lineTitle)
		plt.legend()
		plt.show()

######## TEST CASES ########
#csv_file = "data.csv"

#m1, b1 = least_sq(csv_file)
#print("Slope using algebraic least squares:", m1)
#print("y-intercept using algebraic least squares:", b1)
#print()

#m2, b2 = mat_least_sq(csv_file)
#print("Slope using linear algebra least squares:", m2)
#print("y-intercept using linear algebra least squares:", b2)

#plot_reg(csv_file, True)

#plot_reg(csv_file, False)

