'''
http://effbot.org/librarybook/binascii.htm
http://www.programcreek.com/python/example/1814/binascii.a2b_base64
'''
import binascii

text = b'hello, mrs teal'

data = binascii.b2a_base64(text)
text = binascii.a2b_base64(data)
print (text, "<=>", repr(data))

data = binascii.b2a_uu(text)
text = binascii.a2b_uu(data)
print (text, "<=>", repr(data))

data = binascii.b2a_hqx(text)
text = binascii.a2b_hqx(data)[0]
print (text, "<=>", repr(data))

# 2.0 and newer
data = binascii.b2a_hex(text)
text = binascii.a2b_hex(data)
print (text, "<=>", repr(data))

## $ python binascii-example-1.py
## hello, mrs teal <=> 'aGVsbG8sIG1ycyB0ZWFs\012'
## hello, mrs teal <=> '/:&5L;&\\L(&UR<R!T96%L\012'
## hello, mrs teal <=> 'D\'9XE\'mX)\'ebFb"dC@&X'
## hello, mrs teal <=> '68656c6c6f2c206d7273207465616c'

#if __name__ == "__main__":