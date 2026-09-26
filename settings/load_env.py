from pathlib import Path
import os
from dotenv import load_dotenv

path = __file__

BASE_DIR = Path(path).resolve().parent.parent
env_path = BASE_DIR/".env"
load_dotenv(dotenv_path=env_path)

SQLALCHEMY_URL=os.getenv('SQLALCHEMY_URL')
SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM= os.getenv('ALGORITHM')

