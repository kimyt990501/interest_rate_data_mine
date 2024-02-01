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

# 금리, 원/달러환율, 주가 데이터 불러오기
ir_kskqku_data = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\interest_rate_data_mine\\data\\ir_kskqku_data.csv', index_col=0 ,encoding='euc-kr') # 전체 경로 (윈도우)
#ir_kskqku_data = pd.read_csv('interest_rate_data_mine\\data\\ir_kskqku_data.csv', index_col=0 ,encoding='euc-kr') # 상대경로


# %%
