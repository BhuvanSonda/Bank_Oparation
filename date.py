import datetime as dt

def age_finder(year,month,day):
    now=dt.date.today()
    birth=dt.date(year=year,month=month,day=day)
    print(f'you born on "{birth.strftime("%A")}"')
    print(f"your current age is {(now.year-birth.year)-1} year - {now.month+(12-birth.month)} months \n")

def alram(day=0,hrs=0,min=0,sec=0):
    current=dt.datetime.now()
    t=current.time()
    set=dt.time(hour=hrs,minute=min,second=sec)
    D_set=current+dt.timedelta(days=day)
    print(f"your alram is set for {D_set.strftime('%A')}, {set} ")
    print(f"remaining time is {D_set.day-current.day} days , {t.hour-set.hour}:{t.minute-set.minute}:{t.second-set.second} \n")



age_finder(2005,10,17)
alram(1,1,1,0)