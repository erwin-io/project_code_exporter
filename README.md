# Smart Project Code Exporter

A simple Windows tool that collects important code files from a project folder and combines them into one `.txt` file.

This is useful when you want to:

- Copy your project code into ChatGPT
- Save a clean code reference
- Share selected project files with someone
- Review project files in one place
- Export Ionic, Angular, Node.js, or Python project code

The tool automatically skips heavy or unnecessary folders such as:

```txt
node_modules
.git
dist
build
android
ios
venv
__pycache__
coverage
```

This means it will not export your installed libraries, compiled files, or platform build folders.

---

## What You Need Before Using

Before using the tool, check these:

- [ ] You are using Windows
- [ ] You already have Python installed
- [ ] You have these two files:
  - `export_code.bat`
  - `export_project.py`
- [ ] Both files are inside the same folder

No extra installation is needed.

You do **not** need to install:

```txt
python-docx
npm packages
VS Code extensions
third-party libraries
```

> If you feel you already installed Python before, just give it a try. If the tool opens and works, then you are ready.

---

## Recommended Folder Setup

Create a folder like this:

```txt
C:\Tools\ProjectExporter\
```

Put both files inside:

```txt
C:\Tools\ProjectExporter\
│
├── export_code.bat
└── export_project.py
```

> Important: both files must be in the same folder.

---

## How to Use

### Step 1: Open the Tool

Double-click:

```txt
export_code.bat
```

A black command window will open.

You should see something like:

```txt
Smart Project Code Exporter
TXT Only - No External Libraries

Enter project folder path:
```

---

### Step 2: Enter Your Project Folder Path

Paste the folder path of your project.

Example for an Ionic project:

```txt
C:\Development\smartcopradryer\smart-copra-app
```

Example for a Node.js project:

```txt
C:\Development\my-node-api
```

Example for a Python project:

```txt
C:\Development\my-fastapi-project
```

Then press **Enter**.

---

### Step 3: Wait for Auto-Detection

The tool will try to detect the project type automatically.

For example:

```txt
Auto-detected project type: ionic
```

or:

```txt
Auto-detected project type: node
```

or:

```txt
Auto-detected project type: python
```

After that, it will export the files automatically.

---

## If Auto-Detection Fails

Sometimes the project may not have enough common files for detection.

If that happens, the tool will ask:

```txt
Could not auto-detect project type.

Choose project preset:
[1] Ionic / Angular
[2] Angular
[3] Node.js / Express / NestJS
[4] Python / FastAPI
[5] All common code files
```

Choose the number that matches your project.

Use this guide:

```txt
1 = Ionic mobile/web app
2 = Angular web app
3 = Node.js, Express, NestJS backend
4 = Python, FastAPI, Flask, Django-style project
5 = Unknown project or mixed code files
```

If you are not sure, choose:

```txt
5
```

---

## Where the Output File Is Saved

The exported `.txt` file will be saved inside the project folder you selected.

Example project folder:

```txt
C:\Development\smartcopradryer\smart-copra-app\
```

Example output file:

```txt
smart-copra-app_export_ionic_20260502_010500.txt
```

The file name includes:

- Project name
- Detected project type
- Date and time

This helps avoid overwriting old exports.

---

## What the Exported TXT Contains

The TXT file includes:

- Project folder path
- Detected project type
- Export date and time
- Total files exported
- File list
- Full contents of each included file

Example structure:

```txt
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
```

---

## Project Types Supported

### Ionic / Angular

Usually detected if the project has:

```txt
ionic.config.json
capacitor.config.ts
capacitor.config.json
@ionic/angular
```

It exports files such as:

```txt
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
```

It skips:

```txt
node_modules
android
ios
www
dist
```

---

### Angular

Usually detected if the project has:

```txt
angular.json
@angular/core
@angular/cli
```

It exports files such as:

```txt
src/**/*.ts
src/**/*.html
src/**/*.scss
src/**/*.css
package.json
angular.json
tsconfig.json
environment files
README.md
```

---

### Node.js / Express / NestJS

Usually detected if the project has:

```txt
package.json
```

It exports common backend folders such as:

```txt
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
```

It also includes common config files like:

```txt
package.json
package-lock.json
tsconfig.json
.env
nodemon.json
README.md
```

---

### Python / FastAPI

Usually detected if the project has:

```txt
requirements.txt
pyproject.toml
Pipfile
main.py
venv
.venv
```

It exports folders such as:

```txt
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
```

It also includes:

```txt
requirements.txt
pyproject.toml
.env
README.md
```

---

## Important Notes

### 1. The Tool Exports Text Files Only

This tool does not export to DOCX or PDF.

That is intentional, so users do not need to install extra libraries.

The output is always:

```txt
.txt
```

---

### 2. It Does Not Modify Your Project

The tool only reads your project files and creates a new TXT file.

It does not edit, delete, or move your source code.

---

### 3. Be Careful with `.env` Files

The tool can include `.env` files.

These may contain sensitive information such as:

```txt
API keys
database passwords
tokens
secret keys
Firebase credentials
```

Before sharing the exported TXT file with anyone, check if it contains private credentials.

For ChatGPT use, you may want to replace secrets with:

```txt
YOUR_API_KEY_HERE
YOUR_DATABASE_PASSWORD_HERE
```

---

## Common Problems and Fixes

### Problem: The window says Python is not recognized

Possible message:

```txt
'python' is not recognized as an internal or external command
```

This means Windows cannot find Python.

Checklist:

- [ ] Python is installed
- [ ] Python was added to PATH during installation
- [ ] CMD or the computer was restarted after installation

If you feel Python is already installed, try opening Command Prompt and running:

```bat
python --version
```

If it shows a version number, Python is working.

---

### Problem: I pasted the wrong folder path

Close the window and double-click `export_code.bat` again.

Then paste the correct project folder path.

---

### Problem: It exported too many files

Use a more specific project folder.

For example, instead of exporting:

```txt
C:\Development
```

Use:

```txt
C:\Development\my-project
```

---

### Problem: It exported zero files

Possible causes:

```txt
The selected folder is not the real project folder
The project has unusual file types
The project type was not detected correctly
```

Try running the tool again and choose:

```txt
5 = All common code files
```

when asked.

---

## Best Practice for Copy-Pasting to ChatGPT

After generating the TXT file:

1. Open the exported `.txt` file
2. Copy only the parts needed
3. Avoid sending the entire file if it is very large
4. Remove secret values from `.env` files
5. Tell ChatGPT what you want fixed or reviewed

Example prompt:

```txt
I exported my Ionic project code using Smart Project Code Exporter.
Please review the login/authentication flow and suggest improvements.
```

Another example:

```txt
This is my Node.js API export.
Please help me refactor it into controller, service, route, and config files.
```

---

## Quick Start Summary

```txt
1. Put export_code.bat and export_project.py in one folder
2. Double-click export_code.bat
3. Paste your project folder path
4. Press Enter
5. Wait for export to finish
6. Open the generated .txt file inside your project folder
7. Copy and use it as reference
```

---

## Suggested Tool Name

Recommended name:

```txt
Smart Project Code Exporter
```

Short name:

```txt
Code Exporter TXT
```

For non-technical users, **Smart Project Code Exporter** is recommended because it clearly explains what the tool does.
