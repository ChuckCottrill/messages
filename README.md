empty (for now)

### Virtual Environment

```
virtualenv --python=python3 env --no-site-packages
source env/bin/activate
# later ...
deactivate
```

### Run server

```
python manage.py runserver 0:8000
```

### Install Redis

```
brew install redis
# or
sudo apt-get install redis-server
```

#### Check Redis working

```
redis-cli -v
redis-cli
PING
PONG
```

```
SET hello "world" EX 10
OK
GET hello
“world”
DEL hello
SET foo "bar" EX 100  # 100 is the number of seconds
OK
TTL foo  # Number of seconds remaining till expiry
97
PERSIST foo
1
TTL foo
-1
GET foo
"bar"
```



### Install

pip intall --user pipenv
pipenv install django djangorestframework requests
pipenv install redis












