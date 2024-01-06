import urllib.request, urllib.parse, urllib.error
host = 'data.pr4e.org'
fhand = urllib.request.urlopen(f'http://{host}/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # adds one to the value 
        #here key is word and value is 0 then 1 is added
print(counts)