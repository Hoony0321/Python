#import
import pybithumb as pybit
import time
import datetime

### 가상화폐 티커 목록 얻기 ###

# ticker = pybithumb.get_tickers();
# print(ticker);
# print(len(ticker)); #가상화폐 개수


### 현재가 얻기 ###

# price = pybithumb.get_current_price("BTC");
# print(price);

### 1초에 한번씩 현재가 얻기 -  최대 초당 20회 API 호출 가능(초과할 시 차단됨) ###

# while(True):
#     price = pybithumb.get_current_price("BTC");
#     print(price);
#     time.sleep(1);  


### 모든 가상화폐 현재가 출력하기 ###

# tickers = pybit.get_tickers();

# for index,ticker in enumerate(tickers):
#     if(index == 20): break;
#     price = pybit.get_current_price(ticker);
#     print(ticker , " : " , price);
#     time.sleep(0.01);


### 24시간동안 저가/고가/거래금액/거래량 가져오기 ###

# detail =pybit.get_market_detail("BTC"); #반환값 튜플임.
# print(detail);


### 호가 정보 얻기 ###

# orderbook = pybit.get_orderbook("BTC"); #딕셔너리 객체 반환
# print(orderbook);

# for k in orderbook: #timestamp & payment_currency & order_currency & bids & asks 이렇게 총 5개의 키가 있음.
#     print(k);

# print(orderbook['payment_currency']); #빗썸은 현재 원화만 지원하므로 결제 화폐는 KRW로 출력
# print(orderbook['order_currency']); #조회한 가상화폐 티커 출력

# dt = datetime.datetime.fromtimestamp(int(orderbook['timestamp'])/1000); #timestamp는 1970년 1월 1일부터 지나간 ms 값을 저장하고 있음. 이를 datetime 모듈 이용해서 알아보기 쉽게 변환.
# print(dt); #호가를 조회한 시간 출력

# bids = orderbook['bids'] #매수 호가
# asks = orderbook['asks'] #매도 호가
# print(bids);
# print(asks);

# for bid in bids:
#     price = bid['price'];
#     quantity = bid['quantity'];
#     print("매수 호가 :" , price , "매수잔량 :" , quantity);


### 여러 가상화폐 정보 한번에 얻기 ###

all = pybit.get_current_price("ALL");
for k,v in all.items():
    print(k,v);


### 모든 가상화폐 현재가 출력 ###

# all = pybit.get_current_price("ALL");
# for ticker, data in all.items():
#     print(ticker , data['closing_price']);


### 예외 처리 ###
#네트워크 불량 / 서버 불량 등 다양한 원인으로 예기치 못한 문제가 발생하여 생각하지 못한 값이 바인딩되어 코드 실행에 문제가 생길 수 있음
#따라서 이에 대한 예외 처리를 try / except 구문을 통해 처리해야 함.


# while(True):
#     price = pybit.get_current_price("BTC");
#     try:
#         print(price/10);
#     except:
#         print("에러 발생!!" , price);
#     time.sleep(0.2);


###연습문제
#1) 표 5-1을 참고해서 모든 가상화폐의 24시간 변동률을 출력하세요.

# allCurrency = pybit.get_current_price("ALL");

# for ticker , data in allCurrency.items():
#     print(ticker , data['fluctate_rate_24H']);



### 거래소 과거 시세 가져오기 ###

# btc = pybit.get_ohlcv("BTC");
# print(btc);


### 이동 평균 계산하기 ###

# btc = pybit.get_ohlcv("BTC");
# close = btc['close'];

# print((close[0] + close[1] + close[2] + close[3] + close[4]) / 5)
# print((close[1] + close[2] + close[3] + close[4] + close[5]) / 5)
# print((close[2] + close[3] + close[4] + close[5] + close[6]) / 5)  
# # ===> 너무 귀찮음 / rolling / mean 매소드 사용하면 됨

# window = close.rolling(5); # rolling(5) => 5일씩 데이터를 그룹화
# ma5 = window.mean(); # mean() => 그룹화된 값의 평균을 구함
# print(ma5);


### 이동 평균 위에 있는지 아래에 있는지 판단하는 함수 만들기 ###

# btc = pybit.get_ohlcv("BTC");
# close = btc['close'];

# ma5 = close.rolling(window=5).mean();

# #ma5[-1] 은 제일 최근 5일간 이동평균인데 이건 오늘 날짜까지 포함되어 있음. 
# # 현재 시장이 상승장인지 하락장인지 보기위해선 전날까지 계산된 5일 이동평균을 봐야하므로 ma5 맨 뒤에서 2번째 객체 이용
# last_ma5 = ma5[-2]; 

# cur_price = pybit.get_current_price("BTC");
# if cur_price > last_ma5:
#     print("상승장입니다.");
# else :
#     print("하락장입니다.");


### 가상화폐 ticker 인자로 받아 상승장/하락장 판단 함수 만들기 ###

# def increase_marker(ticker):
#     data = pybit.get_ohlcv(ticker);
#     ma5 = data['close'].rolling(window=5).mean();
#     last_ma5 = ma5[-2];
#     current_price = pybit.get_current_price(ticker);
#     if current_price > last_ma5:
#         return True;
#     else :
#         return False;

# tickers = pybit.get_tickers();

# for index, ticker in enumerate(tickers):
#     if(index == 20): break;
    
#     print(ticker, end="");
#     if(increase_marker(ticker)):
#         print(" : 상승장");
#     else :
#         print(" : 하락장");








