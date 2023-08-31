echo " BULD START"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo " BULD END"
