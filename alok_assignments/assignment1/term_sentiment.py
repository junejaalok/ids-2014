import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        my_tweet=json.loads(line)
        place=my_tweet['place']
        if place:
            print "hello"
#        try:
#            print my_tweet['place']
#        except Exception:
#            print "place doesn't exist"

        
if __name__ == '__main__':
    main()
