sec_id = 'SHFE.RB'
bar_type = '60'  # seconds, 'tick', 'daily'

start_time='2017-06-15 9:00:00'
end_time='2017-06-18 15:00:00'

a_subscribe_symbol = sec_id + '.bar.' + bar_type
subscribe_symbols = a_subscribe_symbol

bench_symbol = sec_id