#!/usr/bin/env bash
#/usr/bin/env bash

admin_user="admin"
admin_pwd="password"
admin_email="$admin_user@example.com"



apt-get update
apt-get -y upgrade

# Installation de python et Django
apt-get install -y python3.5
apt-get install -y python3-pip
pip3 install --upgrade pip
pip3 install django
pip3 install psycopg2
pip3 install python-form

apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

pip3 install scipy
pip3 install pandas
pip3 install scikit-learn
# Installation de mysql server



apt-get update


apt-get install python-dev python-pip -q -y

export DEBIAN_FRONTEND=noninteractive
echo "installing over mysql server"

apt-get -q -y install mysql-server
service mysql start
#without pip3 it will not going to work for python3
echo "installing python mysql db"

#sudo pip3 install mysqlclient fails with mysql_config not found

apt-get -y install libmysqlclient-dev
#without pip3 it will not going to work for python3
pip3 install mysqlclient

echo "installing python mysql db done"
mysql -uroot -e "CREATE DATABASE myproject CHARACTER SET utf8 COLLATE utf8_general_ci"
mysql -uroot -e "CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost'"
mysql -uroot -e "FLUSH PRIVILEGES"

echo "mysql installation done"
