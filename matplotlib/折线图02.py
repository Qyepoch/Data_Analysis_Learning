# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname=f'C:\Windows\Fonts\simsun.ttc')
y_1 = [1,0,2,2,3,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,3,2,1,1]

x = range(11,31)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y_1,label='me',color='r',linewidth=5,linestyle='--',alpha=0.5)
plt.plot(x,y_2,label='同桌')

# 设置x轴刻度
x_leble = ["{}岁".format(i) for i in x]
plt.xticks(x,x_leble,fontproperties=my_font)
plt.yticks(range(0,9))

# 绘制网格
plt.grid(alpha=0.4)

# 添加图例
plt.legend(prop=my_font)# 使用prop显示中文

# 展示
plt.show()