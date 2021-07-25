#2021_07_25
import requests
from bs4 import BeautifulSoup
##pandas - Series => 1차원 데이터 저장(행)
from pandas import Series

data = [100,200,300,400,500];
s = Series(data);

#print => index 0부터 출력
print(s);
#type => series
print(type(s));
#index 내가 원하는 값으로 만들기
date = ['2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04', '2021-07-05'];
series_myIndex = Series(data, index = date);
print(series_myIndex);
#내가 설정한 index값으로도 random access 가능 (원래 설정된 기본 index ex) 0,1,2,3,4 ... 으로도 접근 가능!)
print(series_myIndex['2021-07-01']);
print(series_myIndex[0]);
#딕셔너리처럼 keys() , values() 비슷한 매서드 존재
print(series_myIndex.index);
print(series_myIndex.values);
#여러 index값 인덱싱 가능 !!이때 리턴값은 series 객체임을 명심!!
print(series_myIndex[['2021-07-01' , '2021-07-03']]);
#index값으로 슬라이싱 하기 (END값 포함)
print(series_myIndex['2021-07-02' : '2021-07-04']);
#series 객체에 값 추가 및 삭제
series_myIndex['2021-07-05'] = 500; #값 추가
print(series_myIndex);
series_drop = series_myIndex.drop('2021-07-05'); #값 삭제 => 주의!! drop 매서드는 새로운 series 객체를 리턴함. 원본을 건들지 않음!!
print(series_drop);
#series 객체 사칙연산 (리스트, 튜플, 딕셔너리는 사칙연산 적용  X!!)
serise_operate = series_myIndex/10; #주의!! 이때 반환 값이 사칙연산 적용된 series 객체임. 원본을 건들지 않음!!!
print(serise_operate);


##pandas -  DataFrame => 2차원 데이터 저장
from pandas import DataFrame

#딕셔너리 객체를 이용해 DataFrame 생성!
data = {'open' : [100,200] , 'high' : [110,210]};
df = DataFrame(data);
print(df);
#OHLC(OPEN/HIGH/LOW/CLOSE) 데이터 표현하기 //index값 자동 맵핑된 숫자가 아닌 지정된 숫자로 표현하기
data = {'open' : [730,750], 'high' : [755,780], 'low' : [700,710], 'close' : [750,770]};
df = DataFrame(data, index =['2021-07-01', '2021-07-02']);
print(df);


#엑셀 파일 읽어오기
import pandas as pd
df = pd.read_excel("./python/excel/ohlc_test.xlsx");
print(df);
#엑셀 파일 자동 맵핑 인덱스 => 내가 설정한 인덱스로 바꾸기
df = df.set_index('date');
print(df)
#엑셀 파일로 저장하기
##df.to_excel('./python/excel/ohlc_test.xlsx');

#read_html() 함수로 웹페이지를 DataFrame로 변환하기
url = "https://finance.naver.com/item/sise_day.nhn?code=066570";
df = pd.read_html(requests.get(url,headers={'User-agent': 'Mozilla/5.0'}).text);
print(df[0]);

#읽은 데이터에서 NaN행 제거 axis = 0 (행) , axis = 1 (열)
print(df[0].dropna(axis=0));
print(type(df));
#DataFrame 객체에서 열 데이터 가져오기 (이때 반환되는 객체는 series)
data = {"open": [730, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]};
df = DataFrame(data , index=["2018-01-01", "2018-01-02"]); 
print(df['open']);
#DataFrame 객체에서 행 데이터 가져오기 (이때 반환되는 객체는 series)
print(df.loc['2018-01-01']);
#하나 이상의 행 데이터 가져오기 
target = ['2018-01-01', '2018-01-02'];
print(df.loc[target]);
#DataFrame에 데이터 열(column) 추가하기
data = {"2018-01-01" : 300, "2018-01-02" : 400};
series_volume = Series(data);
df['volume'] = series_volume;
print(df);
#DataFrame 기존 데이터 이용해서 새로운 열 추가
upper = df['open'] * 1.3;
df['upper'] = upper;
print(df);
#column shift = 열/행 조작하기/옮기기
s = Series([100,200,300]);
s2 = s.shift(1);
print(s);
print(s2);

##연습문제





