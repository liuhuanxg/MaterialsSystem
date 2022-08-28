# !/bin/bash
rm -rf  apps/center_library/migrations
rm -rf  apps/home/migrations
rm -rf  apps/local_library/migrations
rm -rf  apps/material_application/migrations
`mysql -uroot -proot123456 -e "drop database materials_system;"`
`mysql -uroot -proot123456 -e "create database materials_system charset=utf8;"`