import sys
import json
import re

def sfile(afile):
    scores = {} # initialize an empty dictionary
    for line in afile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores # Print every (term, score) pair in the dictionary

def tfile(afile):
    tweet=[]
    for line in afile:
        my_tweets=json.loads(line)
        if 'text' in my_tweets.keys():
            clear_tweets = re.sub(ur'[^\s\w_]+', u'', my_tweets['text'], flags=re.UNICODE)
            tweet.append(clear_tweets)
    return tweet

def hw():
    print 'Hello, world!'

def match(score,tweets):
    for i in range(len(tweets)):
        count=0
        for j in score:
            if j in tweets[i].encode('UTF-8').lower():
                count += score[j]
        print count

def lines(fp):
    print str(len(fp.readlines()))

def main():
    dict_scores={}
    tweets=[]
    match_score=[]
    sent_file = open(sys.argv[1])
    dict_scores=sfile(sent_file)
    tweet_file = open(sys.argv[2])
    tweets=tfile(tweet_file)
    match(dict_scores,tweets)
    
if __name__ == '__main__':
    main()
    