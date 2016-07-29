#This file should be run when making changes to the models.py file
#It will delete all your existing data but it will make the migrations
#up to date and make your database clean
#only do this if you know what you are doing

sudo mysql -e "drop database qipr;"
sudo mysql -e "create database qipr character set utf8;"
rm -rf /var/www/qipr-registry/registry/migrations
#Need to Comment out all the urls for the registry app, else the migrations fail
pushd qipr
cp urls.py temp_urls.py
rm urls.py
cp migration_urls.py urls.py
popd
python3 manage.py makemigrations registry
python3 manage.py migrate
pushd qipr
#Adding back the proper urls
rm urls.py
cp temp_urls.py urls.py
rm temp_urls.py
popd

#Uncomment below line if you need a superuser for Admin login:Prompts for email,username,password
#python3 manage.py createsuperuser 
