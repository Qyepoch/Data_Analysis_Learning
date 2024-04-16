# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=12)
March = [1, 3, 5, 7, 9, 11, 13]
Oco = [4,12,4,17,8,25,12,34,5]

x_label1 = range(1,8)
x_label2 = range(8,17)

# 设置图片大小（设置图片大小要在绘图之前）
plt.figure(figsize=(20,8),dpi=80)

# 绘图（一定要画完图之后再修改其他信息）
plt.scatter(x_label1,March,label="first")
plt.scatter(x_label2,Oco,label="其他")


# 修改x轴刻度
x_label = list(x_label1) + list(x_label2)
x_labels = ["第{}个点".format(i) for i in x_label]
plt.xticks(x_label,x_labels,fontproperties=my_font,rotation=45)
# 添加图例
plt.legend(loc='upper left',prop=my_font)

# 添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("标题",fontproperties=my_font)


# 展示
plt.show()
