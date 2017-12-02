'''
Created on May 27, 2013
@author: rduval
zipcheck.py: validation function for US zip codes
'''

def zip_errors(z):
    """
    Validate z as either NNNNN or NNNNN-NNNN.
    """
#    pass
    l = len(z)
    if l not in (5,10):
        return "Zip codes should be 5 or 10 chars long"
    if (not z[:5].isdigit() or
        len(z) == 10 and not z[6:].isdigit()):
        return "Zil code contains non-numberic characters"
    if l == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the two parts"
    return

