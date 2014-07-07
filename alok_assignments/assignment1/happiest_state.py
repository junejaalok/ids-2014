import sys
import json
import re
import string

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k

#Order the states-happy_index dictionary based on the happy_index
def orderme(d):
    sorted_d=sorted(d.items(), key=lambda x: x[1],reverse=True)
    return sorted_d

def sfile(afile):
    scores = {} # initialize an empty dictionary
    for line in afile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores # Print every (term, score) pair in the dictionary

def score_line(score,my_tweet):
    if 'text' in my_tweet:
        if "lang" in my_tweet and my_tweet["lang"]=="en":
            clear_tweet = re.sub(ur'[^\s\w_]+', u'', my_tweet['text'], flags=re.UNICODE)
            clear_tweet=clear_tweet.split()
            count=0
            for i in range(len(clear_tweet)):
                word=clear_tweet[i].encode('UTF-8').lower()
                if word in score:
                    count += score[word]
            return count

def main():
    sent_file = open(sys.argv[1])
    dict_scores=sfile(sent_file)
    tweet_file = open(sys.argv[2])

    happy_index={}
    for line in tweet_file:
        my_tweet=json.loads(line)
        if 'place' in my_tweet:
            if my_tweet['place'] is not None and my_tweet['lang'] == 'en':
                if 'full_name' in my_tweet['place'].keys():
                    if my_tweet['place']['full_name'] is not None:
                        state= my_tweet['place']['full_name'].encode('UTF-8')
                        st = state.split(',')
                        if len(st) == 2:
                            if len(st[1].strip()) == 2:
                                loc= st[1].strip()
                            elif len(st[1].strip()) == 3:
                                loc= reverse_lookup(states,st[0].strip())
                            score=score_line(dict_scores,my_tweet)
                            if loc not in happy_index:
                                happy_index[loc] = score
                            else:
                                happy_index[loc] += score
    ready=orderme(happy_index)
    print ready[0][0]

if __name__ == '__main__':
    main()
    