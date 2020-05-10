import sys

def usage():
    print('''USAGE: password_manager [options]
          gen n     Generate a password of length n
          view      View all the entries in the manager
          add       Add Data to the Manager 
          del       Remove entry from the Manager
          help      View Usage
          ''')
    
try:
    if sys.argv[1] == 'help':
        usage()
    else:
      print("Invalid Argument \n")
    usage()
except IndexError:
    print("Invalid Argument \n")
    usage()