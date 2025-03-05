import sys

def output(obj):
    import json
    print(json.dumps(obj))

with open(sys.argv[1],'r') as read:
    para=read.read()

new_para=para.lower().replace('.','').replace('!','').replace('?','').replace('\n',' ')
ls=new_para.split()


set_ls=set(ls)
dict={}
for word in set_ls:
    dict[word]=ls.count(word)
output(dict)
