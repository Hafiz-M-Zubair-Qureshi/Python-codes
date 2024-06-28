# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


import zlib
x="hello world!hello world!hello world!hello world!"
compressed_string=zlib.compress(x.encode())
decompressed_string=zlib.decompress(compressed_string)
decompressed_string=decompressed_string.decode()
print("Original String:",x)
print("Compressed string:",compressed_string)
print("decompressed sting",decompressed_string)
