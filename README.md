/home/jon/project

[http://167.172.104.241](http://167.172.104.241)

CT Swap.  A buy sell trade market for Cornell Tech

Activate Environment

```sh
source ctswapenv/bin/activate
```

Build Django

```sh
python manage.py makemigrations
python manage.py migrate
```

Restart Gunicorn

```sh
sudo systemctl restart gunicorn
```

Reset Gunicorn

```sh
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
```

Reset Nginx

```sh
sudo nginx -t && sudo systemctl restart nginx
```