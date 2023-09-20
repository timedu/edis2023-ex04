
import traceback

from supp.utils import create_record
from supp import driver

try:
    import readline
except:
    pass 


def repl(prompt):

    global memtable

    while True:

        try:
            user_input = input(prompt)

        except EOFError:
            print('')
            break        

        if not user_input.strip():
            continue

        input_strings = user_input.split()
        command = input_strings[0].lower()

        try:

            if len(input_strings) == 1:

                if command in ('exit', 'quit'):
                    break

                if command == 'memtable':

                    print(driver.get_memtable_json())
                    continue 

                if command == 'sstables':

                    print(driver.get_sstables_json())
                    continue 

                if command == 'reset':

                    driver.reset_db()
                    continue 

            if len(input_strings) == 2:

                assert all(char.isdigit() for char in input_strings[1])
                key = int(input_strings[1])

                if command == 'set':

                    print(driver.set_record(key, create_record(key)))
                    continue

                if command == 'del':

                    print(driver.del_record(key))
                    continue

                if command == 'get':

                    print(driver.get_record(key))
                    continue
                
            raise AssertionError

        except AssertionError:
            print('Usage: { {set|get|del} <int> } |  memtable|sstables|reset | exit|quit }')

        except Exception as err:
            print(err)
            traceback.print_exc()
