#! /usr/bin/env python

import argparse
import os.path

parser = argparse.ArgumentParser(description="A simple tool to keep track of tasks.")
parser.add_argument("-a", "--add", help="Add an item to your todo list", metavar=("\"List name\"", "\"Item\""), type=str, nargs=2)
parser.add_argument("-r", "--remove", help="Delete an item from your todo list", metavar=("\"List name\"", "\"Item number\""), type=str, nargs=2)
parser.add_argument("-l", "--list", help="Lists your lists", action="store_true")
parser.add_argument("-d", "--display", help="Creates a new list", metavar="\"List name\"", type=str)

args = parser.parse_args()
list_path = f"{os.path.expanduser('~')}/.pytasks"

def add(args):
    if os.path.exists(f"{list_path}/{args.add[0]}.txt"):
        with open(f"{list_path}/{args.add[0]}.txt", "a") as f:
            f.write(f"{args.add[1]}\n")
    else:
        with open(f"{list_path}/{args.add[0]}.txt", "w") as f:
            f.write(f"{args.add[1]}\n")

def remove(args):
    with open(f"{list_path}/{args.remove[0]}.txt", 'r+') as fp:

        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()

        for number, line in enumerate(lines):
            if number not in [int(args.remove[1])-1]:
                fp.write(line)
        
        print(f"Deleting line {args.remove[1]}")

def display(args):

    print(f"\033[01m\033[32m------{args.display}------\033[0m")

    with open(f'{list_path}/{args.display}.txt', 'r') as fr:
        lines = fr.readlines()
        x =1
        for i in lines:
            print(f"\033[31m{x}\033[0m - ", end="")
            print(i, end="")
            x+=1

    print("\033[01m\033[32m----------------\033[0m")        

def parseArgs(args): 
    if args.add is not None:
        add(args)
        
    elif args.remove is not None:
        remove(args)
    
    elif args.list:
        print(*os.listdir(list_path), sep="\n")

    elif args.display is not None:
        display(args)
        
    else:
        print("Needs an argument")


if os.path.exists(list_path) != True:
    os.mkdir(list_path)

parseArgs(args)