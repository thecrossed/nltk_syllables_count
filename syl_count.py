import csv
import nltk
from nltk.corpus import cmudict
from nltk.tokenize import sent_tokenize, word_tokenize
wordSyl = nltk.corpus.cmudict.dict()

def countSyl(filename):
#  open target file
   with open(filename,'r',encoding ='utf-8') as f:
      csv_reader = csv.reader(f)
      with open('countResult.csv','w',encoding ='utf-8') as r:
         thewriter = csv.writer(r)
         for content in csv_reader:
            for l in content:
               count = 0
               line = l.split(':')[-1]
               w = word_tokenize(line)
               for s in w:
                  try:
                     for x in wordSyl[s.lower()][0]:
                        if len(x)==3:
                           count += 1
                  except:
                     continue
#            print (line,count)
               thewriter.writerow([line,count])
            
         
countSyl('count_syl.csv')

      
