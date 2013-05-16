select a.docid, b.docid, a.count as transCount, b.count as worldCount
from frequency a, frequency b
where a.term = "transactions" and 
               b.term = "world" and
               a.docid = b.docid
