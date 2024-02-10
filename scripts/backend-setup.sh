cd backend
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..
uvicorn backend.main:app --log-config=backend/log_config.yml
