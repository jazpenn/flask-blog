部署说明
--------

   15  cd flask-blog/
   24  yum -y groupinstall "Development tools"
   25  sudo vim /etc/sudoers
   26  sudo yum -y groupinstall "Development tools"
   27  sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
   30  mkdir /usr/local/python35
   31  sudo mkdir /usr/local/python35
   32  tar -zxvf Python-3.5.0.tgz 
   34  cd Python-3.5.0
   36  ./configure --prefix=/usr/local/python35
   39  sudo make && sudo make install 
   40  sudo ln -s /usr/local/python35/bin/python3 /usr/bin/python3
   41  sudo ln -s /usr/local/python35/bin/pip3.5  /usr/bin/pip3
   44  sudo yum install -y gcc g++ kernel-devel libffi-devel zlib-devel libjpeg-turbo-devel
   58  sudo yum install -y redis
   61  sudo pip3 install virtualenv
  100  cd flask-blog/
  114  sudo ln -s /usr/local/python35/bin/virtualenv  /usr/bin/virtualenv
  115  virtualenv venv
  116  source venv/bin/activate
  117  pip install -Ur requirements.txt 
  119  sudo yum install -y postgresql
  120  pip install -Ur requirements.txt 
  134  sudo yum install postgresql-server postgresql-contrib
  135  sudo postgresql-setup initdb
  139  pip install -Ur requirements.txt 
  140  sudo systemctl restart postgresql.service
  141  psql
  145  sudo su - postgres
  174  sudo yum install supervisor
  181  python manage.py db
  182  python manage.py db init
  195  python manage.py db upgrade
  207  python manage.py db migrate
  208  python manage.py deploy product
  211  sudo supervisorctl restart FlaskBlog 
