# for_contributors directory

this directory is specifically designed for contributors who want to download the raw python file and its dependencies so that they can properly edit it.
To download the dependencies located in `requirements.txt` in a virtual environment that will be created in the parent of this directory, you need to execute either the `.ps1` or `.sh` file, depending on you OS.
If you are on *WINDOWS*, execute `ìnit.ps1`.
If you are on *LINUX*, execute `ìnit.sh`.

again, a virtual environment along with a `.venv` folder will be created in the *PARENT* directory, meaning one directory before this one, where the python file should also be located.

make sure to have *PYTHON3* installed, as it is required for this process.

If everything goes correctly, you will find a `.venv` folder in the parent directory which should include all packages from `requirements.txt`.

Now you can properly run and edit the python file ;)
