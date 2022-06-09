# event-project
## SSH:
ssh root@IP

## Activate ENV
source django_env/bin/activate

## RUN for Testing:
- http://0.0.0.0:8000/
- 
## pm2 Start:
- 

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


