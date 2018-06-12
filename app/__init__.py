from flask import Flask

app = Flask(__name__)
#读取配置文件信息
app.config.from_object('config')
from app import views
from app import retrieval
