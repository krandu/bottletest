# encoding=utf-8
import MySQLdb
import logging

error_log = '/'.join(pro_path,'log/task_error.log')

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)S %(filename)s[line:%(lineno)d]%(levelname)s%(message)s',
                    datefmt='%Y-%m-%d%H:%M:%S',
                    filename=error_log,
                    filemode='a',)


db_name = 'task'
db_user = 'root'
db_pass = 'root'
db_ip = 'localhost'
db_port = 3306

def writeDb(sql,db_data=()):
    try:
        conn = MySQLdb.connect(db=db_name,user=db_user,passwd=db_pass,host=db_ip,port=int(db_port))
        cursor = conn.cursor()
    except Exception,e:
        print e
        logging.error('数据库连接失败：%s'%e)
        return False
    try:
        cursor.execute(sql,db_data)
        conn.commit()
    except Exception.e:
        conn.rollback()
        logging.error('数据写入失败：%s' % e )


app = default_app()
app = SessionMiddleware(app,session_opts)
run(app=app,host = 'localhost',port = 80,debug= True)