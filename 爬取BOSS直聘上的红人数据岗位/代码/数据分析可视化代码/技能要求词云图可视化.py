import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#读取爬取文件的路径
file_path = "boss直聘红人运营数据.xlsx"
df = pd.read_excel(file_path)
skills_column = '技能要求' 
skills_text = ' '.join(df[skills_column].dropna().astype(str))
font_path = "C:\\Windows\\Fonts\\simhei.ttf"  
wordcloud = WordCloud(width=800, height=400,
                      background_color='white',
                      max_words=100,
                      max_font_size=100,
                      font_path=font_path,  
                      colormap='viridis',
                      random_state=42).generate(skills_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.title('技能要求词云图', fontproperties=FontProperties(fname=font_path, size=24), pad=20)
plt.show()
