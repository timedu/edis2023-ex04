
'''
EDIS / Assignment 4
'''

if __name__ == '__main__':

    '''
    Parse arguments
    '''

    from  argparse import ArgumentParser

    parser = ArgumentParser(
        description='Assignment 4'
    )

    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 
    parser.add_argument(
        '-i', '--io', choices=['json', 'avro'], default='json',
        help='what io module is used, default: json '
    ) 
    args = vars(parser.parse_args())

    '''
    Import modules
    '''

    from supp.repl import repl

    if args['review'] == '1':
         from todos.review_1 import db 
    elif args['review'] == '2':
         from todos.review_2 import db
    else:
         from todos.your_code import db 

    if args['io'] == 'avro':
        if args['review'] == '1':
             from todos.review_1 import io_avro as io_format
        elif args['review'] == '2':
             from todos.review_2 import io_avro as io_format
        else:
             from todos.your_code import io_avro as io_format
    else:
         from supp import io_json as io_format

    import supp.config
    supp.config.mod['io'] = io_format     
    supp.config.mod['db'] = db     


    '''
    Run REPL
    '''

    todo_folder = 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'
    io_module = 'json' if not args.get('io') else args['io']

    repl(prompt = f'[{todo_folder} / {io_module}] > ')

