# **Change the text scale (Win 7,8,10,11)**

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/0) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

An automated process that allows you to change the scale of text in Windows 7,8,10,11.

Relevant for the visually impaired and those.

It is actively used when demonstrating the screen from a high-resolution monitor.


# **Version**

+ Python - works on versions 2 and 3;
+ PowerShell - works on versions 2 and more.


# **Preface**

The example is taken as a basis: https://stackoverflow.com/questions/10365394.


# **Installation**

Make sure you have the following packages installed:
```
pip install os
pip install subprocess
pip install configparser
```
You will also need to use powershell, therefore you need to change the rights to run powershell scripts.


# **Structure**

+ **_resources\config\config.ini_** - contains 'scaling' settings and paths to other files;
+ **_resources\ico\ico.ico_** - basic icon;
+ **_resources\ps1\code.ps1_** - code that changes the size of the text;
+ **_resources\temp\temp_** - a file with a changing 'scaling' status value;
+ **_run.ps1_** - running the file run.py;
+ **_run.py_** - coordinates the 'scaling' status and works with the 'resources' folder.


# **Scaling status**

Size values for text, applications, and other elements:

 - **0** - _100%_ **(default)**;
 - **1** - _125%_;
 - **2** - _150%_;
 - **3** - _175%_;
 - **4** - _200%_;
 - **5** - _225%_


# **Configuration and script launch**

1. Open the file **_resources\config\config.ini_**;
2. Find the variable names 'first' and 'last';
    + **_first_** - the 'scaling' status to return to.
    + **_last_** - the 'scaling' status to change the text size to.
    + Example: 
        ```
        [scaling]
        first = 0
        last = 2

        [temp_setting]
        path = resources/temp
        name = temp

        [ps1_setting]
        path = resources/ps1
        name = code.ps1
        ```
3. Save the settings;
4. Run the file - **_run.py_**

# **Bonus**

If there is a need to install a script shortcut on the taskbar, I recommend that you familiarize yourself with [PS2EXE](https://github.com/MScholtes/PS2EXE).

# **Contributors**

+ [DDoSKudya](https://github.com/DDoSKudya)