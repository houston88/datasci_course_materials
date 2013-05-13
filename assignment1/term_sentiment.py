import sys
import string
import json
import math

def hw():
    print 'Processing tweets....'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(afinnfile)
    #lines(tweet_file)

    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        # The file is tab-delimited. "\t" means "tab character"
        term, score  = line.split("\t")
        # Convert the score to an integer.        
        scores[term] = int(score)
        
    # Print every (term, score) pair in the dictionary
    #print scores.items()
    
    # lets try and load json output
    tweet_file = open(sys.argv[2])
    
    # key: unknown term, value: set of associated words
    unknown_words = {}
    
    for line in tweet_file:
        lineData = json.loads(line)
        #print lineData
        
        if 'text' in lineData:
            line_txt = lineData['text']
            #print line_txt
            
            str_txt = line_txt.encode('utf-8')
            
            # remove common punctuation
            exclude = set(string.punctuation)
            line_txt_no_punc = ''.join(ch for ch in str_txt if ch not in exclude)
            
            #print line_txt_no_punc
            
            assocWords = []
            unknWords = []
            
            # see if word in afin list
            words = line_txt_no_punc.split();
            for word in words:
                # lowercase
                wordLower = word.lower()
                
                if wordLower in scores:
                    # add to assoc words
                    assocWords.append(wordLower)
                else:
                    # add to new term words
                    unknWords.append(wordLower)
            
            # now associate the known and unknown words
            for unknWord in unknWords:
                if unknWord in unknown_words:
                    termAssocWords = unknown_words[unknWord]
                    for assocWord in assocWords:
                        termAssocWords.add(assocWord)
                    # set back into dict
                    unknown_words[unknWord] = set(termAssocWords)
                else:
                    termAssocWords = []
                    for assocWord in assocWords:
                        termAssocWords.append(assocWord)
                    # set into dict
                    unknown_words[unknWord] = set(termAssocWords)

        # end if text in tweet
    # end for each line in tweet
        
    # we now have a collection of unknown terms and their associated known sentiment words
    
    # for each association, calculate a sentiment for unknown term
    for unknWord in unknown_words:
        assocWords = unknown_words[unknWord]
        
        if (len(assocWords) > 0):
            #print 'For ' + unknWord + ' associated sentiment words: ' + str(assocWords)
            
            posScore = 1
            negScore = 1
            
            for word in assocWords:
                if (scores[word] > 0):
                    # positive associated word
                    posScore += scores[word]
                else:
                    # negative associated word
                    negScore += math.fabs(scores[word])
    
            #print 'Calc: ' + str(posScore) + '/' + str(negScore)
    
            # calc term sentiment
            sentiment = posScore / negScore
        
            # print out sentiment
            print unknWord + ' ' + str(sentiment)
        
        # end if
    

if __name__ == '__main__':
    main()
