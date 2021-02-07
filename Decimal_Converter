# funtion name: to_decimal
# input: num (a non-negative non-decimal int as string)- ex: 11101, 7712, ABC
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: decimal representation of num AS INTEGER 
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it to decimal for you. You should use
				# implement the algorithm discussed in class
# assumptions: num will always be non-negative
			#  num will always be a valid number ex: 31112 (base2) won't be an input
			#. if num has letters, they will always be captialized
			#  base will be 2, 8, or 16
def to_decimal(num, base):
        output = 0
        length = len(num)
        for i in range(length):
                if(num[i] == 'A'):
                        digit = 10
                elif(num[i] == 'B'):
                        digit = 11
                elif(num[i] == 'C'):
                        digit =12
                elif(num[i] == 'D'):
                        digit = 13
                elif(num[i] == 'E'):
                        digit == 14
                elif(num[i] == 'F'):
                        digit = 15
                else:
                        digit = int((num[i]))
                output = output +((digit * (base ** (length - (i + 1)))))
        return output

# funtion name: to_base
# input: dec_num (a positive decimal integer)- ex: 1, 6, 10, 68, 102...
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: non-base-10 representation of dec_num AS STR
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it for you. You should use
				# implement the algorithm discussed in class
# assumptions: dec_num will always be non-negative
			#  base will be 2, 8, or 16				
def to_base(dec_num, base):
        a = dec_num
        b = base
        r = 0
        output = ""
        if(base == 16):
                while(a >= 1):
                        if((a % b) == 10):
                                output = output + "A"
                                a = (int)(a / b)
                        elif((a % b) == 11):
                                output = output + "B"
                                a = (int)(a / b)
                        elif((a % b) == 12):
                                output = output + "C"
                                a = (int)(a / b)
                        elif((a % b) == 13):
                                output = output + "D"
                                a = (int)(a / b)
                        elif((a % b) == 14):
                                output = output + "E"
                                a = (int)(a / b)
                        elif((a % b) == 15):
                                output = output + "F"
                                a = (int)(a / b)
                        else:
                                r = (a % b)
                                a = (int)(a / b)
                                output = output + str(r)
                return output[::-1]
        else:
                while(a >= 1):
                        r =(a % b)
                        a = (int)(a / b)
                        output = output + str(r)
                return output[::-1]
