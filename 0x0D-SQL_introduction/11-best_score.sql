-- lists all records with a score >= 10 in the table 
-- Execute: cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
