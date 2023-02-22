#a-z
#A-Z
#0-9
#.,_ one time used
#@ one time used 
#. will be placed in 2nd or 3rd position from the last 

import re
email_condition="^[a-z A-Z]+[\._]?[a-z A-Z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your email id :")


if re.search(email_condition,user_email):
    print("email is valid ")
else:
    print("wrong email")    