import read

df=read.load_data()

df['submission_time']

def parse_hour(tstp):
    from dateutil.parser import parse
    return parse(tstp).hour


df['hour']=df['submission_time'].apply(parse_hour)

occurence=df['hour'].value_counts()

for name,row in occurence.items():
    print("{0}: {1}".format(name, row))
    