from datetime import datetime
import argparse

import snowflake


def check_bit_length(value):
    if not value.isnumeric():
        raise argparse.ArgumentTypeError(f'{value} is not a positive int number')
    ivalue = int(value)
    if ivalue.bit_length() > snowflake.snowflake_bit_length:
        raise argparse.ArgumentTypeError(f'{value} has {ivalue.bit_length()} bits, '
                                         f'but max {snowflake.snowflake_bit_length} is allowed.')
    return ivalue


parser = argparse.ArgumentParser(description='Twitter Snowflake Reverser')
parser.add_argument('snowflake', type=check_bit_length)
args = parser.parse_args()

sf = args.snowflake
snowflake_binary = snowflake.append_zeros(f'{sf:b}')

timestamp = snowflake.get_timestamp(sf)
machine_id = snowflake.get_machine_id(sf)
machine_sequence = snowflake.get_machine_sequence(sf)

output = f'=================\n' \
         f'In binary (N of bits is {snowflake.snowflake_bit_length})\n' \
         f'{snowflake.spaces(snowflake_binary)}\n' \
         f'=================\n' \
         f'Timestamp (raw): {timestamp}\n' \
         f'Twitter Datetime (in local timezone): ' \
         f'{datetime.fromtimestamp(snowflake.twitter_timestamp + timestamp / 1000)} \n' \
         f'Machine ID: {machine_id}\n' \
         f'Machine Sequence: {machine_sequence}'
print(output)
