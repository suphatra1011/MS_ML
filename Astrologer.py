import argparse
import sys

"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day) -> str:
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    
    return "一個星座"


def get_each_number(number: int) -> []:
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920) 
    return [1,9,2,0]
    """
    #number = 
    #result = [1,2,3]


    return result


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """
    year/1000

    life_num = 10

    return life_num

def parseArgs():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('integer', type=int, help='Enter the birthday date')
    # args = parser.parse_args()
    # print(args.integer) 
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int, help='The year of birth')
    parser.add_argument('month', type=int, help='The month of birth')
    parser.add_argument('day', type=int, help='The day of birth')
    args = parser.parse_args()
    #print(args.year)
    #print(args.month)
    #print(args.day)
    return args


def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-y", "--year" , type=int, help="The year of birth.")
    parser.add_argument("-m", "--month", type=int, help="The month of birth.")
    parser.add_argument("-d", "--day"  , type=int, help="The day of birth.")
    #parser.add_argument("-v", "--verbose",dest='verbose',action='store_true', help="Verbose mode.")
    options = parser.parse_args(args)
    return options

if __name__ == '__main__':    
    args=parseArgs()
    #opt=getOptions()
    #get_each_number(opt)
    #month = int(input('請輸入月份（例如：5）：'))
