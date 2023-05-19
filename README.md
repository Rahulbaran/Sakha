# [Sakha](https://sakha.pythonanywhere.com)

- A basic social media app that allows users to connect with friends and share content. Users can create and share posts, photos, and videos. They can also follow other users, like posts, and comment on posts. The app is easy to use and can be accessed from any device.
- Flask & JavaScript have been used to develop the app.

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

##### Windows

```bash
$ virtual/scripts/activate.bat
```

##### Mac/Linux

```bash
$ source virtual/bin/activate
```

### Install all the python packages using requirements.text

```bash
(virtual)$ pip install -r requirements.txt
```

### Create a folder of name `Database` inside `Sakha` folder

```bash
(virtual)$ mkdir Sakha/Database
```

### Create a file `.env` in the root folder and put the following inputs in the file which will be used in app configuration

| INPUT NAME                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------- |
| SECRET_KEY                                                                                                                  |
| RECAPTCHA_PRIVATE_KEY (You will have to register your application in Google Recaptcha website to get private & public keys) |
| RECAPTCHA_PUBLIC_KEY                                                                                                        |
| GMAIL_USERNAME                                                                                                              |
| GMAIL_PASSWORD (You will have to generate it using google account)                                                          |

### In the terminal/command prompt setup the following configuration

##### Windows

```bash
> set FLASK_APP=run
> set FLASK_ENV=development

```

##### Mac/Linux

```shell
(virtual)$ export FLASK_APP=run && export FLASK_ENV=development
```

### Activate your python interpreter & create a sqlite database inside _Database_ folder using the following commands

```bash
>>> from Sakha import create_app, db
>>> with create_app().app_context():
        db.create_all()
```

You can also use MYSQL database. To setup the MYSQL Database for the application, put the following configuration inside `.env` file and follow the same path you took for creating sqlite database.

```
SQL_DATABASE_URI = 'mysql+pymysql://<username>:<password>@localhost/sakha'
```

### Exit from the Python Interpreter & run the application

```bash
$ flask run
```

> Checkout the [app](https://sakha.pythonanywhere.com)
