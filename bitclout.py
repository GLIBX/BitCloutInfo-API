import os
from main import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port=int(os.environ.get('PORT', 5000)))
