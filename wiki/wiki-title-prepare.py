## split texts to sentences

import re
import sys
import time

from bs4 import BeautifulSoup

stdout = sys.stdout
# reload(sys)
# sys.setdefaultencoding('utf-8')
sys.stdout = stdout

infilePath = sys.argv[1]
outfilePath = sys.argv[2]
concept_tag = '\con'
other_tag = "\O"
concept_begin_tag = '\CON-B'
concept_intermediate_tag = '\CON-I'
concept_splitter = '*'
splitted_texts = ''
count_articles = 0
count_tokens = 0
start_time = time.time()
outfile = open(outfilePath, 'w')
conRE = re.compile('\\\\con')
infile = open(infilePath)
filedata = "<root>" + infile.read() + "</root>"

soup = BeautifulSoup(filedata, 'html.parser')
doc_tag = soup('doc')

for doc in doc_tag:
    title = doc.get('title')
    if len(title) > 1:
        outfile.write(title + "\n")
