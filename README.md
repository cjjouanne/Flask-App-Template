# Flask APP project template

> by [Charlie Jouanne](https://github.com/cjjouanne)

## Prerequisites:

* `Docker`
* `docker-compose`

## Config app variables

First, run this command on the terminal inside the project directory to create an `.env` file.
```
touch .env
```
Then add this inside the `.env` file
```
SECRET_KEY="a12b9af2eb5a96ch8rl1e1c6771e525b30fa2c8"
SQLALCHEMY_DATABASE_URI="postgresql://myuser:mypassword@postrgres:5432/my_app"

MAIL_SERVER="smtp.gmail.com"
MAIL_PORT=465
MAIL_USERNAME="example@gmail.com"
MAIL_PASSWORD="********"
MAIL_USE_TLS=False
MAIL_USE_SSL=True
```
## Config Database variables

Run this command on terminal to create `.env_db` file.
```
touch .env_db
```
Then add this inside the `.env_db` file
```
POSTGRES_USER="myuser"
POSTGRES_PASSWORD="mypassword"
POSTGRES_DB="my_app"
```
## Settig up Nginx

First, launch the app with this command
```
docker-compose up -d
```
and run
```
docker-compose stop
docker-compose down
```
To stop it. This will create a new folder named `./nginx-conf`. Then add a
`nginx.conf` file inside this folder by running the following commands

```
cd nginx-conf
touch nginx.conf
```
```
server {
	listen 80;
	server_name localhost; #on production use domian.extension www.domain.extension
	location / {
		proxy_pass http://web:5000;
	}
}
```
Now, you are ready to go!

## Run the app!
```
docker-compose up -d
```
Now go to http://localhost:80 and start browsing :)
