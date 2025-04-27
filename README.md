# MySQL Gene Addition
Repository for the subject "Sistemas de Información Clínica" (UPNA). The following is for educational purpose only.

# Installation
Download the `mysql_db` directory and run the `gui.py` file. For modifications, `mysql.library` external library is required. For its installation, run in terminal the following:
```
pip install mysql-connector-python
```
If an executable file is prefered, the `pyinstaller` addon can be used. For its installation (if not already), run in terminal:
```
pip install pyinstaller
```
Then run:
```
pyinstaller --onefile gui.py
```
**Warning**: `mysql.library` is depended on several mysql resources that could or could not be in the desired machine. If not, download them (most of the cases in Linux derived OS).
