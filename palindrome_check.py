import sys
import json

data={
    "palindrome":"",
    "result":""
    }
with open(sys.argv[1],"r") as file:
    content=file.read()
ls=[s for s in content if s.isalpha()]

vls=ls[::-1]

s_ls="".join(ls).lower()
s_vls="".join(vls).lower()

if s_ls==s_vls:
    data["palindrome"]="true"
    data["result"]=s_ls
else:
    data["palindrome"]="false"
    data["result"]=s_ls
with open("output.json","w") as file:
    json.dump(data,file)
