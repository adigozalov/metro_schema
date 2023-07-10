#!/usr/bin/python3


print('#################################################################################')
print('###    Uploading json file to volt table                                      ###')
print('###                                                                           ###')
print('###                                                                           ###')
print('###                                                                           ###')
print('#################################################################################')

import sys
import os
from subprocess import Popen, PIPE
import json

os_path = os.environ["PATH"]
v_home_dir = sys.path[0]
v_data_dir = str(v_home_dir) + "/data/"
# list_files=v_data_dir+"stations.json"

list_files = sorted(os.listdir(v_data_dir))


# Function to call sqlcmd and execute query;
def runSqlQuery(sqlCommand):
    session = Popen(['sqlcmd'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(sqlCommand.encode())
    queryResult, errorMessage = session.communicate()
    out_db = queryResult.decode().split()
    out_db_str = ','.join(out_db)
    return out_db_str


# reading all files on data directory and start reading those files
for file_name in list_files:
    if file_name == 'stations.json':
        with open(v_data_dir + file_name) as user_file:
            parsed_json = json.load(user_file)
        for rows in parsed_json:
            keys_list = list(rows.keys())
            values_list = list(rows.values())
            table_name = file_name.split('.')[0]
            sql_command = 'insert into ' + str(table_name) + ' values(' + str(values_list)[1:-1] + ');'
            # sql_output=runSqlQuery(sql_command)
            print(sql_command)
            # print(sql_output)
            with open("dml.sql", "a") as myfile:
                myfile.write(sql_command + "\n")
    # 2 starting fetch track and block data into station_track and track_blocks from tracks.json file
    elif file_name == 'tracks.json':
        with open(v_data_dir + file_name) as user_file:
            parsed_json = json.load(user_file)
        index_counter = 0
        # 3 Generating unique id for each track and insering track ingormation in station_track table
        for rows in parsed_json:
            index_counter = index_counter + 1
            keys_list = list(rows.keys())
            values_list = list(rows.values())
            sql_command_station_tracks = "insert into station_track(track_id,route_id,from_station_id,to_station_id," \
                                         "distance_in_miles,distance_in_feet) values(" + str(
                index_counter) + ",'" + str(rows["route_id"]) + "','" + str(rows["from_station_id"]) + "','" + str(
                rows["to_station_id"]) + "'," + str(rows["distance_between_miles"]) + "," + str(
                rows["distance_feet"]) + ");"
            print(str(rows["to_station_id"]))
#            sql_command_station_tracks = "insert into station_track(track_id,route_id,from_station_id,to_station_id) values(" + str(index_counter) + ",'" + str(rows["route_id"]) + "','" + str(rows["from_station_id"]) + "','" + str(rows["to_station_id"]) + "');"
            # sql_output=runSqlQuery(sql_command_station_tracks)
            print(sql_command_station_tracks+ str(rows["to_station_id"]))
            # print(sql_output)
            with open("dml.sql", "a") as myfile:
                myfile.write(sql_command_station_tracks + "\n")
            block_index_counter = 0

            # 4 generating unique index and inserting block information into track_blocks
            for block_distance in rows["track_blocks"]:
                block_index_counter = block_index_counter + 1
                block_index = str(index_counter) + str(block_index_counter)
                sql_command_track_blocks = "insert into track_blocks(block_id,track_id,block_distance_in_feet) " \
                                           "values(" + str(block_index) + "," + str(index_counter) + "," + str(
                    block_distance) + ");"
                # sql_output=runSqlQuery(sql_command_track_blocks)
                print(sql_command_track_blocks)
                # print(sql_output)
                with open("dml.sql", "a") as myfile:
                    myfile.write(sql_command_track_blocks + "\n")
