import sys
import json
import re
import string

#AFINN-111.txt file in dictionary
def sfile(afile):
    scores = {} # initialize an empty dictionary
    for line in afile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores # Print every (term, score) pair in the dictionary

#Score each tweet
def score_line(score,my_tweet):
    clear_tweet = re.sub(ur'[^\s\w_]+', u'', my_tweet['text'], flags=re.UNICODE)
    clear_tweet=clear_tweet.split()
    count=0
    for i in range(len(clear_tweet)):
        word=clear_tweet[i].encode('UTF-8')
        if word in score:
            count += score[word]
    return count

#list of absent words in scoring dictionary (AFINN-111.txt)
def abs_me(score,my_tweet):
    temp=[]
    clear_tweet = re.sub(ur'[^\s\w_]+', u'', my_tweet['text'], flags=re.UNICODE)
    clear_tweet=clear_tweet.split()
    for i in range(len(clear_tweet)):
        word=clear_tweet[i].encode('UTF-8')
        if word not in score:
            temp.append(word)
    return temp
               
def main():
    absent={}
    final={}
    sent_file = open(sys.argv[1])
    dict_scores=sfile(sent_file)
    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        my_tweet=json.loads(line)
        if 'text' in my_tweet and my_tweet['text'] is not None:
            score=score_line(dict_scores,my_tweet)
            abs_list=abs_me(dict_scores,my_tweet)
            
            pos=0
            neg=0

            if score < 0:
                neg+=score
            elif score > 0:
                pos+=score
       
            for i in range(len(abs_list)):
                word=abs_list[i]
                if word not in absent:
                    num=1
                    absent[word]=[score,num]
                else:
                    num+=1
                    absent[word][0]+=score
                    absent[word][1]+=num
                
    for word in absent:
        print word,absent[word][0]/float(absent[word][1])

if __name__ == '__main__':
    main()
    