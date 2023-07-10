drop table stations if EXISTS;
CREATE TABLE stations
(
station_id VARCHAR(20) ,
coordinate_x DECIMAL,
coordinate_y DECIMAL,
station_name  VARCHAR(100) ,
CONSTRAINT pk_station_id
PRIMARY KEY (station_id)

) ;


drop table station_track if EXISTS;

CREATE TABLE station_track (
track_id INTEGER,
route_id VARCHAR(20),
from_station_id VARCHAR(20),
to_station_id VARCHAR(20),
distance_in_miles DECIMAL,
distance_in_feet INTEGER,
CONSTRAINT pk_track_id
primary key (track_id)

);

drop table track_blocks if EXISTS;
CREATE TABLE track_blocks (
block_id  INTEGER,
track_id INTEGER,
block_distance_in_feet INTEGER ,
CONSTRAINT pk_block_id PRIMARY KEY (block_id)
);

drop table  train if EXISTS;
create table train (
position_block_id integer,
train_id integer not null,
begin_date timestamp,
CONSTRAINT pk_train_id PRIMARY KEY (train_id)
);

PARTITION TABLE train  ON COLUMN train_id;

