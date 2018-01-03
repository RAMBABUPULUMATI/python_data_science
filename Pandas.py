import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
print(web.__version__)
style.use('ggplot')
df = web.DataReader( 'AAPL', 'google', '2016/1/1', '2017/1/1' )
print(df.head())
#df['Close'].plot()
#plt.show()