# Pytasks
### A simple program for making a todo list
Pytask supports multiple lists that can read and write from. You can display them in your terminal a quick reminder on what needs to get done.

## Usage

-l, --list to display your todo list

-a, --add ["str"] to add items to your todo list

-r, --remove [int] to delete items from your todo list

## Examples

This adds "Start learning Rust" to a list called "todo". If "todo" hasn't been created yet it will create it for you.

```bash
./main.py -a todo "Start learning Rust"
```
This will delete the 3rd item from the list called "todo"
```bash
./main.py -r todo 3
```
To display your list use the -d or --display option with the name of the list you want to display.
```bash
./main.py -d todo
```
