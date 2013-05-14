'''
Created on May 13, 2013
@author: Houston Harris
'''

import sys
import string
import json

def main():
    #print "hello there"
    
    tweet_file = open(sys.argv[1])
    
    word_counts = {}
    
    for line in tweet_file:
        lineData = json.loads(line)
        
        if 'text' in lineData:
            line_txt = lineData['text']
            #print line_txt
            
            str_txt = line_txt.encode('utf-8')
            
            exclude = set(string.punctuation)
            line_txt_no_punc = ''.join(ch for ch in str_txt if ch not in exclude)
            
            words = line_txt_no_punc.split();
            for word in words:
                # lowercase
                wordLower = word.lower()
    
                if wordLower in word_counts:
                    # get current count
                    curCount = word_counts[wordLower]
                    curCount += 1
                    word_counts[wordLower] = curCount
                else:
                    # add initial count
                    word_counts[wordLower] = 1
            # end for each word in tweet
        # end if text in tweet
    # end for each line in tweet file
    
    # now we have total word counts
    totalUniqueTerms = float(len(word_counts))
    for wordCount in word_counts:
        #print wordCount + ' ' + str(word_counts[wordCount])
        
        # The frequency of a term can be calculate with the following formula:
        # [Num of occurrences of the term in all tweets]/[Num of occurrences of all terms in all tweets]
        
        frequency = float(word_counts[wordCount]) / totalUniqueTerms
        
        print wordCount + ' ' + str(frequency)
    

if __name__ == '__main__':
    main()