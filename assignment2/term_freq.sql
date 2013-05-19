--select a.row_num, b.col_num, sum(a.value * b.value)
--from a, b
--where a.col_num = b.row_num
--group by a.row_num, b.col_num

--select a.docid, b.docid, 
--from frequency a, frequency b
--where a.docid < b.docid

SELECT a1.row_id AS document_i, a2.row_id AS document_j,
(a1.row_v * a2.row_v) /
((a1.row_v * a1.row_v) * (a2.row_v * a2.row_v)) AS theta
FROM a AS a1, a AS a2
WHERE a1.row_id > a2.row_id
