# coding=utf-8
'''绘制横着的条形图'''
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=12)

x = ["功夫","美丽心灵","那些年我们\n一起追过的女孩"]
y = [45,23,34]

# 设置大小
plt.figure(figsize=(10,4),dpi=80)

# 绘图
plt.barh(range(len(x)),y,align='center',height=0.3,color="pink")#这里可以设置宽度

# 网格
plt.grid(alpha=0.3)

x_ = list(range(len(x)))
x_lab = ["《{}》".format(i) for i in x]
plt.yticks(x_,x_lab,fontproperties=my_font)
# 添加图例
plt.legend(prop=my_font)

plt.savefig("./images/barh.jpg")
# 展示
plt.show()