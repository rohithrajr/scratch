import struct 

b = b'\xc0\x00\x02\x00\x19\x00\x00\x01\x00`\x01\x01\x00\x00\xff\xff' # this is the byte string you want to convert to an integer
print(struct.unpack('<H', b[-2:])[0])  # this unpacks the last two bytes of the byte string b and converts it to a 16 bit unsigned integer


""" a = 1234 # this is the integer you want to convert to a byte string
binary_string = struct.pack('<H', a) # convert the integer a to a 16 bit unsigned integer
binary_string = binary_string[::-1] # reverse the byte order 
#add a one byte header at end to the byte string to make it 3 bytes long
binary_string = binary_string + b'\x00'
print(binary_string) 
 """
 
a = 1234  # this is the integer you want to convert to a byte string
binary_string = struct.pack('<H', a)[::-1] + b'\x00' # convert the integer a to a 16 bit unsigned integer and reverse the byte order 
print(binary_string) 