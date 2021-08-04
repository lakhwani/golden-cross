import math
import backtrader as bt
from config import ticker

#change order_percentage to cash_used
class GoldenCross(bt.Strategy):
    #parameters:
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', ticker))

    def __init__(self):
        
        self.fast_MA = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname = '50 day moving average'
        )

        self.slow_MA = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname = '200 day moving average'
        )
        self.crossover = bt.indicators.CrossOver(self.fast_MA, self.slow_MA)

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                #golden cross occurs -> buy position
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                #since no fractional shares
                self.size = math.floor(amount_to_invest / self.data.close)
                self.buy(size=self.size)
                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))

        #we have a position
        if self.position.size > 0:
            #if death cross occurs -> sell position
            if self.crossover < 0:
                print("Sell {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.sell(size=self.size)

#buy and hold from the start
class HODL(bt.Strategy):

    def next(self):
        #if don't own anything (no position yet)
        if self.position.size == 0:
            amount = int(self.broker.getcash() / self.data)
            self.buy(size = amount)