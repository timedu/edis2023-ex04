
import json
from os import path

from supp.utils import create_record
from supp.config import mod, TOMBSTONE
from supp.memtable import memtable


def set_record(key, value):
    '''
    Set record
    '''
    mod['db'].flush_memtable()
    memtable[key] = value
    return memtable[key]


def get_record(key):
    '''
    Gets a record
    '''
    record = memtable.get(key)
    if record:
        # 230920 / TiM
        # return record if record[1] != TOMBSTONE else None
        return record if record['value'] != TOMBSTONE else None
        # --
    else:    
        return mod['db'].get_from_sstables(key)


def del_record(key):
    '''
    Marks a record deleted
    '''
    mod['db'].flush_memtable()
    memtable[key] = create_record(key, tombstone=True)
    return memtable[key]


def get_memtable_json():
     '''
     Returns memtable as JSON
     '''
     return json.dumps(memtable, sort_keys=True, indent=4)


def get_sstables_json():
    '''
    Return content of sstable files
    '''
    sstables = []
    for sstable_filename in mod['io'].list_sstables():
        sstables.append({
            'file': path.basename(sstable_filename),
            'sstable': mod['io'].read_sstable(sstable_filename)
        })
    return json.dumps(sstables, sort_keys=True, indent=4) 


def reset_db():
    '''
    Clears memtable and removes all sstable files
    '''
    memtable.clear()
    mod['io'].delete_sstables()
