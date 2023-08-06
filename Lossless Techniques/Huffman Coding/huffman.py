import re
import numpy as np
from PIL import Image
import time
import math
import cv2
def calculate_compression_ratio(original_size, compressed_size):
    compression_ratio = original_size / compressed_size
    return compression_ratio

print("Huffman Compression Program")
print("=================================================================")
h = int(input("Enter 1 if you want to input a color image file, 2 for default grayscale case:"))
if h == 1:
    file = input("Enter the filename:")
    my_string = np.asarray(Image.open(file), np.uint8)
    shape = my_string.shape
    a = my_string
    print("Entered string is:", my_string)
    my_string = str(my_string.tolist())
elif h == 2:
    array = np.arange(0, 737280, 1, np.uint8)
    my_string = np.reshape(array, (1024, 720))
    print("Entered string is:", my_string)
    a = my_string
    my_string = str(my_string.tolist())
else:
    print("You entered an invalid input")

start_time = time.time()
letters = []
only_letters = []
for letter in my_string:
    if letter not in letters:
        frequency = my_string.count(letter)
        letters.append(frequency)
        letters.append(letter)
        only_letters.append(letter)

nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]

nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)

def combine_nodes(nodes):
    pos = 0
    newnode = []
    if len(nodes) > 1:
        nodes.sort()
        nodes[pos].append("1")
        nodes[pos+1].append("0")
        combined_node1 = (nodes[pos][0] + nodes[pos+1][0])
        combined_node2 = (nodes[pos][1] + nodes[pos+1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine_nodes(nodes)
    return huffman_tree

newnodes = combine_nodes(nodes)
huffman_tree.sort(reverse=True)

print("Huffman tree with merged pathways:")
checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)

count = 0
for level in huffman_tree:
    print("Level", count, ":", level)
    count += 1
print()

letter_binary = []
if len(only_letters) == 1:
    lettercode = [only_letters[0], "0"]
    letter_binary.append(lettercode * len(my_string))
else:
    for letter in only_letters:
        code = ""
        for node in checklist:
            if len(node) > 2 and letter in node[1]:
                code = code + node[2]
        lettercode = [letter, code]
        letter_binary.append(lettercode)

print(letter_binary)
print("Binary code generated:")
for letter in letter_binary:
    print(letter[0], letter[1])

bitstring = ""
for character in my_string:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]

binary = "0b" + bitstring
print("Your message as binary is:")

end_time = time.time()
execution_time_lzw = end_time - start_time

print("Compression time:", execution_time_lzw)
uncompressed_file_size = len(my_string) * 7
compressed_file_size = len(binary) - 2
compression_ratio = calculate_compression_ratio(uncompressed_file_size, compressed_file_size)
print("Compression Ratio:", compression_ratio)
print("Your original file size was", uncompressed_file_size, "bits. The compressed size is:", compressed_file_size)
print("This is a saving of", uncompressed_file_size - compressed_file_size, "bits")

output = open("compressed.txt", "w+")
print("Compressed file generated as compressed.txt")

start_time = time.time()
print("Decoding.......")
output.write(bitstring)
bitstring = str(binary[2:])
uncompressed_string = ""
code = ""
for digit in bitstring:
    code = code + digit
    pos = 0
    for letter in letter_binary:
        if code == letter[1]:
            uncompressed_string = uncompressed_string + letter_binary[pos][0]
            code = ""
        pos += 1

print("Your UNCOMPRESSED data is:")
if h == 1:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, shape)
    print(res)
    print("Observe the shapes and input and output arrays are matching or not")
    print("Input image dimensions:", shape)
    print("Output image dimensions:", res.shape)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    if np.array_equal(a, res):
        print("Success")
if h == 2:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    print(res)
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, (1024, 720))
    print(res)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    print("Success")

end_time = time.time()
execution_time_lzw = end_time - start_time
print("Decompression time:", execution_time_lzw)
print("compressio ratio:",compression_ratio)
