from datetime import datetime

date = datetime(2018, 1, 10)
print('NOW', datetime.now())

timestamp = datetime.timestamp(date)
print("timestamp =", timestamp)


#%%
from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))


#%%
from datetime import timedelta, datetime, date

one_date = date(2018, 1, 10)
t_delta = timedelta(days=5)

new_date = one_date - t_delta
print('new_date', new_date)

