# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. Both user names and 
# company names are composed of letters only.



my_mail = input("Enter the email: ")
separator = my_mail.split("@")      # here split function breaks the string and in split function string break from @
print("username is:",separator[0])