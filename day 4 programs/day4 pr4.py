s=(input("Enter a string:"))
s = ''.join(e for e in s if (e.isalnum()))
s=s.lower().replace(" ","")
str=""
for i in s:
   str=i+str
str2=str
if(s==str):
    print(True)
else:
    print(False)
Footer
