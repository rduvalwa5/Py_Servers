'''
Created on Jun 17, 2016
https://docs.python.org/3/library/stdtypes.html#typebytes
4.8.1. Bytes
Bytes objects are immutable sequences of single bytes. Since many major binary protocols are based on the ASCII text encoding,
bytes objects offer several methods that are only valid when working with ASCII compatible data and are closely related to 
string objects in a variety of other ways.

@author: rduvalwa2
'''

def bytes_literals():
    s = 'my single string'
    b = b'my single string'
    print("as text ", s, "as bytes ", b)
    
    s = "double quote embed ' my string"
    b = b"double quote embed ' my string"
    print("as text ", s, "as bytes ", b)
    
    s = "my string"
    b = b'''my string'''
    print("as text ", s, "as bytes triple quoted ", b)

def create_zero_filled_byte_obj(number):
    return bytes(number)
 
def create_bytes_from_string(st, ):
    '''
    bytes([source[, encoding[, errors]]])
    Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256. 
    bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing 
    and slicing behavior.
    Accordingly, constructor arguments are interpreted as for bytearray().
    Bytes objects can also be created with literals, see String and Bytes literals.
    '''
 
def convert_binary_to_ascii(b): 
    return ascii(b)

def convert_String_To_Utf8_Bytes(st):
    binTxtUtf8 = bytes(st,'utf-8')    
    return binTxtUtf8

def convert_String_To_Ascii_Bytes(st):
    binTxtAscii = bytes(st,'ascii')
    return binTxtAscii

def bytes_replace_example(byte_str,replace_byte,by_byte):
    return  byte_str.replace(replace_byte,by_byte)


def bytes_range(n):
    return bytes(range(n))


if __name__ == '__main__':
    stg = 'abcde'
    bytes_literals()
    
    
    
    binBytes = convert_String_To_Ascii_Bytes(stg)
    asciiString = convert_binary_to_ascii(binBytes)
    print(asciiString)
    print("Text ", stg, "Binary utf8", convert_String_To_Utf8_Bytes(stg), "Binary ASCII", convert_String_To_Ascii_Bytes(stg))
    
    num = 5
    created_filled = create_zero_filled_byte_obj(num)
    adnum = 0
    for z in created_filled:
        adnum = adnum + 1
    print("total bytes are ", adnum)
    print("stg ",stg,type(stg))
    bytes(stg,'ascii')
    print(stg, type(stg))
    print('binBytes',binBytes,type(binBytes))
    print(binBytes.__len__())
    print(binBytes.capitalize())
#    binBytes = binBytes.replace(b'a', b'x')
    '''
    Note that you have save the replace back into the original variable.
    '''
    binBytes = bytes_replace_example(binBytes,b'a', b'X')
    print("variable binBytes now is :", binBytes)

    print(bytes_range(5),type(bytes_range(5)))
    for b in bytes_range(5):
        print(b)
        
    aB = bytes('abcde','ascii')
    for a in aB:
        print(a)
    
    
    
    