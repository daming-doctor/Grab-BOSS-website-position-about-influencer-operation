from DrissionPage import ChromiumPage
import pandas as pd
import os
import time

dp = ChromiumPage()
# 启动监听特定接口
dp.listen.start('zhipin.com/wapi/zpgeek/search/joblist.json?')

# 访问目标网页
url = 'https://www.zhipin.com/web/geek/jobs?query=%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BA%A2%E4%BA%BA%E8%BF%90%E8%90%A5&city=101280600'
dp.get(url)

# 存储所有数据的列表
all_data = []
max_records = 300

first_resp = dp.listen.wait()
json_data = first_resp.response.body
jobList = json_data['zpData']['jobList']


for index in jobList:
    if len(all_data) >= max_records:
        break

    dit = {
        '公司': index.get('brandName'),
        '公司规模': index.get('brandScaleName'),
        '职位': index.get('jobName'),
        '地区': index.get('areaDistrict'),
        '地点': index.get('businessDistrict'),
        '学历': index.get('jobDegree'),
        '薪资': index.get('salaryDesc'),
        '技能要求': ''.join(index.get('skills', []))
    }
    all_data.append(dit)
    print(f"已收集 {len(all_data)} 条数据")

while len(all_data) < max_records:
    # 滚动到底部触发新数据加载
    dp.scroll.to_bottom()
    print(f"已滚动到底部，等待新数据... 当前已收集 {len(all_data)} 条数据")

    try:
        resp = dp.listen.wait(timeout=5)
        json_data = resp.response.body
        jobList = json_data['zpData']['jobList']

        # 如果没有新数据则退出
        if not jobList:
            print("没有获取到新数据，停止爬取")
            break

        # 解析新数据
        for index in jobList:
            if len(all_data) >= max_records:
                break

            dit = {
                '公司': index.get('brandName'),
                '公司规模': index.get('brandScaleName'),
                '职位': index.get('jobName'),
                '地区': index.get('areaDistrict'),
                '地点': index.get('businessDistrict'),
                '学历': index.get('jobDegree'),
                '薪资': index.get('salaryDesc'),
                '技能要求': ''.join(index.get('skills', []))
            }
            all_data.append(dit)
            print(f"已收集 {len(all_data)} 条数据")

        time.sleep(1)

    except Exception as e:
        print(f"等待新数据超时或出错: {str(e)}")
        break

# 保存所有数据到Excel
if all_data:
    df = pd.DataFrame(all_data)
    #请根据自身情况修改保存路径
    file_path = os.path.join(r'', 'boss直聘红人运营数据.xlsx')
    df.to_excel(file_path, index=False)
    print(f"共爬取 {len(all_data)} 条数据，已保存至 {file_path}")
else:
    print("未获取到任何数据")

dp.quit()