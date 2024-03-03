-- converts hbtn_0c_0 database to UTF8
-- Execute: cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
USE hbtn_0c_0
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHANGE name name  VARCHAR (256) CHARACTER utf8mb4 COLLATE utf8mb4_unicode_ci;
