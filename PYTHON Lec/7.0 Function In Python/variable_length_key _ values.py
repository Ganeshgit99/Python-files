'''

Varaible length key value pair


addition=(a=10)                         l=1
addition=(a=10,b=20)                    l=2
addition=(a=10,b=20,c=30)               l=3
addition=(a=10,b=20,c=30,d=40)          l=4

'''
def addition(**data):
    s=0
    for i in data:
        s=s+data[i]
    print("Addition is:",s)
    #print(data)
    #print(type(data))
addition(a=10)                         
addition(a=10,b=20)                    
addition(a=10,b=20,c=30)               
addition(a=10,b=20,c=30,d=40)

#Dryrun
'''
data           i    s
{a:10}         a    s=0+data[a]=0+10=10    s=10
{a:10,b:20}    a    s=0+data[a]=0+10=10    s=10
               b    s=10+data[b]=10+20=30  s=30

'''



