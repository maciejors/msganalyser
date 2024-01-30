cd backend
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install numpy==1.26.3 pandas==2.2.0 fastapi==0.109.0 uvicorn
uvicorn main:app
