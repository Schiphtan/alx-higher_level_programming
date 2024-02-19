-- Lists all records of the table
-- Execute: cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name
FROM second_table
ORDER BY score DESC, name;
