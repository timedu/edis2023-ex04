
from os import path, remove 
from glob import glob

import avro.schema # pyright: ignore
from avro.datafile import DataFileReader, DataFileWriter # pyright: ignore
from avro.io import DatumReader, DatumWriter # pyright: ignore

from supp.config import get_data_dir
from supp.utils import create_sstable_filename, get_sstable_pattern


def list_sstables():
    '''
    Lists all sstables (path names)
    '''
    return glob(get_sstable_pattern('avro'))


def delete_sstables():
    '''
    Deletes all sstable files
    '''    
    for filename in list_sstables():
        remove(filename)


# ------------
# todo (start)


def read_sstable(filename):
    '''
    Reads sstable from avro file
    '''

    return {}


def write_sstable(memtable):
    '''
    Writes memtable to sstable in avro file
    '''

    pass


# todo (end)
# ------------
