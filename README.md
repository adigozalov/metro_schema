# metro_schema
Scripts are designed to create objects, read json files from ./data directory and upload data into volt database. 

Execute run.sh to 
1. create objects using ddl.sql
2. Pars json files in the data directory
3. create dml.sql which will have all insert statements with the necessary data from json files.
4. exectute dml.sql to over volt database.
5. remove dml.sql from os.
   
Test changes 