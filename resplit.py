# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
vow='aeiouAEIOU'
con='QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
print(con)
pattern=rf'(?<=[{con}])([{vow}]{{2,}})(?=[{con}])'
#pattern=rf'([{con}])([{vow}]{{2,}})([{con}])'

matches=[]
#match=re.finditer(pattern,s)

for match in re.finditer(pattern,s):
    vowel=match.group(1)
    matches.append(vowel)
    #print(vowel)
    if vowel:
        print(vowel)
    else:
        print(-1)
if len(matches)==0:
    print(-1)
   
            
        
    