import os
from backend import create_server
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    # backend
    app = create_server()
    app.run(host=os.getenv('HOST'),
            port=os.getenv('PORT'),
            debug=True)

# express api endpoints
# orm sql
# unit tests (ci)
# server: integration test

# docker
# github actions

