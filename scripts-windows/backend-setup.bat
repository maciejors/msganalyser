cd ..\backend
pip install virtualenv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd ..
uvicorn backend.main:app --log-config=backend/log_config.yml
