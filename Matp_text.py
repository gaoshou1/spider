from matplotlib import pyplot as plt
import random
from matplotlib import font_manager


# 设置字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")


x = range(0, 120)
y = [random.randint(20,35) for i in range(120)]

# 设置图片大小
# plt.figure(figsize=(20, 10), dpi=80)

# 散点图
# plt.scatter()

# 条形图
# plt.bar/barh()

# 绘图
plt.plot(x, y, label="线")

# 设置x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=90, fontproperties=my_font)  # rotation 字体方向

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(C)", fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.4)  # alpha透明度

# 添加图例
plt.legend(prop=my_font)

# 保存
# plt.savefig("./ti.png")
plt.show()