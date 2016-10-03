github download django         #install django

apt-get install python-mysqldb #install python-mysql
pip install pymysql ＃mac

django-admin.py startproject mysite #create a project named mysite

python manage.py startapp gscan


python manage.py makemigrations
python manage.py migrate  #create database sql


pip install celery

pip install django-celery

#mac

$ wget http://download.redis.io/releases/redis-3.2.0.tar.gz
$ tar xzf redis-3.2.0.tar.gz
$ cd redis-3.2.0
$ make

#ubutnu
apt-get install redis-server #install redis

pip install redis

python manage.py celery worker -A gscan.tasks --pool=threads -c 30 --loglevel=info
pip install paramiko
pip install dnspython
pip install theadpool
ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9

python manage.py celery worker -A gscan.tasks --pool=threads -c 50  --loglevel=info
