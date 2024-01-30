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

# 1999년 2분기부터 2023년 2분기까지의 GDP 성장률 데이터 불러오기
gdp_data = pd.read_csv('C:\\Users\\user\\Desktop\\test\\gdp_1999_2_2023_2.csv', encoding='euc-kr')

# 결측치 삭제
gdp_data = gdp_data.dropna()

# 필요없는 행 삭제
gdp_data = gdp_data.drop([0], axis = 0)

# 행열 전환 후 필요없는 인덱스삭제 및 열 이름 변경
gdp_data = gdp_data.T
gdp_data = gdp_data.drop(['Unnamed: 0'])
gdp_data.columns = ['GDP성장률']

#print(gdp_data)


# 1999년 2분기부터 2023년 2분기 까지의 기준 금리 데이터 가져오기
std_ir_data = pd.read_csv('C:\\Users\\user\\Desktop\\test\\korea_ir.csv')

# 필요없는 열 삭제
std_ir_data = std_ir_data.drop(columns=['통계표', '계정항목', '단위', '변환'])

# 행, 열 전환 후 열 이름 변경
std_ir_data = std_ir_data.T
std_ir_data.columns = ['금리']
#print(std_ir_data)

# 인덱스 값인 날짜 데이터 직접 만들어서 각 데이터프레임에 할당해주기
date = pd.date_range(start="1999-04", end="2023-04", freq="3MS")
gdp_data.index = date
std_ir_data.index = date

#print(gdp_data, std_ir_data)

gdp_strir = pd.concat([gdp_data, std_ir_data], axis=1, ignore_index=True)
gdp_strir.columns = ['GDP성장률', '금리']
gdp_strir['GDP성장률'] = gdp_strir['GDP성장률'].astype('float')
#print(gdp_strir)