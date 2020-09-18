class marketData(object):
    # code: 002912, name: 中新赛克, latest_price: 69.88,
    # opening_price: 69.4, closed_price: 69.3, average_price: 69.64,
    # highest_price: 70.62, lowest_price: 68.52, top_price: 76.23,
    # bottom_price: 62.37, business_number: 20397, business_money: 142032261.0,
    # inflow: 18210567.0, outflow: 18579074.0, currency_value: 5793890560.0,
    # total_value: 12192036275.199999, increase: -10.8

    def __init__(self, code, name, latest_price, opening_price, closed_price,
                 average_price, highest_price, lowest_price, top_price,
                 bottom_price, business_number, business_money, inflow,
                 outflow, currency_value, total_value, increase):
        '''

        :param code:  股票代码
        :param name:  股票名称
        :param latest_price: 今日最新价
        :param opening_price:  今日开盘价
        :param closed_price:  昨天收盘价
        :param average_price:  今日均价
        :param highest_price:  今日最高价
        :param lowest_price:  今日最低价
        :param top_price:  今日涨停价
        :param bottom_price:  今日跌停价
        :param business_number:  今日成交量
        :param business_money:  今日成交额
        :param inflow:  今日主力流入
        :param outflow:  今日主力流出
        :param currency_value:  流通市值
        :param total_value:  总市值
        :param increase:  今年以来涨幅
        '''
        self._code = code
        self._name = name
        self._latest_price = float(latest_price)
        self._opening_price = float(opening_price)
        self._closed_price = float(closed_price)
        self._average_price = float(average_price)
        self._highest_price = float(highest_price)
        self._lowest_price = float(lowest_price)
        self._top_price = float(top_price)
        self._bottom_price = float(bottom_price)
        self._business_number = int(business_number)
        self._business_money = int(business_money)
        self._inflow = int(inflow)
        self._outflow = int(outflow)
        self._currency_value = int(currency_value)
        self._total_value = int(total_value)
        self._increase = float(increase)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def latest_price(self):
        return self._latest_price

    @property
    def opening_price(self):
        return self._opening_price

    @property
    def closed_price(self):
        return self._closed_price

    @property
    def average_price(self):
        return self._average_price

    @property
    def highest_price(self):
        return self._highest_price

    @property
    def lowest_price(self):
        return self._lowest_price

    @property
    def top_price(self):
        return self._top_price

    @property
    def bottom_price(self):
        return self._bottom_price

    @property
    def business_number(self):
        return self._business_number

    @property
    def business_money(self):
        return self._business_money

    @property
    def inflow(self):
        return self._inflow

    @property
    def outflow(self):
        return self._outflow

    @property
    def currency_value(self):
        return self._currency_value

    @property
    def total_value(self):
        return self._total_value

    @property
    def increase(self):
        return self._increase

    def __str__(self):
        ret = '[code: %s, name: %s, latest_price: %s, opening_price: %s, closed_price: %s, average_price: %s, highest_price: %s, lowest_price: %s, top_price: %s, bottom_price: %s, business_number: %s, business_money: %s, inflow: %s, outflow: %s, currency_value: %s, total_value: %s, increase: %s]' % (
            self.code, self.name, self.latest_price,
            self.opening_price, self.closed_price, self.average_price,
            self.highest_price, self.lowest_price, self.top_price,
            self.bottom_price, self.business_number, self.business_money,
            self.inflow, self.outflow, self.currency_value,
            self.total_value, self.increase)
        return ret
