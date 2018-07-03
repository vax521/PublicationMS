# PublicationMS
--Requirements
  1.Flask==0.10.1
  2.Flask-Mail==0.9.1
  3.Jinja2==2.7.3
  4.SPARQLWrapper==1.8.2
  5.pyecharts==0.5.5
  6.pyecharts-javascripthon==0.0.6
  7.pyecharts-jupyter-installer==0.0.3

整体方案：

        1.开发问题：
                1. 采用python技术栈，既支持http协议，也可支持脚本任务。
                2. 技术栈：Flask(HTTP协议) + jinja2(模板渲染)+ SqlAlchemy(DB adapter) + echarts(绘图)+sparql(查询引擎)
                4. 以上技术栈全平台兼容，无需再做cache路径配置 和 多平台兼容性问题。

        2.启动方法：
            启动web server
            runServer.py