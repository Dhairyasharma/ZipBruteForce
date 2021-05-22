import argparse
import zipfile
import sys
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('Zipfile', help='Path to zip file')
parser.add_argument('Passwordfile', help='Path to Password file')
group = parser.add_mutually_exclusive_group()
group.add_argument('-v' ,'--verbosity', help='Increase verbosity', action='store_true')
group.add_argument('-q','--quiet' ,action='store_true')

args = parser.parse_args()


zip_file = args.Zipfile
password_file = args.Passwordfile

zip_file = zipfile.ZipFile(zip_file)
Total = len(list(open(password_file,'rb')))
if args.verbosity:

    print('Total Password to Check: ',Total)

    with open(password_file ,'rb') as wordlist:
        for word in wordlist:
            print('[>]Checking password :',word.strip().decode())
            try:
                zip_file.extractall(pwd=word.strip())
                password = word.decode()
                break
            except:
                continue
    if password:
        print('[+] Password Found ',password)
        exit(0)
    else:
        print('[-] Try another wordlist')
        exit(0)
elif args.quiet:
    with open(password_file,'rb') as wordlist:
        for word in wordlist:
            try:
                zip_file.extractall(pwd=word.strip())
                password = word.decode()
                break
            except:
                continue
        if password:
            print('[+] Password = ',password)
            exit(0)
        else:
            print('[-] Password not found in given Wordlist')
            exit(0)

else:
    print('[+] Total Password to Check: ',Total)

    with open(password_file,'rb') as wordlist:
        for word in tqdm(wordlist,total=Total,unit='word'):
            try:
                zip_file.extractall(pwd=word.strip())
                password = word.decode()
                break
            except:
                continue
        if password:
            print('[+] Password of zip file is: ',password)
            exit(0)
        else:
            print('[-] Try another wordlist')
            exit(0)









