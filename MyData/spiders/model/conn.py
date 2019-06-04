import pymysql

class DealData:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='spider',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.db.cursor()

    def insert(self,column,*values,table=None):
        '''
        :param column: 数据库中的列名 list
        :param values: 插入数据库的数据,和column对应
        :param table: 数据表名
        '''
        column = ','.join(column)
        sql = 'insert into {table}({columns}) values(%s,%s,%s,%s,%s,%s,%s,%s) '.format(table=table,columns=column)
        self.cursor.execute(sql,(values))
        self.db.commit()

    def truncate(self,table=None):
        sql = 'truncate table {table}'.format(table=table)
        self.cursor.execute(sql)
        self.db.commit()


