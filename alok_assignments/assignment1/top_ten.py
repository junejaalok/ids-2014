import sys
import json
import re

#Function to extract the hashtags and put in dict
def hashtagfile(afile):
    hashtags_dict={}
    for line in afile:
        my_tweets=json.loads(line)
        if 'text' in my_tweets.keys():
            hashtags=my_tweets['entities']['hashtags']
        
            if hashtags is not None:
                for hashtag in hashtags:
                    if hashtag['text'] not in hashtags_dict:
                        hashtags_dict[hashtag['text']] = 1
                    else:
                        hashtags_dict[hashtag['text']] += 1
    
    return hashtags_dict

#Order the hashtags dictionary based on the count
def orderme(d):
    sorted_d=sorted(d.items(), key=lambda x: x[1],reverse=True)
    return sorted_d

def main():
    tweet_file = open(sys.argv[1])
    hashes=hashtagfile(tweet_file)
    ready=orderme(hashes)
    for k in range(10):
        print ready[k][0], ready[k][1]
    
if __name__ == '__main__':
    main()
    