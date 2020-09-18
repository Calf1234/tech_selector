import sqlite3
from datetime import datetime
from utils import utils
from data import marketdata


class operate(object):
    # 个股每日行情数据表
    table_market_data = 'market_data'
    table_followed_stocks = 'followed_stocks'

    def __init__(self, db_name='stock.db', db_path='stored/'):
        if not (isinstance(db_name, str) and isinstance(db_path, str)):
            info = 'class operate, interface __init__, parms[db_name: %s, db_path: %s] invalid' % (
                str(db_name), str(db_path))
            raise Exception(info)

        if not db_name.endswith('.db'):
            self.db_name = db_name.strip() + '.db'
        else:
            self.db_name = db_name

        if not db_path.endswith('/'):
            self.db_path = db_path.strip() + '/'
        else:
            self.db_path = db_path
        self.db = self.db_path + self.db_name

    def create_table_market_data(self, table_name):
        if type(table_name) != str or len(table_name.strip()) < 1:
            info = 'create_table_market_data, param[table_name: %s] invalid' % (str(table_name))
            raise Exception(info)

        utils.myprint(2, 'create_table_market_data, db: ' + self.db + ', table_name: ' + table_name)

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS %s ('
                       'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
                       'code VARCHAR(20) NOT NULL DEFAULT \'999999\', '
                       'name VARCHAR(20), '
                       'latest_price FLOAT, '
                       'opening_price FLOAT, '
                       'closed_price FLOAT, '
                       'average_price FLOAT, '
                       'highest_price FLOAT, '
                       'lowest_price FLOAT, '
                       'top_price FLOAT, '
                       'bottom_price FLOAT, '
                       'business_number INTEGER, '
                       'business_money INTEGER, '
                       'inflow INTEGER, '
                       'outflow INTEGER, '
                       'currency_value INTEGER, '
                       'total_value INTEGER, '
                       'increase FLOAT, '
                       'timestamp INTEGER, '
                       'date TEXT)' % (table_name))

        cursor.close()
        conn.close()

    def insert_marketData(self, data):
        '''插入指定股票的当日行情数据，该行情数据是在当日股市收盘后从东方财富网址爬取的。

        :param marketData: 行情数据
        :return:
        '''

        if data is None and not isinstance(data, marketdata.marketData):
            utils.myprint(3, 'insert_marketData, 参数不合法, marketData: ' + str(data))
            return

        timestamp = int(datetime.now().timestamp())
        date = str(datetime.now())
        utils.myprint(2, 'insert_marketData, timestamp: ' + str(timestamp) + ', date: ' + date)

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        # 插入指定股票的当日行情数据
        sql = 'INSERT INTO %s (code, name, latest_price, opening_price, closed_price, average_price, highest_price, lowest_price, top_price, bottom_price, business_number, business_money, inflow, outflow, currency_value, total_value, increase, timestamp, date) VALUES (\'%s\', \'%s\', %f, %f, %f, %f, %f, %f, %f, %f, %d, %d, %d, %d, %d, %d, %f, %d, \'%s\')' % (
            self.table_market_data, data.code, data.name, data.latest_price, data.opening_price, data.closed_price,
            data.average_price, data.highest_price, data.lowest_price, data.top_price, data.bottom_price,
            data.business_number, data.business_money, data.inflow, data.outflow, data.currency_value, data.total_value,
            data.increase, timestamp, date)

        utils.myprint(2, 'insert_marketData, insert sql: ' + str(sql))
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    def create_table_followed_stocks(self, table_name):
        if type(table_name) != str or len(table_name.strip()) < 1:
            info = 'create_table_followed_stocks, param[table_name: %s] invalid' % (str(table_name))
            raise Exception(info)

        utils.myprint(2, 'create_table_followed_stocks, db: ' + self.db + ', table_name: ' + table_name)

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS %s ('
                       'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
                       'code VARCHAR(20) NOT NULL DEFAULT \'999999\', '
                       'name VARCHAR(20), '
                       'a_h BOOLEAN, '
                       'group1 BOOLEAN, '
                       'group2 BOOLEAN, '
                       'group3 BOOLEAN, '
                       'group4 BOOLEAN, '
                       'date TEXT)' % (table_name))

        cursor.close()
        conn.close()

    def insert_followedStock(self, data):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        sql = 'insert into %s (code, name, a_h, group1, group2, group3, group4, date) values (\'%s\', \'%s\', %d, %d, %d, %d, %d, \'%s\')' % (
            self.table_followed_stocks, data['code'], data['name'], data['a_h'], data['group1'], data['group2'],
            data['group3'], data['group4'], data['date'])

        utils.myprint(2, 'insert_followedStock, insert sql: ' + str(sql))
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    def query_allstock(self):
        '''查询所以已关注的股票代码，除开港股的

        :return: [(code1, name1), (code2, name2), ...]
        '''
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        sql = 'select code, name from %s where a_h=1' % (self.table_followed_stocks)
        utils.myprint(1, 'query_allcode, sql: ' + sql)
        cursor.execute(sql)

        sql_result = cursor.fetchall()
        cursor.close()
        conn.close()
        return sql_result

    def query_stock_by_group(self, **kwargs):
        '''根据分组条件条件来帅选股票代码，条件有group1, group2, group3, group4等

        :param kwargs: (group1, group2, group3, group4, 四选一)字段
        :return: [(code1, name1), (code2, name2), ...]
        '''
        utils.myprint(2, 'query_stock_by_condition, param: ' + str(kwargs))
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        sql = 'select code, name from %s where ' % (self.table_followed_stocks)
        if len(kwargs) < 1:
            sql = 'select code, name from %s ' % (self.table_followed_stocks)
        elif 'a_h' in kwargs:
            sql += 'a_h = %d' % (kwargs['a_h'])
        elif 'group1' in kwargs:  # 马教授
            sql += 'group1 = %d' % (kwargs['group1'])
        elif 'group2' in kwargs:  # 科技类
            sql += 'group2 = %d' % (kwargs['group2'])
        elif 'group3' in kwargs:  # 消费量
            sql += 'group3 = %d' % (kwargs['group3'])
        elif 'group4' in kwargs:  # 刘备教授
            sql += 'group4 = %d' % (kwargs['group4'])

        utils.myprint(1, 'query_stock_by_condition, sql: ' + sql)
        cursor.execute(sql)

        sql_result = cursor.fetchall()
        cursor.close()
        conn.close()
        return sql_result

    def delete_today_marketdata(self):
        ''' 删除今天的行情数据，来自表 market_data

        :return:
        '''

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        sql = 'select code, name from %s where timestamp > %d' % (self.table_market_data, utils.get_current_day())

        utils.myprint(1, 'delete_today_marketdata, sql: ' + sql)
        cursor.execute(sql)
        stocks = cursor.fetchall()
        if len(stocks) > 0:
            sql = 'delete from %s where timestamp > %d' % (self.table_market_data, utils.get_current_day())
            utils.myprint(3, 'delete_today_marketdata, sql: ' + sql)
            cursor.execute(sql)
        else:
            utils.myprint(2, 'delete_today_marketdata, no data, its time > %s' % (
                datetime.fromtimestamp(utils.get_current_day())))

        cursor.close()
        conn.close()
