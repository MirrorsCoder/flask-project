import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os
from flask import Flask, render_template, send_from_directory, request, jsonify
app = Flask(__name__)

DATABASE_URI = "C:/Users/Administrator/PycharmProjects/flask4/database.db"


UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
ALLOWED_EXTENSIONS = set(['xls', 'xlsx', 'csv'])  # 允许上传的文件后缀







@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/show/')
def show_pages():
    # 创建表格、插入数据
    # @app.before_first_request
    # 连接
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    sql = "SELECT rowid as RowNumber, * FROM database "
    # 创建表
    c.execute(sql)
    u = c.fetchall()
    # print(u)
    conn.commit()
    # 关闭
    conn.close()
    return render_template('show.html',u=u,)

@app.route('/show1')
def show_pages1():
    df = pd.read_csv('C:/Users/Administrator/PycharmProjects/flask4/database.csv')
    plt.hist(df['入学年'], bins=range(2015, 2019), edgecolor='black')

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.hist(df['入学年'], bins=range(2015, 2019), edgecolor='black')

    plt.title('入学年份统计（2015~2018）')
    plt.xlabel('入学年份')
    plt.ylabel('人数')
    # plt.show()
    plt.savefig("image/year.png")

    # 创建表格、插入数据
    # @app.before_first_request
    # 连接
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    sql = "SELECT rowid as RowNumber, * FROM database order by 入学年"
    # 创建表
    c.execute(sql)
    u = c.fetchall()
    # conn.commit()
    # 关闭
    conn.close()
    return render_template('show1.html',u=u,)

@app.route('/show2')
def show_pages2():
    # 创建表格、插入数据
    # @app.before_first_request
    # 连接
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    sql = "SELECT rowid as RowNumber, * FROM database order by 大学 "
    # 创建表
    c.execute(sql)
    u = c.fetchall()
    # conn.commit()
    # 关闭
    conn.close()
    return render_template('show2.html',u=u,)

@app.route('/show3')
def show_pages3():
    # 创建表格、插入数据
    # @app.before_first_request
    # 连接
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    sql = "SELECT rowid as RowNumber, * FROM database order by J值 "
    # 创建表
    c.execute(sql)
    u = c.fetchall()
    # conn.commit()
    # 关闭
    conn.close()
    return render_template('show3.html',u=u,)


@app.route('/show4')
def show_pages4():
    # 创建表格、插入数据
    # @app.before_first_request
    # 连接
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    sql = "SELECT rowid as RowNumber, * FROM database where 入学年 >= 2017 order by 入学年"
    sql1 = "SELECT count(*) from database where 入学年  == 2000"
    # 创建表
    c.execute(sql)
    #c.execute(sql1)
    u = c.fetchall()
    #s = u.count(u)
    #print(s)
    # conn.commit()
    # 关闭
    conn.close()
    return render_template('show4.html',u=u)





@app.route('/file1')
def file():
    return render_template('file.html')



# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 具有上传功能的页面
@app.route('/file')
def upload_test():
    return render_template('file.html')


@app.route('/test')
def test():
    return render_template('file.html')


@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])  # 拼接成合法文件夹地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = f.filename
        f.save(os.path.join(file_dir, fname))  # 保存文件到upload目录

        return render_template('file.html', status='OK')
    else:
        pass


@app.route("/download/<path:filename>")
def downloader(filename):
    dirpath = os.path.join(app.root_path, 'upload')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载




# @app.route("/image")
# def jianshu():
#     import matplotlib
#     matplotlib.use('Agg')  # 不出现画图的框
#     import matplotlib.pyplot as plt
#     from io import BytesIO
#     import base64
#
#     # 这段正常画图
#     plt.axis([0, 5, 0, 20])  # [xmin,xmax,ymin,ymax]对应轴的范围
#     plt.title('My first plot')  # 图名
#     plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 图上的点,最后一个参数为显示的模式
#     # -----------
#
#     # 转成图片的步骤
#     sio = BytesIO()
#     plt.savefig(sio, format='png')
#     data = base64.encodebytes(sio.getvalue()).decode()
#     print(data)
#     html = '''
#        <html>
#            <body>
#                <img src="data:image/png;base64,{}" />
#            </body>
#         <html>
#     '''
#     plt.close()
#     # 记得关闭，不然画出来的图是重复的
#     return html.format(data)
#     #format的作用是将data填入{}





if __name__ == '__main__':
    app.run()
