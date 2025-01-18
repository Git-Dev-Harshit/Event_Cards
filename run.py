import os
from dotenv import load_dotenv
from app import create_app
from app.utils.logger import logger

load_dotenv()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host=os.getenv('HOST'), port=os.getenv('PORT'))
    logger.info(f"Server started successfully and running on port {os.getenv('PORT')}")
