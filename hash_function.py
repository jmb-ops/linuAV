#!/usr/bin/python3
# hash_function.py - A simple function that hashes a text file.
from banner import colors, banner

def hashfun():
    print(colors.BOLDCYAN + 'Please enter a file to be hashed and press enter, a hash file','\n'
          'named "hash_file.txt" will be created in the current working directory.','\n'
          'create a copy of the hash file and keep it along with a copy of the baseline' + colors.RESET,'\n'
          ,colors.BOLDGREEN + 'file in a seperate security dongle aka a flash drive. Keep the flash drive off any','\n'
          'internet connected device and viola you have your first ever tamper proof AV','\n'
          'brought to you by a new concept called multifactor security. :), if you feel','\n'
          'there has been a breach AND some tampering simply compare the hash values of the hash' + colors.RESET,'\n'
          ,colors.BOLDYELLOW + 'file from the same directory as linuAV and the hash file from your security dongle.','\n'
          'if they are different you can futher investigate the using the diff command to locate','\n'
          'the tampered file. You could also write the value printed to your screen on a sticky note','\n'
          'or a piece of paper for another reference.' + colors.RESET)
    print()

    while True:

        try:

            human_input = input(colors.BOLDBLUE + 'file: ' + colors.RESET)
            file = open(human_input)
            contents = file.read()
            break

        except:

            print(colors.BOLDRED + 'File not found! please try again.' + colors.RESET)
            
    print('\n',colors.BOLDBLACK + 'Hash value = ' + colors.RESET, colors.BOLDRED + str(len(contents)) + colors.RESET)

    # the below code will write the hash code to a file in the cwd.
    with open('hash_file.txt','w') as file_out:
        file_out.write(str(len(contents)))

    print()
    print(colors.BOLDMAGENTA + 'Hash file creation completed. Press q and create an offsite backup using','\n'
          'a security dongle "flash drive".' + colors.RESET)

def main():
    hashfun()

if __name__ == "__main__":
    main()
