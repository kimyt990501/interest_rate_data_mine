#%%
import warnings
import pandas as pd
import seaborn as sns

#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font',family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 금리, GDP성장률, 주택거래건수 데이터 불러오기
ir_data = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\interest_rate_data_mine\\data\\ir_data_all.csv', index_col=0 ,encoding='euc-kr')

# 인덱스 값 설정
#idx = ir_data.index.astype('str')
idx = pd.to_datetime(ir_data.index)
idx_year = idx.year.astype('str')

# 1. 그래프 시각화
'''
# 1.1 데이터 각각 시각화
# 그래프 그리기 (선 그래프)
plt.figure(figsize = (12,10))

sns.lineplot(x=idx_year ,y='금리',data = ir_data, label = "기준금리")
sns.lineplot(x=idx_year ,y='GDP성장률',data = ir_data, label = "GDP성장률")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=45)
'''

# 1.2 모든 데이터 한번에 시각화

# 그래프 구간 나누기
fig = plt.figure(figsize=(20,10))
top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4, sharex=top_axes)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

# 선그래프 그리기 (기준금리, GDP성장률)
top_axes.plot(idx, ir_data['금리'], label='기준금리', linewidth=2)
top_axes.plot(idx, ir_data['GDP성장률'], label='GDP성장률', linewidth=2)
top_axes.plot(idx, ir_data['주택가격변동률'], label='주택가격변동률', linewidth=2)

# 막대 그래프 그리기 (주택 거래 건수)
bottom_axes.bar(idx, ir_data['거래건수'], width=40, 
                align='center')

# 그래프 title 지정
top_axes.set_title('기준금리, 주택 거래 건수, GDP성장률, 주택가격변동률 간의 관계', fontsize=22)
bottom_axes.set_title('주택 거래 건수', fontsize=10)

# X축 라벨 지정
bottom_axes.set_xlabel('연도', fontsize=15)

top_axes.legend()
plt.tight_layout()
plt.show()
# %%
