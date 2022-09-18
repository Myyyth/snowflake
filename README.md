# Twitter Snowflake Reverser
![](https://upload.wikimedia.org/wikipedia/commons/5/5a/Snowflake-identifier.png)
Splits an original [Twitter snowflake ID](https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake) into timestamp, machine instance, and machine sequence. 

## Usage
```
$ python snowflake-reverser.py --help
usage: snowflake-reverser.py [-h] snowflake

Twitter Snowflake Reverser

positional arguments:
  snowflake

options:
  -h, --help  show this help message and exit
```
```
$ python snowflake-reverser.py 1571337302416437252
=================
In binary (N of bits is 64)
0001 0101 1100 1110 1000 0010 1111 0011 1000 0100 1101 1010 0011 0000 0000 0100
=================
Timestamp (raw): 374636006931
Twitter Datetime (in local timezone): 2022-09-18 06:16:21.588000
Machine ID: 419
Machine Sequence: 4
```