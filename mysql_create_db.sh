#!/usr/bin/env bash
sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS test_db"
sudo mysql -u root -e "CREATE USER alright IDENTIFIED BY '123'"
sudo mysql -u root -e "GRANT ALL ON test_db.* TO alright@localhost IDENTIFIED BY '123' with grant option"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost'"