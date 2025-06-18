# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#m=re.search('(\w)+','aaadaa')
str1=input()
pattern=re.compile(input())
m=pattern.search(str1)
if not m:print(tuple((-1,-1)))
while m:
    si=m.start()
    ei=m.end()-1
    t=tuple((si,ei))
    print(t)
    m=pattern.search(str1,m.start()+1)

        
