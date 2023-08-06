import re
import time
import numpy as np
from PIL import Image
import math
def calculate_compression_ratio(original_size, compressed_size):
   
    compression_ratio = original_size / compressed_size
    return compression_ratio

def longest_common_substring(s1, s2):

    maxLongest = 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break
        for j in range(0, len(s2)):
            if (i+j < len(s1)):
                if s1[i+j] == s2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset


def encode_lzw(text):

    dictionary = dict()

    i = 0
    index = 1
    while i < len(text):
        if text[i] in dictionary:
            i = i + 1
        else:
            dictionary[text[i]] = index
            index = index + 1


    i = 0
    encoded = []
    while i < len(text):
        j = 0
        stringToBeSaved = text[i]

        while stringToBeSaved in dictionary and i+j < len(text):
            indexInDictionary = dictionary[stringToBeSaved]
            length = len(stringToBeSaved)
            if (i+j == len(text) - 1):
                break
            j = j + 1
            stringToBeSaved = stringToBeSaved + text[i+j]
        i = i + length
        encoded.append(indexInDictionary)
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
        index = index + 1

    return encoded, dictionary

l = []
def decode_lzw(encoded, dictionary):
    i = 0
    while i < len(encoded):
        l.append (list(dictionary.keys())[list(dictionary.values()).index(encoded[i])])
        i = i+1

print("LZW Image Compression Algorithm")
print("=================================================================")
h = int(input("Enter 1 if you want to input an colour image file, 2 for default gray scale case:"))
if h == 1:
    file = input("Enter the filename:")
    my_string = np.asarray(Image.open(file),np.uint8)
    sudhi = my_string
    shape = my_string.shape
    print ("Enetered string is:",my_string)
    stringToEncode = str(my_string.tolist())
elif h == 2:
    array = np.arange(0, 737280, 1, np.uint8)
    my_string = np.reshape(array, (1024, 720))
    print ("Enetered string is:",my_string)
    sudhi = my_string
    stringToEncode = str(my_string.tolist())
else:
    print("You entered invalid input")

print ("Enetered string is:",stringToEncode)
start_time = time.time()
[encoded, dictionary] = encode_lzw(stringToEncode)
end_time = time.time()
execution_time_lzw = end_time - start_time
print("Compression time:",execution_time_lzw)
a = [encoded, dictionary]
print("Compressed file generated as compressed.txt")
output = open("compressed.txt","w+")
output.write(str(a))
print("Encoded string: ", end="")
start_time = time.time()
decode_lzw(encoded, dictionary)
end_time = time.time()
execution_time_lzw = end_time - start_time
print("Decoded string:", "".join(l))
uncompressed_string = "".join(l)

if h == 1:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, shape)
    print(res)
    print("Observe the shapes and input and output arrays are matching or not")
    print("Input image dimensions:",shape)
    print("Output image dimensions:",res.shape)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    if sudhi.all() == res.all():
        print("Success")
if h == 2:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    print(res)
    res = np.array(res)
    res = np.reshape(res, (1024, 720))
    print(res)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    print("Success")
print("Decompression time:",execution_time_lzw)
original_file_size =  len(stringToEncode) * 8
compressed_file_size = len(str(encoded)) * 8
compression_ratio = calculate_compression_ratio(original_file_size, compressed_file_size)
print("compression_ratio",compression_ratio)