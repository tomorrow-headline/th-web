# Tomorrow Headline

## Intro

This document tell you how to deploy this project.

## Features

The main function of this project is written in `Python3` (version 3.6.5) depends on `Django` (version 2.1) and `djangorestframework` (version v3.8.2).

## Prerequisites

### Hardware and System

We recommend that you use the Linux operating system. The recommended kernel version is higher than 4.3.

It is recommended that you use at least 1 core CPU and more than 512MB of memory.

### Set up the Environment

To deploy this project, you need [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/).

After installing python and pip, it is recommended that you use [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) to manage your different python environments. You can use the following command to install virtualenv.

    pip3 install virtualenv

Now you can use the following command to generate your deployment environment:

    git clone https://github.com/newcoderlife/web.git
    cd web
    virtualenv .env --python=python3

Use the next command to activate your python virtual environment:

    source .env/bin/activate

You also need a http server. We recommend that you use [Nginx](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/).

## Deploy

### Install Dependency Package

    pip install django djangorestframework gunicorn

### Configure Django Project

Start by locating the `ALLOWED_HOSTS` directive. This defines a list of the server's addresses or domain names may be used to connect to the Django instance. Any incoming requests with a Host header that is not in this list will raise an exception.

Open setting file

    nano ./tomorrow_headline/settings.py

Edit `ALLOWED_HOSTS`

    ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . ., 'localhost']

Next, move down to the bottom of the file and add a setting indicating where the static files should be placed.

    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

Save and close the file when you are finished.

### Completing Initial Project Setup

Now, we can migrate the initial database schema to database using the management script:

    ./manage.py makemigrations
    ./manage.py migrate

Create an administrative user for the project by typing:

    ./manage.py createsuperuser

We can collect all of the static content into the directory location we configured by typing:

    ./manage.py collectstatic

### Configure Firewall

If you followed the initial server setup guide, you should have a UFW firewall protecting your server. In order to test the development server, we'll have to allow access to the port we'll be using.

Create an exception for port 8000 by typing:

    sudo ufw allow 'Nginx Full'

### Creating systemd Socket and Service Files for Gunicorn

Start by creating and opening a systemd socket file for Gunicorn with sudo privileges:

    sudo nano /etc/systemd/system/gunicorn.socket

Inside, we will create a `[Unit]` section to describe the socket, a `[Socket]` section to define the socket location, and an `[Install]` section to make sure the socket is created at the right time:

    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target

Save and close the file when you are finished.

Next, create and open a systemd service file for Gunicorn with sudo privileges in your text editor.

    sudo nano /etc/systemd/system/gunicorn.service

Add the following code to your file:

    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target

    [Service]
    User=root
    Group=root
    WorkingDirectory=/path/to/your/project
    ExecStart=/path/to/your/project/.env/bin/gunicorn \
              --access-logfile - \
              --workers 3 \
              --bind unix:/run/gunicorn.sock \
              tomorrow_headline.wsgi:application

    [Install]
    WantedBy=multi-user.target

Save and close it now.

We can now start and enable the Gunicorn socket. This will create the socket file at `/run/gunicorn.sock` now and at boot. When a connection is made to that socket, systemd will automatically start the `gunicorn.service` to handle it:

    sudo systemctl start gunicorn.socket
    sudo systemctl enable gunicorn.socket

### Configure Nginx to Proxy Pass to Gunicorn

Start by creating and opening a new server block in Nginx's sites-available directory:

    sudo nano /etc/nginx/sites-available/tomorrow_headline

Add the following code to your file:

    server {
        listen 80;
        server_name server_domain_or_IP;

        location = /favicon.ico { access_log off;   log_not_found off; }
        location /static/ {
            root /path/to/your/project;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
        }
    }

Save and close the file when you are finished. Now, we can enable the file by linking it to the `sites-enabled` directory:

    sudo ln -s /etc/nginx/sites-available/tomorrow_headline /etc/nginx/sites-enabled

Test your Nginx configuration for syntax errors by typing:

    sudo nginx -t

If no errors are reported, go ahead and restart Nginx by typing:

    sudo systemctl restart nginx

You should now be able to go to your server's domain or IP address to view your application.

## Thanks

**Justin Ellingwood** [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)