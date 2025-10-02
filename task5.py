import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

df = pd.read_csv('BTC_data.csv', names=['Date', 'Open', 'High', 'Low', 'Close'],
                 parse_dates=['Date'])

df = df.sort_values('Date')

plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Close'], label='Bitcoin Price (Close)', color='blue')

date_format = DateFormatter("%d-%m-%y")
plt.gca().xaxis.set_major_formatter(date_format)

plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Historical Price (2018-2023)')
plt.legend()

plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.show()