#寫一個function來判斷是不是閏年（二月會多一天的年），

#依照Wikipedia的定義：
#公元年分除以4不可整除，為平年。
#公元年分除以4可整除但除以100不可整除，為閏年。
#公元年分除以100可整除但除以400不可整除，為平年。
#公元年分除以400可整除但除以3200不可整除，為閏年。

#function應該要有一個參數讓使用者投入（傳遞進去）年份，
#function的回傳值(return)應該是布林值，如果是閏年就return True，不是就return False。
#請把function命名為is_leap ，這樣才可以執行測試。（P.S.  is_leap 就是"是不是閏年"的意思，所以function取的名符其實）
#提示：要用到　%　這個符號來＂求餘數＂

def is_leap(year):
	year = int(year)
	if year % 4 != 0:
		print(year, '為平年')
	elif year % 4 == 0 and year % 100 != 0:
		print(year, '為閨年')
	elif year % 100 == 0 and year % 400 != 0:
		print(year, '為平年')
	elif year % 400 == '0' and year % 3200 != 0:
		print(year, '為閨年')
			
year = input('請輸入西元年:')
is_leap(year)				
