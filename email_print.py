#Open the file mbox-short.txt and read it line by line. When you find a line 
# that starts with 'From ' like the following line: 
#         From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008



fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
existing=[]
for line in fh:
    if line.startswith("From "):
        words=line.split()
        #if words[1] not in existing:
        print(words[1])
        existing.append(words[1])
        count=count+1

print("There were", count, "lines in the file with From as the first word")