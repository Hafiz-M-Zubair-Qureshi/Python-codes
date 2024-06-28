# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.




ascii_string = input("Enter the ascii code = ")
acscii_to_unicode = ascii_string.encode("utf-8")
print(acscii_to_unicode)