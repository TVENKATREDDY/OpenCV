import re
import email.utils
pattern=r'^[a-zA-Z][\w_.-]+@[a-z]+\.[a-z]{1,3}$'
n=int(input())
for i in range(n):
    email1=input()
    name,mail=email.utils.parseaddr(email1)
    match=re.search(pattern,mail)   
    print('Match: ',match) 
    if match:
        print(email.utils.formataddr((name,mail)))