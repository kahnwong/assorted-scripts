# 12 days, 26th IS the first day
# month 4
# month 5
from datetime import datetime
from datetime import timedelta


def generate_dates(start_date):
    # date1 = datetime.strptime(start_date, '%Y-%m-%d')
    # date2 = date1 + timedelta(days=12)

    # date_generated = [date1 + timedelta(days=x) for x in range(0, (date2-date1).days)]

    # for date in date_generated:
    #     print (date.strftime('%Y-%m-%d'))

    # print('\n\n')

    date1 = datetime.strptime(start_date, "%Y-%m-%d")
    date2 = date1 + timedelta(days=10)

    date_generated = [date1 + timedelta(days=x) for x in range(0, (date2 - date1).days)]

    for date in date_generated:
        print(
            "(A) Hormones @recurring due:{date}".format(date=date.strftime("%Y-%m-%d"))
        )
        # print('(B) Hormones evening @recurring due:{date}'.format(date=date.strftime('%Y-%m-%d')))

    print("\n\n")


generate_dates("2021-03-05")
generate_dates("2021-04-05")
generate_dates("2021-05-05")
generate_dates("2021-06-05")
generate_dates("2021-07-05")
generate_dates("2021-08-05")
generate_dates("2021-09-05")
