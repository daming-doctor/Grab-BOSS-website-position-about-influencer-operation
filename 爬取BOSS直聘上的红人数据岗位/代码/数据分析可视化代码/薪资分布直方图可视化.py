import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
#请提供文件路径
file_path = "boss直聘红人运营数据.xlsx"
df = pd.read_excel(file_path, sheet_name='Sheet1', usecols=['薪资'])
def parse_salary(salary_str):
    try:
        salary_str = salary_str.replace('k', '').replace('K', '').replace('万', '').replace('W', '')
        parts = salary_str.split('-')
        if len(parts) == 2:
            return (float(parts[0]) + float(parts[1])) / 2 * 1000  
        else:
            return float(parts[0]) * 1000  
    except (ValueError, AttributeError):
        return None
df['平均薪资'] = df['薪资'].apply(parse_salary)
df = df.dropna(subset=['平均薪资'])
plt.figure(figsize=(10, 6))
hist_values, bin_edges, patches = plt.hist(df['平均薪资'], bins=20, color='skyblue', edgecolor='black')
for i, patch in enumerate(patches):
    height = patch.get_height()
    plt.text(patch.get_x() + patch.get_width() / 2, height, 
             f'{int(height)}', ha='center', va='bottom')
plt.title('薪资分布直方图', fontsize=16)
plt.xlabel('平均薪资 (元)', fontsize=14)
plt.ylabel('频率', fontsize=14)
plt.show()