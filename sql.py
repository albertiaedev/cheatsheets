#SQL CHEATSHEET

#Select specific entries
query = SELECT col FROM `folder.db.table`
        WHERE col='row'
        #if you want to select multiple columns, you can separate them with a comma ',' between the names
        #if you want to select all columns, you can use a '*' instead of a column name
        
#Count the entries in a column
COUNT()
#Put together all columns with the same value
GROUP BY
#Exclude entries with a certain criteria
HAVING
#Example:
SELECT col, COUNT(ID)
FROM `folder.db.table`
GROUP BY col
HAVING COUNT(ID)=n
