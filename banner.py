#!/usr/bin/python3


class colors:
    BOLDBLACK = '\033[1;30m'
    BOLDRED = '\033[1;31m'
    BOLDGREEN = '\033[1;32m'
    BOLDYELLOW = '\033[1;33m'
    BOLDBLUE = '\033[1;34m'
    BOLDMAGENTA = '\033[1;35m'
    BOLDCYAN = '\033[1;36m'
    BOLDWHITE = '\033[1;37m'
    RESET = '\033[0m'

def banner():
    print(colors.BOLDBLACK + '====================================================' + colors.RESET)
    print(colors.BOLDYELLOW + '                                    _   +          +   ' + colors.RESET)
    print(colors.BOLDGREEN + '    / /     ++  ___                / \   \ \    / /    ' + colors.RESET)
    print(colors.BOLDBLUE + '   / /     / / /   | / / / // /   / * \   \ \  / /    ' + colors.RESET)
    print(colors.BOLDBLACK + '  / /     / / / /| |/ / / // /   / /_\ \   \ \/ /     ' + colors.RESET)
    print(colors.BOLDMAGENTA + ' / /___  / / / / | | / / // /   / _____ \   \  /      ' + colors.RESET)
    print(colors.BOLDCYAN + '/_____  / / / /  |__/ |____/   / /     \ \   \/       ' + colors.RESET)
    print(colors.BOLDYELLOW + '====================================================' + colors.RESET)
    print(colors.BOLDGREEN + '(Immortalized By: Jason Bain, currenty employable if impressed.)' + colors.RESET)
    print(colors.BOLDBLACK + '(Help menu and instructions written by Darlene S.)' + colors.RESET,'\n')


def main():
    banner()

if __name__ == "__main__":
    main()
