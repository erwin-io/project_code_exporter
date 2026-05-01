Smart Project Code Exporter
User Guide
What This Tool Does

Smart Project Code Exporter is a simple Windows tool that collects important code files from a project folder and combines them into one .txt file.

This is useful when you want to:

Copy your project code into ChatGPT
Save a clean code reference
Share selected project files with someone
Review project files in one place
Export Ionic, Angular, Node.js, or Python project code

It automatically skips heavy or unnecessary folders like:

node_modules
.git
dist
build
android
ios
venv
__pycache__
coverage

So it will not export your libraries, compiled files, or platform build folders.

What You Need Before Using

Before using the tool, check these:

[ ] You are using Windows
[ ] You already have Python installed
[ ] You have the two files:
    - export_code.bat
    - export_project.py
[ ] Both files are inside the same folder

No extra installation is needed.

You do not need to install:

python-docx
npm packages
VS Code extensions
third-party libraries

If you feel you already installed Python before, just give it a try. If the tool opens and works, then you are ready.

Recommended Folder Setup

Create a folder like this:

C:\Tools\ProjectExporter\

Put both files inside:

C:\Tools\ProjectExporter\
│
├── export_code.bat
└── export_project.py

Important: both files must be in the same folder.

How to Use
Step 1: Open the Tool

Double-click:

export_code.bat

A black command window will open.

You should see something like:

Smart Project Code Exporter
TXT Only - No External Libraries

Enter project folder path:
Step 2: Enter Your Project Folder Path

Paste the folder path of your project.

Example for an Ionic project:

C:\Development\smartcopradryer\smart-copra-app

Example for a Node.js project:

C:\Development\my-node-api

Example for a Python project:

C:\Development\my-fastapi-project

Then press Enter.

Step 3: Wait for Auto-Detection

The tool will try to detect the project type automatically.

For example:

Auto-detected project type: ionic

or:

Auto-detected project type: node

or:

Auto-detected project type: python

Then it will export the files automatically.

If Auto-Detection Fails

Sometimes the project may not have enough common files for detection.

If that happens, the tool will ask:

Could not auto-detect project type.

Choose project preset:
[1] Ionic / Angular
[2] Angular
[3] Node.js / Express / NestJS
[4] Python / FastAPI
[5] All common code files

Choose the number that matches your project.

Use this guide:

1 = Ionic mobile/web app
2 = Angular web app
3 = Node.js, Express, NestJS backend
4 = Python, FastAPI, Flask, Django-style project
5 = Unknown project or mixed code files

If you are not sure, choose:

5
Where the Output File Is Saved

The exported TXT file will be saved inside the project folder you selected.

Example:

C:\Development\smartcopradryer\smart-copra-app\

The output file will look like:

smart-copra-app_export_ionic_20260502_010500.txt

The file name includes:

project name
detected project type
date and time

This helps avoid overwriting old exports.

What the Exported TXT Contains

The TXT file includes:

Project folder path
Detected project type
Export date and time
Total files exported
File list
Full contents of each included file

Example structure:

==========================================================================================
PROJECT CODE EXPORT
==========================================================================================
Source Folder : C:\Development\my-project
Preset        : ionic
Exported At   : 2026-05-02 01:05:00
Total Files   : 42
==========================================================================================

FILE LIST
------------------------------------------------------------------------------------------
package.json
angular.json
src/app/app.component.ts
src/app/app.component.html

==========================================================================================
FILE CONTENTS
==========================================================================================

==========================================================================================
FILE: package.json
==========================================================================================
{ ...code here... }
Project Types Supported
Ionic / Angular

Usually detected if the project has:

ionic.config.json
capacitor.config.ts
capacitor.config.json
@ionic/angular

It exports files such as:

src/**/*.ts
src/**/*.html
src/**/*.scss
src/**/*.css
src/**/*.json
package.json
angular.json
ionic.config.json
capacitor.config.ts
tsconfig.json
environment files
README.md

It skips:

node_modules
android
ios
www
dist
Angular

Usually detected if the project has:

angular.json
@angular/core
@angular/cli

It exports files such as:

src/**/*.ts
src/**/*.html
src/**/*.scss
src/**/*.css
package.json
angular.json
tsconfig.json
environment files
README.md
Node.js / Express / NestJS

Usually detected if the project has:

package.json

It exports common backend folders such as:

src
routes
controllers
services
models
config
middleware
utils
database
db
public
views

It also includes common config files like:

package.json
package-lock.json
tsconfig.json
.env
nodemon.json
README.md
Python / FastAPI

Usually detected if the project has:

requirements.txt
pyproject.toml
Pipfile
main.py
venv
.venv

It exports folders such as:

app
src
api
services
models
routes
routers
config
utils
templates

It also includes:

requirements.txt
pyproject.toml
.env
README.md
Important Notes
1. The Tool Exports Text Files Only

This tool does not export to DOCX or PDF.

That is intentional, so users do not need to install extra libraries.

The output is always:

.txt
2. It Does Not Modify Your Project

The tool only reads your project files and creates a new TXT file.

It does not edit, delete, or move your source code.

3. Be Careful with .env Files

The tool can include .env files.

These may contain sensitive information such as:

API keys
database passwords
tokens
secret keys
Firebase credentials

Before sharing the exported TXT file with anyone, check if it contains private credentials.

For ChatGPT use, you may want to replace secrets with:

YOUR_API_KEY_HERE
YOUR_DATABASE_PASSWORD_HERE
Common Problems and Fixes
Problem: The window says Python is not recognized

Possible message:

'python' is not recognized as an internal or external command

This means Windows cannot find Python.

Checklist:

[ ] Python is installed
[ ] Python was added to PATH during installation
[ ] CMD or the computer was restarted after installation

If you feel Python is already installed, try opening Command Prompt and running:

python --version

If it shows a version number, Python is working.

Problem: I pasted the wrong folder path

Close the window and double-click export_code.bat again.

Then paste the correct project folder path.

Problem: It exported too many files

Use a more specific project folder.

For example, instead of exporting:

C:\Development

Use:

C:\Development\my-project
Problem: It exported zero files

Possible causes:

The selected folder is not the real project folder
The project has unusual file types
The project type was not detected correctly

Try running the tool again and choose:

5 = All common code files

when asked.

Best Practice for Copy-Pasting to ChatGPT

After generating the TXT file:

1. Open the exported .txt file
2. Copy only the parts needed
3. Avoid sending the entire file if it is very large
4. Remove secret values from .env files
5. Tell ChatGPT what you want fixed or reviewed

Example prompt:

I exported my Ionic project code using Smart Project Code Exporter.
Please review the login/authentication flow and suggest improvements.

Another example:

This is my Node.js API export.
Please help me refactor it into controller, service, route, and config files.
Quick Start Summary
1. Put export_code.bat and export_project.py in one folder
2. Double-click export_code.bat
3. Paste your project folder path
4. Press Enter
5. Wait for export to finish
6. Open the generated .txt file inside your project folder
7. Copy and use it as reference