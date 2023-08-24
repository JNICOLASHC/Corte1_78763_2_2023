def app(a,*args,**kwargs):
    print(args)
    print(kwargs)

if __name__=="__main__":
    app(1,2,3,4,5,x,m=1,b=2)