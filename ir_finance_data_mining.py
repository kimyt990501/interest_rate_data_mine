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

# 금리, 금융 관련 주식 주가 데이터 불러오기
ir_finance_data = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\interest_rate_data_mine\\data\\ir_finance_data.csv', index_col=0 ,encoding='euc-kr') # 전체 경로 (윈도우)
#ir_finance_data = pd.read_csv('interest_rate_data_mine\\data\\ir_finance_data.csv', index_col=0 ,encoding='euc-kr') # 상대경로

# 1. 그래프 시각화

# 인덱스 값 설정
#idx = ir_data.index.astype('str')
idx = pd.to_datetime(ir_finance_data.index)
idx_year = idx.year.astype('str')

# 1.1 데이터 각각 시각화

# 기준금리를 그래프에서 잘 보이게 하기 위해 500씩 곱해준다
ir_finance_data['기준금리'] = ir_finance_data['기준금리'].mul(5000)

# 기준 금리, 원/달러 환율 선 그래프로 시각화
plt.figure(figsize = (12,10))

sns.lineplot(x=idx_year ,y='기준금리', data = ir_finance_data, label = "기준금리")
sns.lineplot(x=idx_year ,y='한국금융지주', data = ir_finance_data, label = "한국금융지주")
sns.lineplot(x=idx_year ,y='신한지주', data = ir_finance_data, label = "신한지주")
sns.lineplot(x=idx_year ,y='하나금융지주', data = ir_finance_data, label = "하나금융지주")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=45)
# %%
