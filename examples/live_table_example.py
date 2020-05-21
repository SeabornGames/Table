from random import random, seed
from time import monotonic, sleep

from seaborn_table import SeabornTable

table = SeabornTable(
    columns=['#', 'time', 'characters', 'number'],
    live_tables=[
        dict(type='grid', recreate=40, clip_widths=15, repeat_header=20,
             break_line=True, min_widths=0, align='center')])

seed(monotonic())
for i in range(10000):
    try:
        random_characters = ''.join([chr(int(random() * 74) + 48)
                                     for i in range(int(random() * 20))])
        table.append({'#': i,
                      'time': monotonic(),
                      'characters': random_characters,
                      'number': round(random(), int(random() * 10))})
        sleep(0.3)
    except KeyboardInterrupt:
        break

table.close_live_table()
