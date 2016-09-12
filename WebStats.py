'''
Given a site download the webstats from the site using Python 
(you can use requests module)

1. Find out the response codes that are recieved for each site and 
show the counts of how many times each response code has been 
encountered.

2. Now from the downloaded file, collect the number of hits(GET/POST)
   made on different sites.

Works for both Python 2.7 and Python 3.5

author - Pabitra Kumar Pati
'''

import requests
import re
from sys import version_info
import logging

logging.basicConfig(filename="WebStats.log", filemode='w', level=logging.INFO)
log = logging.getLogger("WebStats.py")

# Link for such stat files :- https://sites.google.com/site/stats202/data
r = requests.get("https://sites.google.com/site/stats202/data/weblog.txt?attredirects=0&d=1")

if version_info[0] < 3:
    out = r.content
else:
    out = r.text

data = {}
codes = [200, 302, 304, 404]
url_dict = {}

# Get each line by splitting with new line '\n'
content = out.split('\n')
for line in content[:-1]:
    #print(line)
    m = re.search('GET(.+?\" \d{3}) ', line)
    if m:
        result= m.group(1)
    else:
        m = re.search('POST(.+?\" \d{3}) ', line)
        if m:
           result= m.group(1)
    if not m:
        log.info(" No GET/POST found so skipping this line  :- {} ".format(line))
        continue

    #print (result, type(result))
    result = result.split('/')
    url = result[0].strip()
    code= int(result[-1].split()[-1])
    #print(code, url)
    # Check if the error code already exists in the dictionary
    if code in data:
        data[code].update({url: data[code][url]+1}) if url in data[code] else ( data[code].update({url:1})) 
    else:
        data.update({(code):{url:1}})
 
# check for how many times each code has been encountered
for code in data:
    s = sum([data[code][url] for url in data[code]])
    # Put an if condition if you want to print only stats for codes in codes list    
    log.info("  Response Code {} has been encountered {} times".format(code, s)) 

    # Collect the number of time the URL is hit
    # This could also be done, while parsing the line in content
    dct = {url:data[code][url] for url in data[code]}
    for k,v in dct.items():
         url_dict.update({k: url_dict[k]+v}) if k in url_dict else url_dict.update({k:v})

log.info(" ======================================================")

for url in url_dict:
    log.info("  URL '{}' has been hit {} times".format(url, url_dict[url]))

# END
