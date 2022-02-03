import requests
import pandas as pd


def crawler_investing(st_date, end_date):
    headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
    }

    # 以蘋果(AAPL)為例
    payload = {
        'curr_id': '6408',
        'smlID': '1159963',
        'header': 'AAPL历史数据',
        'st_date': st_date,
        'end_date': end_date,
        'interval_sec': 'Daily',
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical_data'
    }

    url = "https://cn.investing.com/instruments/HistoricalDataAjax"
    res = requests.post(url=url, data=payload, headers=headers)
    df_data = pd.read_html(res.text)[0]

    return df_data.to_json(orient='records', force_ascii=False)


if __name__ == '__main__':
    # 指定日期格式：%Y/%m/%d
    print(crawler_investing(st_date='2021/12/01', end_date='2022/01/31'))
