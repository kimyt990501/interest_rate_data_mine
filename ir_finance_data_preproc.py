import FinanceDataReader as fdr
import pandas as pd

# 금리 데이터 가져오기
#ir_data = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\interest_rate_data_mine\\data\\stdir.csv', index_col=0 ,encoding='euc-kr') # 전체 경로 (윈도우)
ir_data = pd.read_csv('interest_rate_data_mine\\data\\stdir.csv', index_col=0 ,encoding='euc-kr') # 상대경로
ir_data = ir_data[29:]
#print(ir_data)

# 한국금융지주, 신한지주, 하나금융지주 주식 데이터 가져오기
hankook = fdr.DataReader('071050', '2006-06-01', '2023-07-01')
shinhan = fdr.DataReader('055550', '2006-06-01', '2023-07-01')
hana = fdr.DataReader('086790', '2006-06-01', '2023-07-01')

# 종가 데이터만 뽑되 각 월별 마지막 날 데이터만 가져온다
hankook = hankook['Close'].resample('M').first()
shinhan = shinhan['Close'].resample('M').first()
hana = hana['Close'].resample('M').first()

#print(hankook)
#print(shinhan)
#print(hana)

# 분기별 평균 구하기
hk_list = hankook.values.tolist()
sh_list = shinhan.values.tolist()
hn_list = hana.values.tolist()

list_hk = []
list_sh = []
list_hn = []

for j in range(1, 205, 3):
    sum = 0
    for i in range(j, j + 3):
        sum += hk_list[i]
        mean = sum / 3
    list_hk.append('%0.2f' % mean)

for j in range(1, 205, 3):
    sum = 0
    for i in range(j, j + 3):
        sum += sh_list[i]
        mean = sum / 3
    list_sh.append('%0.2f' % mean)

for j in range(1, 205, 3):
    sum = 0
    for i in range(j, j + 3):
        sum += hn_list[i]
        mean = sum / 3
    list_hn.append('%0.2f' % mean)

hankook_df = pd.DataFrame(list_hk)
shinhan_df = pd.DataFrame(list_sh)
hana_df = pd.DataFrame(list_hn)

hankook_df.columns = ['지수']
shinhan_df.columns = ['지수']
hana_df.columns = ['지수']

# 인덱스 값인 날짜 데이터 직접 만들어서 각 데이터프레임에 할당해주기
date = pd.date_range(start="2006-09", end="2023-07", freq="3M")
hankook_df.index = date
shinhan_df.index = date
hana_df.index = date
ir_data.index = date

ir_finance_data = pd.concat([ir_data, hankook_df, shinhan_df, hana_df], axis=1, ignore_index=True)
ir_finance_data.columns = ['기준금리','한국금융지주', '신한지주', '하나금융지주']
ir_finance_data['기준금리'] = ir_finance_data['기준금리'].astype('float')
ir_finance_data['한국금융지주'] = ir_finance_data['한국금융지주'].astype('float')
ir_finance_data['신한지주'] = ir_finance_data['신한지주'].astype('float')
ir_finance_data['하나금융지주'] = ir_finance_data['하나금융지주'].astype('float')

# ir_finance_data.to_csv('C:\\Users\\user\\Desktop\\github_repo\\interest_rate_data_mine\\data\\ir_finance_data.csv', encoding='euc-kr') # 전체경로 (윈도우)
ir_finance_data.to_csv('interest_rate_data_mine\\data\\ir_finance_data.csv', encoding='euc-kr') # 상대경로