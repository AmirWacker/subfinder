#!/usr/bin/python3

import sys
import time
import os
import socket
import whois
import requests
from colorama import init, Fore, Back, Style

if platform.system() != "Linux":
    print (colors.R + "\n You are not using Gnu/Linux Based Os\n" + colors.W)
    sys.exit()

if les(sys.argv) != 2:
    print( Fore.RED + "[Error] Input Error! Usage: python subfinder.py <Domain>")

def main():
    pass

if __name__ == "__main__":
    main()
