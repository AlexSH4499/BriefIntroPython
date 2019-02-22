import unittest

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING encoded
#

def divide_string(string,size):
    divided = []
    curr =''
    i = 0
    for char in string:
        # print(i)
        if i == 0 and size==1:
            # print(i)
            divided.append(curr)
            curr = ''
        if i%size == 0 and i > 0:#fails if size = 1 due to ignoring i
            # print(i)
            divided.append(curr)
            curr = ''
        curr+=char
        i+=1
    if i % size == 0:
        divided.append(curr)
    # print(divided)
    return divided

def huffman_dict(codes):
    di={}
    size_chars= 0
    for c in codes:
        ch,co = c.split("\t")
        ch.strip()
        co.strip()
        if co not in di:
            if ch == '[newline]':
                di[co] = '\n'
            else:
                di[co] = ch
                size_chars=len(co)
    return di,size_chars

def decode(codes, encoded):
    decoder,size_chars = huffman_dict(codes)

    #now we split the encoded string into smaller ones
    result = ''
    for st in divide_string(encoded,size_chars):
        result += decoder[st]

    return result

class TestDivider(unittest.TestCase):

    def test_div(self):
        import string
        str = string.ascii_lowercase[0:24]
        print(str)
        size = 3
        self.assertEqual(divide_string(str, size), ['abc','def','ghi',
                                                    'jkl','mno','pqr',
                                                    'stu','vwx'])
        size=1
        self.assertEqual(divide_string(str, size), list(str))
if __name__ =='__main__':
    unittest.main()
