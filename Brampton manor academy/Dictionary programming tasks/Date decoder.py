def SplitDate(date):
    monthDict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    input_split = date.split('-')
    day=input_split[0]
    month=input_split[1]
    month_num=monthDict[month]
    year=input_split[2]
    return day, month_num, year

date=input("Please enter the date in the format of dd-mmm-yy: ")
print(SplitDate(date))
