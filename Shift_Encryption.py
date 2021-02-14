# function name: shift_cipher_encode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the encoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_encode(string, n):
        string_Length = len(string)
        index = 0
        output = ""
        for num in range(string_Length):
                if(not(string[num].isalpha())):
                        output = output + string[num]
                elif(string[num].isupper()):
                        ascii_Value = ord(string[num])
                        ascii_Value = ascii_Value + n
                        if((ascii_Value) > 90):
                                ascii_Value = (ascii_Value % 90) + 64
                        output = output + chr(ascii_Value)
                else:
                        ascii_Value = ord(string[num])
                        ascii_Value = ascii_Value + n
                        if((ascii_Value) > 122):
                                ascii_Value = (ascii_Value % 122) + 96
                        output = output + chr(ascii_Value)
        return output

# function name: shift_cipher_decode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the decoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_decode(string, n):
        string_Length = len(string)
        index = 0
        output = ""
        for num in range(string_Length):
                if(not(string[num].isalpha())):
                        output = output + string[num]
                elif(string[num].isupper()):
                        ascii_Value = ord(string[num])
                        ascii_Value = ascii_Value - n
                        if((ascii_Value) < 65):
                                ascii_Value = (91 - (65 - ascii_Value))
                        output = output + chr(ascii_Value)
                else:
                        ascii_Value = ord(string[num])
                        ascii_Value = ascii_Value - n
                        if((ascii_Value) < 97):
                                ascii_Value = (123 - (97 - ascii_Value))
                        output = output + chr(ascii_Value)
        return output


# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
