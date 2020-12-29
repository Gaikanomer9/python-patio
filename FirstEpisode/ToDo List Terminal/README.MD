## ToDo list in the terminal

Starting the project:

```
cd FirstEpisode/ToDo\ List\ Terminal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After that you can invoke the command line interface via python module
```
python todo.py --help
```

## Packaging terminal app
In order to make the app available in the system anywhere in the terminal, 
we would need to create a binary executable file and permanently add it to
our system PATH

```
# Creating new binary executable
pyinstaller todo.py
# Creating a new path for binary executables
mkdir ~/bin
cp -r dist/todo ~/bin/todo
export PATH=$PATH":$HOME/bin/todo"
```


Put `export PATH=$PATH":$HOME/bin/todo"` in ~/.zshrc or another shell you are using
