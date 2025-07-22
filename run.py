from app import create_app
# 올릴때 지
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

application = create_app()

if __name__ == "__main__":
    application.run(debug=True)