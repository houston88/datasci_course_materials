select sumCount,docid from
(  
    select sum(count) as sumCount,docid
    from frequency
    group by docid
)
where sumCount > 300
