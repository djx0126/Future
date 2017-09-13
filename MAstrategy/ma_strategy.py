#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gmsdk.api import StrategyBase
from gmsdk.util import bar_to_dict

from MAstrategy import configs


class MyStrategy(StrategyBase):
    def __init__(self, *args, **kwargs):
        super(MyStrategy, self).__init__(*args, **kwargs)
        self.oc = True
    
    def on_login(self):
        print('logged in')
    
    def on_error(self, err_code, msg):
        # print('get error: %s - %s' % (err_code, msg))
        pass
    
    def on_bar(self, bar):
        print('%s: %s, %s'%(str(bar.sec_id ), str(bar.strendtime), str(bar.close)))
        print(bar_to_dict(bar))
        if self.oc:
            self.open_long(bar.exchange, bar.sec_id, 0, 100)
        else:
            self.close_long(bar.exchange, bar.sec_id, 0, 100)
        self.oc = not self.oc

    def on_backtest_finish(self, indicator):
        print('backtest finished', str(indicator))



if __name__ == '__main__':
    mystrategy = MyStrategy(
        username='13916718115',
        password='dd103654',
        strategy_id='9517a1cf-9627-11e7-b97f-9eb6d0d3ac91',
        subscribe_symbols=configs.a_subscribe_symbol,
        mode=4,
        td_addr='localhost:8001')
    ret = mystrategy.backtest_config(
        start_time=configs.start_time,
        end_time=configs.end_time,
        initial_cash=1000000,
        transaction_ratio=1,
        commission_ratio=0,
        slippage_ratio=0,
        price_type=1,
        bench_symbol=configs.bench_symbol)#基准=沪深300
    print('config status: ', ret)
    ret = mystrategy.run()
    print('exit code: ', ret)
