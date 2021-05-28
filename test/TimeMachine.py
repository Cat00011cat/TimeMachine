import os
import datetime

new_date = datetime.datetime.now()  # 现在时间
data_str = new_date.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间
oneDay = datetime.datetime(2018, 9, 8, 9, 33 ,22)  # 认识的时间
difference = new_date.toordinal() - oneDay.toordinal()  # d.toordinal()返回日期是是自 0001-01-01 开始的第多少天
# print('今天是%s距认识老黄%s还有%s天' % (data_str, oneDay.strftime('%m-%d'), difference))
# print('今天是%s认识老黄已经%s天' % (data_str, difference))

print("时光机".center(30,'+'))
print('⏰相识于：{}\n\
⏰当前时间：{}'\
.format(oneDay,data_str))

print('✈时光机：{}天'.format(difference))
print('♥时光不老，我们不散♥')
print('😊'+'哈'*9)
print("✈⏰✈".center(30,'+'))
os.system("pause")  #这将生成一个暂停，并要求用户按任意键继续。
