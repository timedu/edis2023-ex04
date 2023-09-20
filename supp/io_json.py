
from os import remove 
from glob import glob
import json

from supp.utils import create_sstable_filename, get_sstable_pattern


def list_sstables():
    '''
    Lists all sstables (path names)
    '''
    return glob(get_sstable_pattern('json'))


def read_sstable(filename):
    '''
    Reads sstable from file
    '''
    fin = open(filename, 'rt' )
    sstable_json = fin.read()
    fin.close()

    sstable = {}
    for record in json.loads(sstable_json):
        sstable[record['key']] = record

    return sstable


def write_sstable(memtable):
    '''
    Writes memtable to sstable in file
    '''
    filename = create_sstable_filename('json')
    memtable_json = json.dumps(list(memtable.values()), indent=4)
    fout = open(filename, 'wt' )
    fout.write(memtable_json)
    fout.close()


def delete_sstables():
    '''
    Deletes all sstable files
    '''    
    for filename in list_sstables():
        remove(filename)
