-- answer still not correct, must be close though
select a.docid, b.docid, a.term, b.term, sum(a.count * b.count) as similarity
from frequency a, 
(
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) b
where a.term = b.term
group by a.docid
order by similarity desc

-- I think this is basically the similar, yields higher counts, still not correct
select a.docid, a.term, b.term, sum(a.count*b.count) as mCount
from frequency a, frequency b
where (a.term = "washington" or a.term = "taxes" or a.term ="treasury")
    and (b.term = "washington" or b.term = "taxes" or b.term ="treasury")
    and a.term = b.term and a.docid != b.docid
group by a.docid
order by mCount desc

--select a.docid,  a.term, a.count
--from frequency a
--where a.docid = "9795_txt_trade"
--order by a.term desc

--select docid, term, count
--from frequency
--where docid = "16094_txt_trade"

--select docid, term, count
--from frequency
--where (docid = "16094_txt_trade" and term = "washington")
--    or  (docid = "16094_txt_trade" and term = "taxes")
--    or (docid = "16094_txt_trade" and term ="treasury")


--select docid, term, sum(count)
--from frequency
--where (term = "washington")
--    or  (term = "taxes")
--    or (term ="treasury")
--group by docid
--order by count desc, docid desc
