# Assuming that we have some email addresses in the "username@companyname.com" format, please write program 
# to print the company name of a given email address. Both user names and company names are composed of letters only.



my_mail = input("Enter the email: ")
separator = my_mail.split("@")
company = separator[1].split(".")
print("company Name is:",company[0])