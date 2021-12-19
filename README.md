# Sakha

It is social network web application which has been created by me with ❤ for people. It is a flask application and I spent a lot of time to create this.
You can run this application locally after going through the steps mentioned below.

## How to run it locally

### Clone the project

```bash
$ git clone https://github.com/Rahulbaran/Sakha.git
```

### Create the virtual environment

```bash
$ python3 -m venv virtual
```

### Activate the virtual environment

#### Windows

```bash
$ virtual/scripts/activate.bat
```

#### Mac/Linux

```bash
$ virtual/Scripts/activate
```

### Install all the python packages using requirements.text

```bash
(virtual)$ pip install -r requirements.txt
```

### Create a folder of name `Database` inside `Sakha` folder

```bash
(virtual)$ mkdir Database
```

### In the terminal/command prompt setup the following

#### Windows

```bash
> set FLASK_APP=run
> set FLASK_ENV=development

```

#### Mac/Linux

```shell
(virtual)$ export FLASK_APP=run && export FLASK_ENV=development
```

### Activate your python interpretor & import

### Run the application

```bash
$ flask run
```
