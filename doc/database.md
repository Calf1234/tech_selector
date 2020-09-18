# 数据存储

## 个股收盘行情数据

### 行情数据

- 最新 f43、今开 f46、昨收 f60、均价 f71、最高 f44、最低 f45、涨停价 f51、跌停价 f52、成交量 f47、成交额 f48
- 量比 f50、换手率 f168、振幅 f170、内盘 f161、外盘 f49
- 流通股本 f85、总股本 f84、流通市值 f117、总市值 f116
- 市净率 f167、动态市盈率 f162、静态市盈率 f163、滚动市盈率 f164
- 每股收益 f55、每股净资产 f92
- 52周最高 f174、52周最低 f175
- 主力流入 f135、主力流出 f136
- 20日涨幅、60日涨幅、今年以来涨跌幅


### 个股单日行情数据表：

行情数据内容有不少，数据库表也没必要把所有数据都存储进来，所以挑选部分重要数据进行存储。

| 字段 | 类型 | 描述 |
| :-- | :-- | :-- |
| id | INTEGER | 主键，自增长|
| code | VARCHAR(20) | 股票代码|
| name | VARCHAR(20) | 股票名称|
| latest_price | FLOAT | 最新，即收盘价|
| opening_price | FLOAT | 今开，即开盘价|
| closed_price | FLOAT | 昨收，即昨天的收盘价|
| average_price | FLOAT | 均价|
| highest_price | FLOAT | 最高|
| lowest_price | FLOAT | 最低|
| top_price | FLOAT | 涨停价|
| bottom_price | FLOAT | 跌停价|
| business_number| INTEGER | 成交量|
| business_money | INTEGER | 成交额|
| inflow | INTEGER | 主力流入|
| outflow | INTEGER | 主力流出|
| currency_value | INTEGER | 流通市值|
| total_value | INTEGER | 总市值|
| increase | FLOAT | 今年以来涨跌幅|
| timestamp | INTEGER | 存储日期，指定从1970-01-01 00:00:00 utc开始的秒数|
| date | TEXT | 存储日期，以“yyyy-mm-dd hh:mm:ss.sss” 格式指定日期|


### 样例代码

```text

# code: 002912, name: 中新赛克, latest_price: 69.88,
# opening_price: 69.4, closed_price: 69.3, average_price: 69.64,
# highest_price: 70.62, lowest_price: 68.52, top_price: 76.23,
# bottom_price: 62.37, business_number: 20397, business_money: 142032261.0,
# inflow: 18210567.0, outflow: 18579074.0, currency_value: 5793890560.0,
# total_value: 12192036275.199999, increase: -10.8

# 创建表
CREATE TABLE market_data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, code VARCHAR(20) NOT NULL DEFAULT '999999', name VARCHAR(20), latest_price FLOAT, opening_price FLOAT, closed_price FLOAT, average_price FLOAT, highest_price FLOAT, lowest_price FLOAT, top_price FLOAT, bottom_price FLOAT, business_number INTEGER, business_money INTEGER, inflow INTEGER, outflow INTEGER, currency_value INTEGER, total_value INTEGER, increase FLOAT, timestamp INTEGER, date TEXT);

# 插入数据
insert into market_data ('code', 'name', 'latest_price', 'opening_price', 'closed_price', 'average_price', 'highest_price', 'lowest_price', 'top_price', 'bottom_price', 'business_number', 'business_money', 'inflow', 'outflow', 'currency_value', 'total_value', 'increase') values ('002912', '中新赛克', 69.88, 69.4, 69.3, 69.64, 70.62, 68.52, 76.23, 62.37, 20397, 142032261, 18210567, 18210567, 5793890560, 12192036275, -10.8);
```



## 已关注的股票列表

### 数据表

| 字段 | 类型 | 描述 |
| :-- | :-- | :-- |
| id | INTEGER | 主键，自增长|
| code | VARCHAR(20) | 股票代码|
| name | VARCHAR(20) | 股票名称|
| a_h | BOOLEAN | A股/港股， 0/1(1 表示A股)|
| group1 | BOOLEAN | 马教授自选股列表，0/1(1 表示在关注列表中)|
| group2 | BOOLEAN | 科技类自选股列表，0/1(1 表示在关注列表中)|
| group3 | BOOLEAN | 消费类自选股列表，0/1(1 表示在关注列表中)|
| group4 | BOOLEAN | 刘备教授自选股列表，0/1(1 表示在关注列表中)|
| date | TEXT | 存储日期，以“yyyy-mm-dd hh:mm:ss.sss” 格式指定日期|


### 样例代码

```text

# 创建表
CREATE TABLE followed_stocks (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, code VARCHAR(20) NOT NULL DEFAULT '999999', name VARCHAR(20), a_h BOOLEAN, group1 BOOLEAN, group2 BOOLEAN, group3 BOOLEAN, group4 BOOLEAN, date TEXT);


```