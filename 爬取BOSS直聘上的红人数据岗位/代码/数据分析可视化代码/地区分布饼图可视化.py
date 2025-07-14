import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
#请提供文件路径
file_path = "boss直聘红人运营数据.xlsx"
df = pd.read_excel(file_path)
region_counts = df['地区'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal') 
plt.title('地区分布')
plt.show()