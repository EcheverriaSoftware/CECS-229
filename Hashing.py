# hash table
class hash_table:

	# constructor
	# inputs: size (defaults to 8 if no arguments are provided)
	def __init__(self, size = 8):
		# self.table: empty hash table of indicated size
		self.table = (None,) * size
		# self.size: number of positions in table
		self.size = size


	# Already completed function!
	# INSERTS value INTO HASHTABLE AT index
	# example: insert(5, 10) will place 5 into index#10
	def insert(self, value, index):
		temp = list(self.table)
		temp[index] = value
		self.table = tuple(temp)

	# function name: linear_probe
	# input: value- value to be inserted
			#start_index- where linear probing starts
	# output: returns the index of the hash_table that the value should be 
		#	inserted after linear probing
	# assumptions: value will always be an integer
		#	your table will always be big enough
	def linear_probe(self, value, start_index):
		if(self.size == start_index + 1):
			start_index = 0
		while(start_index < self.size):
			if(self.table[start_index] == None):
				return start_index
			else:
				start_index = start_index + 1
				if(start_index + 1 == self.size):
					start_index = 0

	# function name: insert
	# input: value- value to be inserted
	# output: Do not return anything. Just insert value into the proper position
		#	in self.table. Utilize linear_probe and insert in this function
	# assumptions: value will always be an integer
		#	your table will always be big enough
	def hash(self, value):
		# TODO
		# hint: empty spots in tuples are labeled as None
		if(self.table[value % self.size] == None):
			self.insert(value, value % self.size)
		else:
			probe_Index = self.linear_probe(value, value % self.size)
			self.insert(value, probe_Index)

	# Already completed function!
	def get_table(self):
		return self.table


	# Already completed function!
	def __str__(self):
		return str(self.table)




"""**********************************************************************"""
# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
"""**********************************************************************"""
