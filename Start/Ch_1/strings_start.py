# Example file for Advanced Python: Language Features by Joe Marini
# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

# define some starting values
b = bytes([0x41, 0x42, 0x43, 0x44])

# decode the byte string
s2 = b.decode("utf-8")

s = "This is a string"
print(s+s2)

# encode strings to byte strings
b1 = s.encode('utf-8')
b2 = s2.encode('utf-8')

print(b1+b2)

# encode in UTF8
b3 = s.encode('utf-32')
b4 = s2.encode('utf-32')

print(b3+b4)
# TODO: Try combining them.

# TODO: Bytes and strings need to be properly encoded and decoded
# before you can work on them together

# TODO: encode the string as UTF-32
