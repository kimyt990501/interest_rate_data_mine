import FinanceDataReader as fdr
import pandas as pd

# 코스피, 코스닥 지수 데이터 가져오기
kosdaq = fdr.DataReader('KQ11', '2006-06-01', '2023-07-01')
kospi = fdr.DataReader('KS11', '2006-06-01', '2023-07-01')

# 종가 데이터만 뽑되 각 월별 마지막 날 데이터만 가져온다
kospi = kospi['Close'].resample('M').first()
kosdaq = kosdaq['Close'].resample('M').first()

# 분기별 평균 구하기
kp_list = kospi.values.tolist()
kd_list = kosdaq.values.tolist()

list_p = []
list_d = []

for j in range(1, 205, 3):
    sum = 0
    for i in range(j, j + 3):
        sum += kp_list[i]
        mean = sum / 3
    list_p.append('%0.2f' % mean)

for j in range(1, 205, 3):
    sum = 0
    for i in range(j, j + 3):
        sum += kd_list[i]
        mean = sum / 3
    list_d.append('%0.2f' % mean)

kospi_df = pd.DataFrame(list_p)
kosdaq_df = pd.DataFrame(list_d)

kospi_df.columns = ['코스피지수']
kosdaq_df.columns = ['코스닥지수']

# 원달러환율 데이터 가져오기
exchange_rate = fdr.DataReader('USD/KRW', '2006-06-01', '2023-07-01')

# 종가 데이터만 뽑되 각 월별 마지막 날 데이터만 가져온다
ku_rate = exchange_rate['Close'].resample('M').first()

# 분기별 평균 구하기
ku_list = ku_rate.values.tolist()

list_ku = []
for j in range(1, 205, 3):
    sum = 0
    for i in range(j, j + 3):
        sum += ku_list[i]
        mean = sum / 3
    list_ku.append('%0.2f' % mean)

kurate_df = pd.DataFrame(list_ku)
kurate_df.columns = ['원달러환율']

# 인덱스 값인 날짜 데이터 직접 만들어서 각 데이터프레임에 할당해주기
date = pd.date_range(start="2006-09", end="2023-07", freq="3M")
kospi_df.index = date
kosdaq_df.index = date
kurate_df.index = date

# 각 데이터 프레임 합친 후 csv 파일로 저장
kskqku = pd.concat([kospi_df, kosdaq_df, kurate_df], axis=1, ignore_index=True)
kskqku.columns = ['코스피지수', '코스닥지수', '원달러환율']
kskqku['코스피지수'] = kskqku['코스피지수'].astype('float')
kskqku['코스닥지수'] = kskqku['코스닥지수'].astype('float')
kskqku['원달러환율'] = kskqku['원달러환율'].astype('float')

# kskqku.to_csv('C:\\Users\\user\\Desktop\\github_repo\\interest_rate_data_mine\\data\\kskqku_data.csv', encoding='euc-kr') # 전체경로 (윈도우)
kskqku.to_csv('interest_rate_data_mine\\data\\kskqku_data.csv', encoding='euc-kr') # 상대경로