SELECT A.docid,B.docid,sum(A.count*B.count)
FROM frequency A, frequency B
WHERE A.term=B.term and A.docid < B.docid and 
A.docid='10080_txt_crude' and B.docid='17035_txt_earn'
group by A.docid, B.docid;