--similarity matrix
select a.docid, a.term, b.term, sum(a.count * b.count) as similarity
from frequency a, frequency b
where a.docid = "10080_txt_crude" and b.docid = "17035_txt_earn"
   and a.term = b.term
group by a.docid
