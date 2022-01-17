Transforming your CSV table into an-SQL query ready format to put in your INSERT INTO function does not get easier. Came in real handy when you (like me) had limited access to upload a table to the database--you just had to make do with what you can do: CREATE TABLE and INSERT INTO.

# steps:
1. run script
``` 
py fctii.py filename null_symbol string_columns
```
args:
* filename has to be in **csv** without its .csv ending and include their parent directory if not already in the same dir--but still has to be under the working directory
** null_symbol is usually either NULL or ?
*** string_columns define the columns that need the apostrophes around the phrase, could be in the columns' index (1-based) or names
2. copy all the text from (filename).txt to your INSERT INTO query right after the VALUES statement: INSERT INTO (table name) VALUES (_insert here_)
3. run query

# sample example:
for a table of form in a **food_stall.csv** to be inserted into a **sample_table** table in your databse:
columns
1   id      int
2   stall   string
3   food    string
sample
    id  stall             thing
 1  01  Cirebon 77        Bubur Ayam
 2  02  Depan Kanayakan   Sate Ayam
 3  11  For You           Juice
 4  21  Delicious Night   ?

run
``` 
py fctii.py food_stall ? 2,thing
```

open
food_stall.txt
and copy all the text inside—expected text inside the file:
```
(01,"Cirebon 77","Bubur Ayam"),
(02,"Depan Kanayakan","Sate Ayam"),
(11,"For You","Juice"),
(21,"Delicious Night",NULL);
```

query
INSERT INTO sample_table 
VALUES 
(**_paste all the copied text here_**);

requirements: Python 3.7 version or above, Numpy, pandas

note: for Impala, and prolly some other SQL accent (likely Hive too), always define tables with STRING type instead of VARCHAR as its innate attribute does not allow VARCHAR type data to be inserted through query. If needed during a joining process, the STRING columns can just be cast as VARCHAR later under SELECT statement.


