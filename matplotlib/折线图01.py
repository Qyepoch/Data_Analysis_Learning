#-*-utf-8-*-
from matplotlib import pyplot as plt, font_manager
import  numpy as np
import random
import matplotlib

# s设置字体
'''font = {'family': 'sans-serif','weight': 'normal','size':12}
matplotlib.rc('font', **font)
# or 
matplotlib.rc('font',family='Micoroft')'''

# 另外一种设置字体中文100%成功
my_font = font_manager.FontProperties(fname=f'C:\Windows\Fonts\simsun.ttc')

temp = [random.randint(20,35) for _ in range(120)]
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,24,27,22,18,15]

# 设置图片大小    dpi：图片变清晰
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.plot(range(1,121),temp)

# 设置x轴刻度
# x_label = np.arange(2,25,0.5)
# plt.xticks(x_label[::3])# 步长为3

_x = ["10点{}分".format(i) for i in range(60)]
_x +=["11点{}分".format(i) for i in range(60)]
plt.xticks(range(0,120,10),_x[::10],rotation=45,fontproperties=my_font)# 将数值型数据对应到数字上 个数要相同 rotation:旋转的度数

# 设置y轴刻度
# plt.yticks(temp)

# 保存    可以保存svg矢量图格式，放大不会有锯齿
plt.savefig('./images/temperature.png')

# 添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度（℃）",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.4)# 透明度

# 最后展示
plt.show()
