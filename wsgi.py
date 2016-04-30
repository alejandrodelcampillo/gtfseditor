from app import *

if __name__ == "__main__":
    application = create_app(os.getenv('FLASK_CONFIG'))
    application.run()