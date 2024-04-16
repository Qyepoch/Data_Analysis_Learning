from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=12)

x = ["功夫","美丽心灵","那些年我们一起追过的女孩"]
y = [45,23,34]

# 设置大小
plt.figure(figsize=(8,15),dpi=80)

# 绘图
plt.bar(range(len(x)),y,align='center',width=0.3)#这里可以设置宽度



x_ = list(range(len(x)))
x_lab = ["《{}》".format(i) for i in x]
plt.xticks(x_,x_lab,rotation=90,fontproperties=my_font)
# 添加图例
plt.legend(prop=my_font)


# 展示
plt.show()