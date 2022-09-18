snowflake_bit_length = 64
timestamp_shift_n = 22
machine_id_shift_n = 12
twitter_timestamp = 1288834974657 / 1000


def append_zeros(bits):
    return '0' * (snowflake_bit_length - len(bits)) + bits


def spaces(bits, space_after=4):
    return ' '.join(bits[i:i+space_after] for i in range(0, len(bits), space_after))


def get_timestamp(sf):
    """
    Shifting bits to get the timestamp
    :param sf: int
        snowflake
    :return: int
        timestamp
    """
    return sf >> timestamp_shift_n


def get_machine_id(sf):
    """
    Creating inverted mask of timestamp and performing bitwise AND on snowflake, shifting bits
    to get rid of machine sequence
    :param sf: int
        snowflake
    :return: int
        machine ID
    """
    return (sf & ~(get_timestamp(sf) << timestamp_shift_n)) >> machine_id_shift_n


def get_machine_sequence(sf):
    """
    Creating inverted mask consisting of timestamp and machine ID and performing bitwise AND on snowflake
    :param sf: int
        snowflake
    :return: int
        machine sequence
    """
    return sf & ~((get_timestamp(sf) << timestamp_shift_n) | (get_machine_id(sf) << machine_id_shift_n))
