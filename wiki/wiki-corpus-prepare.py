## split texts to sentences

import re
import sys
import time

from nltk.tokenize import sent_tokenize, word_tokenize

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
with open(infilePath, 'r') as f:
    for text in f:
        text = text.strip()
        if len(text) > 20:
            if not text.startswith('<doc id='):
                text = re.sub('\d', '0', text.lower())
                output = sent_tokenize(text)
                for sent in output:
                    tokens = word_tokenize(sent)
                    if not len(tokens) < 6:
                        tagged_sen = []
                        for token in tokens:
                            mk = conRE.findall(token)
                            if mk:
                                keyphrase = token.split(concept_tag)[0]
                                word_list = keyphrase.split(concept_splitter)
                                if len(word_list) > 4:
                                    for wordi in word_list:
                                        tagged_sen.append(wordi)
                                else:
                                    tagged_sen.append(word_list[0] + concept_begin_tag)
                                    if len(word_list) > 1:
                                        for wordi in word_list[1:]:
                                            tagged_sen.append(wordi + concept_intermediate_tag)

                            else:
                                tagged_sen.append(token + other_tag)
                        outfile.write(' '.join(tagged_sen) + "\n")
            else:
                count_articles += 1
                if count_articles % 2000 == 0:
                    elapsed_time = time.time() - start_time
                    print(infilePath.split('/')[-1], 'Processed article number:', count_articles, 'Elapsed time:',
                          elapsed_time, 's')
