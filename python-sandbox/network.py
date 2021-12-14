


#  SOCKET /////////////////////////////////////////
        # import socket 
        # mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # mysock.connect(('data.pr4e.org', 80))
        # cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
        # mysock.send(cmd)

        # while True:
        #     data=mysock.recv(512)
        #     if(len(data) <1):
        #         break
        #     print(data.decode())
        # mysock.close()

#  /////////////////////////////////////////
#  urllib /////////////////////////////////////////

import urllib.request, urllib.parse, urllib.error

# 1) 
        # fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
        # # fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
        # for line in fhand:
        #     print(line.decode().strip())

# 2) - Dictionary with word frquency 
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) +1
print(counts)



# 7:09:00
# Web Scraping 

# BEAUTIFUL SOUP
# Instll Beautiful Soup - Interface for retreiveing "tags" via web scraping
# install :
#   https://pypi.python.org/pypi/beautifulsoup4

# example: pull this file: https://www.py4e.com/code3/bs4.zip


