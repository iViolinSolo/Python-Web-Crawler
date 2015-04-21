# Python-Web-Crawler
Web Spider written with python, for user info on Amazon

File Introduction:  
`Deduplication.py` deduplication, deduplicate the same user ids in './userIds'  
`breakpoint` store the breakpoint, for sometimes, Amazon server may let my crawler time out, but I didn't handle such   conditions, so I need a "breakpoint" to store the query stopped accidently, in this file it store a user Id did not be executed, so next time I just need to stop my python program and just restart, run it again, and it can restore query from the breakpoint.  
`data` store some useful information such as the user id did not exits or the web link  
`newIDs` store the user ids after './Deduplication.py' processed, no same user id will exists  
`processFile.py` generate file './userIds', read line and split the line and get user id, its useful, object file is 'http://snap.stanford.edu/data/web-Movies.html'  :  'Movies.txt.gz'  
`storage.dat` something not useful  
`test.html` not useful, website for testing  
`userIds` raw data with some dupligate data  
`userInfo.data` output file , generate by './walker.py'  
`walker.py` main python program, a python spider, fake with http hidders, Disguise as a web explorer, so not to be identified by the Amazon Server  
