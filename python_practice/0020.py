#!/usr/bin/env python
# 第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」
# 然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
# 就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
import re


def getTotalTime(time_list):
    hours = minutes = seconds = 0
    for single_time in time_list:
        if single_time.find('时') != -1:
            hours += int(single_time.split('时')[0])
            single_time = single_time.split('时')[1]
        elif single_time.find('分') != -1:
            minutes += int(single_time.split('分')[0])
            single_time = single_time.split('分')[1]
        elif single_time.find('秒') != -1:
            seconds += int(single_time.split('秒')[0])
            single_time = single_time.split('秒')[1]
    return 3600*hours + 60*minutes + 1*seconds


def main(csv_path):
    f = open(csv_path, 'r')
    content = f.read()
    f.close()
    time = re.findall('\w+?秒', content)
    # print(time)
    periodsOfTime = (re.findall('查询时段[\s\S]+?,[\s\S]+?,',
                     content)[0].split(',')[1])
    totalTime = getTotalTime(time)
    print('时间段:%s,总时长:%s秒' % (periodsOfTime, str(totalTime)))


if __name__ == '__main__':
    main('18225600365-20160801-20160831-201.csv')
    print('success!')
