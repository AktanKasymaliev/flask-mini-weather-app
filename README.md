# flask-mini-weather-app
Mini one paged weather app based on python/flask

Hello, in the first, you sould clone rep:
* cloning repository:
```
git clone https://github.com/AktanKasymaliev/flask-mini-weather-app.git
```
* Download virtual enviroment:
```
pip install python3-venv 
Activating: python3 -m venv venv
```
* Install all requirements: 
```
pip install -r requirements.txt
```
* Create a file settings.ini on self project level, copy under text, and add your value: 
```
[API]
key = <api key>
```

* Load configurations in bash
```
- export APP_SETTINGS="configurations.settings.DevelopmentConfig"
```
* Start project
```
python main.py
```
