# Pytasks
A simple program for making a todo list

## Usage

-l, --list to display your todo list

-a, --add ["str"] to add items to your todo list

-d, --delete [int] to delete items from your todo list

## Examples

```bash
./main.py -a todo "Start learning Rust"
```
This adds "Start learning Rust" to a list called "todo"
```bash
./main.py -d todo 3
```
This will delete the 3rd item from the list called "todo"
