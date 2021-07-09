from weather import app 
from weather.urls import urlpatterns

@app.route(urlpatterns['main_page'])
def hello_world():
    return "<p>Hello, World!</p>"