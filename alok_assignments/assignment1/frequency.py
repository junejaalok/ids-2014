import sys
import json
import re

def tfile(afile):
    tweet=[]
    for line in afile:
        my_tweets=json.loads(line)
        if 'text' in my_tweets.keys():
            clear_tweets = re.sub(ur'[^\s\w_]+', u'', my_tweets['text'], flags=re.UNICODE)
            tweet.append(clear_tweets)
    return tweet

def freq(tweets):
    count=0
    score_dict={}
    for i in range(len(tweets)):
        for j in tweets[i].encode('UTF-8').split():
            count += 1
            if j not in score_dict:
                score_dict[j] = 1
            else:
                score_dict[j] += 1
    for key in score_dict:
        print "%s %f" % (key,score_dict[key]/float(count))

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets=[]
    tweet_file = open(sys.argv[1])
    tweets=tfile(tweet_file)
    freq(tweets)
    
if __name__ == '__main__':
    main()
    