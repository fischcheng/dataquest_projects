import read
df = read.load_data()

all_headline=""
for row in df['headline']:
    all_headline+=str(row)

list_words=all_headline.split(" ")
lower=[word.lower() for word in list_words]

from collections import Counter
cnt = Counter()
for word in lower:
    cnt[word] += 1

print(cnt.most_common(100))

