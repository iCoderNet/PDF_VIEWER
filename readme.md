## Creating an E-BOOK with .exe extension using Python
In order to open the PDF file through the browser, the program was transferred to the .exe extension

### Required libraries
```shell
pip install flask
pip install pywebview
pip install pyinstaller
```

### Python to EXE file
```shell
pyinstaller --noconfirm --onefile --windowed --add-data "static;static" --icon=icon.ico server.py
```