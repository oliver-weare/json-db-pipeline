This is my 2nd attempt a building a data pipeline. I wanted to create something a little more complex (in comparison to my first project).

Here is how the full project works, with the order in which the project files should be executed. 
[postgresql is required for this project]

1. [RUN]: create_db.py -- a simple script that creates the required databse on your machine and then creates the table using the create_table.sql in the 'sql' folder.

2. [RUN]: generate_jsons.py -- this generates 1000 json files, all containing one field called 'random_number' with a random generated number as the value. Running this script is only necesary once, but running it again will replace the original 1000 files.

3. [RUN]: populate_pipeline.py -- here the table is populated with the 1000 json files.

4. [RUN]: visualise.py -- all of the rows are printed to the terminal for casual viewing.