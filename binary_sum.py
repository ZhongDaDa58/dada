import sys
su=0

args=sys.argv
if len(args)>2 and len(args)<9:
        for n in args[1:]:
                add=int(n,2)
                su+=add
        summ=format(su,"b")
        print(summ)
else:
        print("error")
