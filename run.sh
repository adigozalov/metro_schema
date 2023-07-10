#!/bin/bash

python3 json_uploader.py

sqlcmd  < ddl.sql 

sqlcmd < dml.sql


rm dml.sql

