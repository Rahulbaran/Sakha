# import os
from Sakha import create_app

app = create_app()

if __name__=="__main__":
    app.run(debug=True, load_dotenv=True, port=5050)