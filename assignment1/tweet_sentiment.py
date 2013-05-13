import sys
import string
import json

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
    #count = 0
    for line in tweet_file:
        lineData = json.loads(line)
        #print lineData
        
        tweetScore = 0
        if 'text' in lineData:
            line_txt = lineData['text']
            #print line_txt
            
            str_txt = line_txt.encode('utf-8')
            
            # remove common punctuation
            exclude = set(string.punctuation)
            line_txt_no_punc = ''.join(ch for ch in str_txt if ch not in exclude)
            
            #print line_txt_no_punc
            
            # see if word in afin list
            words = line_txt_no_punc.split();
            for word in words:
                # lowercase
                wordLower = word.lower()
                
                if wordLower in scores:
                    tweetScore += scores[wordLower]
                    #print 'Word: ' + wordLower + ' Sentiment score: ' + str(scores[word])
                    
        print float(tweetScore)
            
        #count = count + 1
        #if (count > 100):
        #    break
    
    

if __name__ == '__main__':
    main()
