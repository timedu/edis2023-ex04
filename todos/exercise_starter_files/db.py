
from supp.config import TOMBSTONE, MEMTABLE_TRESHOLD, SSTABLES_TRESHOLD
from supp.config import mod # mod['io'] refers to io_json or io_avro
from supp.memtable import memtable


def get_from_sstables(key):
    '''
    Gets a record from sstable files
    '''

    # ...

    return None


def compact_sstables():
    '''
    Compacts sstables to a single file, if necessary  
    '''
    sstable_filenames = mod['io'].list_sstables()

    if len(sstable_filenames) < SSTABLES_TRESHOLD:
        return

    # ...



def flush_memtable():
    '''
    Flushes memtable to a new sstable file, if necessary
    '''
    global memtable

    if len(memtable) >= MEMTABLE_TRESHOLD:

        # ...
        
        pass    
