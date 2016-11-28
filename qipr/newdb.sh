#This file should be run when making changes to the models.py file
#It will delete all your existing data but it will make the migrations
#up to date and make your database clean
#only do this if you know what you are doing

sudo mysql -u qipr_r_admin_api -p -e "drop database qipr;"
sudo mysql -u qipr_r_admin_api -p -e "create database qipr character set utf8;"
sudo rm -rf /var/www/qipr-registry/registry/migrations
#Need to Comment out all the urls for the registry app, else the migrations fail
pushd qipr
sudo cp urls.py temp_urls.py
sudo rm urls.py
sudo cp migration_urls.py urls.py
popd
sudo python3 manage.py makemigrations registry
sudo python3 manage.py migrate
sudo python3 manage.py loaddata ./registry/fixtures/*
pushd qipr
#Adding back the proper urls
sudo rm urls.py
sudo cp temp_urls.py urls.py
sudo rm temp_urls.py
popd

#Uncomment below line if you need a superuser for Admin login:Prompts for email,username,password
#python3 manage.py createsuperuser 
