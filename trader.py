import os, sys, argparse
from backtrader import strategy
import pandas as pd
import backtrader as bt
from strategies import GoldenCross, HODL
from config import ticker

#UI
strategies = {
    "goldencross": GoldenCross,
    "hodl": HODL
}

parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="Which strategy to run?", type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("Error: Invalid Strategy! Must be one of: {}".format(strategies.keys()))
    sys.exit()

#choose crypto/stock of choice
data = ticker

#brain behind the backtrader and set starting cash
cerebro = bt.Cerebro()
cerebro.broker.set_cash(100000)

#price insertion
prices = pd.read_csv('data/{}.csv'.format(data), index_col='Date', parse_dates=True)
feed = bt.feeds.PandasData(dataname = prices)
cerebro.adddata(feed)

#strategy of choice -> run -> graph plot
cerebro.addstrategy(strategies[args.strategy])
cerebro.run()
cerebro.plot()