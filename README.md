Transforming your CSV table into an-SQL query ready format to put in your INSERT INTO function does not get easier. Came in real handy when you (like me) had limited access to upload a table to the database--you just had to make do with what you can do: CREATE TABLE and INSERT INTO.

steps:
1. run 
``` fctii.py(#this sthe args)
```
2. copy all the text from (filename).txt to your INSERT INTO query right after the VALUES statement: INSERT INTO (table name) VALUES ...
3. run the query

sample example:
CREATE TABLE test (column1 INT, column2 STRING )


note: for Impala, always choose STRING over VARCHAR as its innate attribute causes errors in the process. You can just cast the STRING columns back to VARCHAR later under SELECT statement.


