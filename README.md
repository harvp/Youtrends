# Youtrends
youtubeTrend.py - Python code to insert JSON data to Cassandra DB
videoinfo.json - JSON data file
cassandra-queries.sql - Commands to create keyspace and tables in the Cassandra

Program need to be run by following beloe steps:

1) Start the Cassandra Server on your system
     cassandra -f is the command for macOS
     
2) Once server is up and running, enter CQL command prompt using below command in new terminal
        cqlsh

3) Follow the commands in the .sql file one by one

4) Open a new terminal and create a Python Virtual Environment so that the program can run

5) Run the program using the below command:
    python youtubeTrend.py
