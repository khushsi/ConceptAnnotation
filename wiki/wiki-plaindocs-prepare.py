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
concept_tag = '\CON'
other_tag = "\O"
concept_begin_tag = '\CON-B'
concept_intermediate_tag = '\CON-I'
concept_splitter = '*'
splitted_texts = ''
count_articles = 0
count_tokens = 0
start_time = time.time()
outfile = open(outfilePath, 'w')
conRE = re.compile('\\\\CON')
infile = open(infilePath)
filedata = "<root>" + infile.read() + "</root>"

soup = BeautifulSoup(filedata, 'html.parser')
doc_tag = soup('doc')

for doc in doc_tag:
    content = doc.contents[0].replace("\n", " ")
    tokens = []
    for word in content.split(" "):
        mk = conRE.findall(word)
        if mk:
            concept = word.replace(concept_tag, "").split("*")
            tokens += concept
        else:
            tokens.append(word)
    outfile.write(' '.join(tokens) + "\n")
