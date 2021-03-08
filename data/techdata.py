class techdata(object):
    # 如 MACD, BOLL, KDJ等技术指标，对象数据如下：
    # {
    #     "TDate": "2020/11/6 0:00:00",
    #     "DIFF": "-1.35749089083856",
    #     "DEA": "-1.35279634132149",
    #     "MACD": "-0.00938909903413787",
    #     "D": "35.7417208852936",
    #     "J": "21.9544238441133",
    #     "K": "31.1459552049002",
    #     "RSI1": "42.8235565886613",
    #     "RSI2": "43.3954250097063",
    #     "RSI3": "45.702663142688",
    #     "BOLL": "103.1275",
    #     "UPPER": "108.096027792118",
    #     "LOWER": "98.1589722078816",
    #     "Close": "100.69",
    #     "BIAS1": "-0.554723379039029",
    #     "BIAS2": "-0.875343533368884",
    #     "BIAS3": "-2.22056776616064",
    #     "WR1": "71.2914485165795",
    #     "WR2": "84.0534979423869"
    # }

    def __init__(self, tdate, diff, dea, macd,
                 d, j, k,
                 rsi1, rsi2, rsi3,
                 boll, upper, lower, close,
                 bias1, bias2, bias3,
                 wr1, wr2):
        self._tdate = tdate

        # macd
        self._diff = str(round(float(diff), 2))
        self._dea = str(round(float(dea), 2))
        self._macd = str(round(float(macd), 2))

        # kdj
        self._d = d
        self._j = j
        self._k = k

        # rsi
        self._rsi1 = rsi1
        self._rsi2 = rsi2
        self._rsi3 = rsi3

        # boll
        self._boll = str(round(float(boll), 2))
        self._upper = str(round(float(upper), 2))
        self._lower = str(round(float(lower), 2))
        self._close = str(round(float(close), 2))

        # bias
        self._bias1 = bias1
        self._bias2 = bias2
        self._bias3 = bias3

        # wr
        self._wr1 = wr1
        self._wr2 = wr2

    # ############### MACD指标 >>>>>>>>>>>>>>>>
    @property
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, diff):
        self._diff = diff

    @property
    def dea(self):
        return self._dea

    @dea.setter
    def dea(self, dea):
        self._dea = dea

    @property
    def macd(self):
        return self._macd

    @macd.setter
    def macd(self, macd):
        self._macd = macd

    # <<<<<<<<<<<<<<<<< MACD指标 ###############

    # ############### BOLL指标 >>>>>>>>>>>>>>>>
    @property
    def boll(self):
        return self._boll

    @boll.setter
    def boll(self, boll):
        self._boll = boll

    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, upper):
        self._upper = upper

    @property
    def lower(self):
        return self._lower

    @lower.setter
    def lower(self, lower):
        self._lower = lower

    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, close):
        self._close = close

    # <<<<<<<<<<<<<<<<< BOLL指标 ###############


def techdata_2_json(techdata):
    return {
        'TDate': techdata._tdate,
        # macd
        'DIFF': techdata._diff,
        'DEA': techdata._dea,
        'MACD': techdata._macd,
        # kdj
        'D': techdata._d,
        'J': techdata._j,
        'K': techdata._k,
        # rsi
        'RSI1': techdata._rsi1,
        'RSI2': techdata._rsi2,
        'RSI3': techdata._rsi3,
        # boll
        'BOLL': techdata._boll,
        'UPPER': techdata._upper,
        'LOWER': techdata._lower,
        'Close': techdata._close,
        # bias
        'BIAS1': techdata._bias1,
        'BIAS2': techdata._bias2,
        'BIAS3': techdata._bias3,
        # wr
        'WR1': techdata._wr1,
        'WR2': techdata._wr2
    }


def json_2_techdata(json):
    return techdata(
        json['TDate'],
        json['DIFF'], json['DEA'], json['MACD'],
        json['D'], json['J'], json['K'],
        json['RSI1'], json['RSI2'], json['RSI3'],
        json['BOLL'], json['UPPER'], json['LOWER'], json['Close'],
        json['BIAS1'], json['BIAS2'], json['BIAS3'],
        json['WR1'], json['WR2']
    )
