from datetime import datetime
def get_days_from_today(date):
    date=datetime.strptime(date,'%Y-%m-%d')
    return (datetime.today()-date).days
print(get_days_from_today("2021-10-09"))