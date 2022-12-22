
source /venv/bin/activate

pip install -r requirements.txt

gunicorn -w 2 -k uvicorn.workers.UvicornWorker app.main:app