# get all user id
def processLine(line):
    if(line.startswith(r'review/userId:')):
        userId = line.split(r' ')
        return userId[1]
    else:
        return 0


fw = file("userIds", "w")

filepath = "movies.txt"
with open(filepath) as f:
    for line in f:
        userId = processLine(line)
        if(userId != 0):
            fw.write(userId)
        #do sth
        # print line

# userId = processLine('review/userId: A3NPHQVIY59Y0Y')
# print userId
