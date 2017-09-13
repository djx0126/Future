import talib
import numpy as np
from gmsdk.util import bar_to_dict

from MAstrategy import SYGNAL_TYPE

ema_n = 50
atr_mean_n = 20
back_look_n = 20
atr_a = 20

def calc(strategy, configs, bar):
    last_daily_bars = strategy.get_last_n_dailybars(bar.exchange+'.'+bar.sec_id, int(ema_n * 1.25), end_time=bar.strendtime)
    close = _get_data(last_daily_bars, 'close')
    high = _get_data(last_daily_bars, 'high')
    low = _get_data(last_daily_bars, 'low')

    long_ema_period = ema_n
    short_ema_period = int(ema_n/5)
    ema_long = talib.EMA(close, timeperiod=long_ema_period)
    ema_short = talib.EMA(close, timeperiod=short_ema_period)

    atr = talib.ATR(high, low, close, timeperiod=atr_mean_n)

    hh = talib.MAX(high, timeperiod=back_look_n)[-1] - atr[-1] * atr_a / 10
    ll = talib.MIN(low, timeperiod=back_look_n)[-1] + atr[-1] * atr_a / 10

    if configs.debug:
        print('[%s]ema(%s): %s, atr:%s' % (str(bar.strendtime), str(ema_n), str(ema_long[-1]), str(atr[-1])))

    save_loss = hh if ema_short[-1] > ema_long[-1] else ll

    if bar.close > save_loss:
        return SYGNAL_TYPE.BUY

    if bar.close < save_loss:
        return SYGNAL_TYPE.SELL


def _get_data(bars, property):
    last_closes = [bar_to_dict(bar)[property] for bar in bars]
    last_closes.reverse()
    return np.asarray(last_closes)
