
sec_id = 'CZCE.FG'
sec_id = 'SHFE.RB'

bar_type = str(30 * 60)  # seconds, 'tick', 'daily'
bar_type = 'daily'  # seconds, 'tick', 'daily'

start_time='2017-05-15 9:00:00'
end_time='2017-09-12 15:00:00'


debug = True

a_subscribe_symbol = sec_id + '.bar.' + bar_type
subscribe_symbols = a_subscribe_symbol

bench_symbol = sec_id