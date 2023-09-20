
from datetime import datetime
from os import path

from supp.config import TOMBSTONE, get_data_dir


def create_record(key, tombstone=False):
    '''
    Create record value
    '''
    dt = datetime.now()
    value = dt.strftime('%c') if not tombstone else TOMBSTONE
    timestamp = dt.timestamp()
    return {'key': key, 'value': value, 'timestamp': timestamp}


def create_sstable_filename(suffix='json'):
    '''
    Creates filename for new sstable
    '''
    timestamp = datetime.now().timestamp()
    return path.join(get_data_dir(), f'sstable-{timestamp}.{suffix}')


def get_sstable_pattern(suffix='json'):
    '''
    Returns pattern to get list of sstable files
    '''
    return path.join(get_data_dir(),f'sstable-*.{suffix}')
