# event-project
## SSH:
ssh root@IP

## Activate ENV
source django_env/bin/activate

## RUN for Testing:
- http://0.0.0.0:8000/
- 
## pm2 Start:
- pm2 start echosystem.config.json

## STOP pm2:
- pm2 stop python

git pull
sudo reboot
npm run build
rename package.json (port)
sudo ufw allow (port)
npm run start & disown


server run:

https://github.com/sunilmalhotra1/django_with_pm2


## echosystem.config.json

{
"apps": [{
"name": "djnago_with_pm2",
"script": "manage.py",
"args": ["runserver", "0.0.0.0:8000"],
"exec_mode": "fork",
"instances": "1",
"wait_ready": true,
"autorestart": false,
"max_restarts": 5,
"interpreter" : "python"
}]
}



## Steps:
Install Node from given link https://nodejs.org/en/download/
Install npm using this command in command prompt / terminal npm install npm@latest -g reference : https://www.npmjs.com/get-npm
Run this command for execute django application non stop on server machine pm2 start echosystem.config.json
Description of echosystem.config.json

{ "apps": [{ "name": "djnago_with_pm2", "script": "manage.py", "args": ["runserver", "127.0.0.1:8000"], "exec_mode": "fork", "instances": "1", "wait_ready": true, "autorestart": false, "max_restarts": 5, "interpreter" : "python" }] }

If we have to change the port number of our django application, then we can the port no in args attribute of echosystem.config.json file.
After done the changes in echosystem.config.json file, stop the server using pm2 command like this:
pm2 stop all // this command will stop all server.
pm2 stop 0 // if you know the pm2 id then execute command like this.
pm2 start echosystem.config.json // again start the django application.
