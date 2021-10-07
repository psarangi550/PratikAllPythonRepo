import datetime
import pytz

# for ele in pytz.all_timezones:
#     print(ele)
dt=datetime.datetime.now(tz=pytz.UTC)
tz_london=pytz.timezone("Europe/Helsinki")
dt=dt.now().astimezone(tz=tz_london)
print(dt)

dt3=datetime.datetime.today().replace(tzinfo=pytz.UTC)
tz_london=pytz.timezone("Europe/Helsinki")
dt2=dt3.now().astimezone(tz=tz_london)
print(dt2)

#2nd way of doing the time is
dt1=datetime.datetime.now()
Helsinki=pytz.timezone("Europe/Helsinki")
dt1=Helsinki.localize(dt1)
dt2=dt1.now(tz=Helsinki)
print(dt2)