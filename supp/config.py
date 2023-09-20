
from os import path
import sys

TOMBSTONE = '-TOMBSTONE-'
MEMTABLE_TRESHOLD = 5
SSTABLES_TRESHOLD = 3

def get_data_dir():
    main_path = sys.modules['__main__'].__file__
    return path.join( path.dirname(main_path), 'data' )  

'''
set by main based on arguments:
- mod['io'] <- supp.io_json or todos.<todo_folder>.io_avro
'''

mod = {}

