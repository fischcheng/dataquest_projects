def load_data():
    import pandas as pd
    column_names=['submission_time', 'upvotes', 'url', 'headline']
    df=pd.read_csv('hn_stories.csv',header = None, names = column_names)
    return df 

if __name__== "__main__":
    load_data()
    