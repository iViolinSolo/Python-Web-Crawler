filepath = "userIds"
result=[]
with open(filepath) as f:
    for line in f:
        result.append(line)
        #do sth
        # print line

listUserIds = list(set(result))
#after deduplication UserId
f = file("newIDs","w")
for item in listUserIds:
    f.write(item)
f.close()
