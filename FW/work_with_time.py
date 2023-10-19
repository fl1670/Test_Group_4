import datetime

now = datetime.datetime.now()


class WorkWithTime:

    # Возвращяет дату "2015-07-25 00:00:00.000"
    def get_date_time_for_sql_increased_x_days(self, timedelta_days=0):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        temp = datetime2.strftime("%Y-%m-%d %H:%M:%S")
        temp = temp + '.000'
        return temp
