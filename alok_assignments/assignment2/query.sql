SELECT qu.docid, f.docid,sum(qu.count*f.count)
from (
SELECT * FROM frequency
UNION
SELECT 'q', 'washington', 1 
UNION
SELECT 'q', 'taxes', 1
UNION 
SELECT 'q', 'treasury', 1) qu, frequency f
where qu.term=f.term and qu.docid='q'
group by qu.docid,f.docid
order by sum(qu.count*f.count);
