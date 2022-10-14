#! /usr/bin/env python

import argparse
import os.path

parser = argparse.ArgumentParser(description="A simple tool to keep track of tasks.")
parser.add_argument("-a", "--add", help="Add an item to your todo list", type=str)
parser.add_argument("-d", "--delete", help="Delete an item from your todo list", type=int)
parser.add_argument("-l", "--list", help="List Items on your todo list", action='store_true')

args = parser.parse_args()
home_dir = os.path.expanduser('~')

if args.add is not None:
    if os.path.exists(f"{home_dir}/todolist.txt"):
        with open(f"{home_dir}/todolist.txt", "a") as f:
            f.write(f"{args.add}\n")
    else:
        with open(f"{home_dir}/todolist.txt", "w") as f:
            f.write(f"{args.add}\n")

elif args.delete is not None:
    with open(f'{home_dir}/todolist.txt', 'r') as fr:
        lines = fr.readlines()
        ptr = 1

        with open(f'{home_dir}/todolist.txt', 'w') as fw:
            for line in lines:
               
                if ptr != args.delete:
                    fw.write(line)
                ptr += 1
    print(f"Deleting line {args.delete}")

elif args.list is True:
    print("\033[01m\033[32m------TODO------\033[0m")
    with open(f'{home_dir}/todolist.txt', 'r') as fr:
        lines = fr.readlines()
        x =1
        for i in lines:
            print(f"\033[31m{x}\033[0m - ", end="")
            print(i, end="")
            x+=1
    print("\033[01m\033[32m----------------\033[0m")
else:
    print("Need an argument")