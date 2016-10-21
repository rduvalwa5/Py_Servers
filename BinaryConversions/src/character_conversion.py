'''
Created on Jun 16, 2016
Convert from binary to ascii
https://docs.python.org/3/library/binascii.html

https://docs.python.org/3/library/stdtypes.html#typebytes
http://www.gossamer-threads.com/lists/python/python/977040

@author: rduvalwa2
'''

import binascii

def convert_String_To_Bytes(st):
    binTxt = bytes(st,'utf-8')
    return binTxt
    
def convert_AsciiToBin(text):
    data = binascii.b2a_base64(text)
    return data

def convertBinToAscii(data):
    '''
    binascii.b2a_base64(data)
    Convert binary data to a line of ASCII characters in base64 coding. The return value is the converted line, 
    including a newline char. The newline is added because the original use case for this function was to feed it a series 
    of 57 byte input lines to get output lines that conform to the MIME-base64 standard. Otherwise the output 
    conforms to RFC 3548.
    b2a_base64(data).decode('ascii')
    '''
    print("In fuction")
#    s_data = binascii.b2a_base64(data).decode('ascii')
    s_data = binascii.a2b_base64(data).decode('ascii')
    return  s_data
    
#if __name__ == "__main__":
if __name__ == '__main__':
    print("Start")
    myString = 'abcde'
    myBinary = convert_String_To_Bytes(myString)
    print("Returned Bytes are ", myBinary)
    data = convert_AsciiToBin(myBinary)
    print("Returned data is ", data)
    txt = convertBinToAscii(data)
    print("Returned text is ", txt)
