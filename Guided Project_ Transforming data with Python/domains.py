import read
df = read.load_data()

#print(df['url'].loc[0:5])
domains=df['url'].value_counts()[0:100]

#for name,row in domains.items():
#    print("{0}: {1}".format(name, row))
    

def subdomain(dname):
    slist=str(dname).split('.')
    if len(slist)>2:
        oname=".".join(slist[-2:])
    else:
        oname=str(dname)
    return oname

df['subdomain']=df['url'].apply(subdomain)

subdm=df['subdomain'].value_counts()[0:100]
for name,row in domains.items():
    print("{0}: {1}".format(name, row))
    

