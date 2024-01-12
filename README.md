# Golden Cross Strategy Backtester for S&P 500

## Overview
This Python script is developed to backtest the Golden Cross trading strategy specifically on the S&P 500 index. The Golden Cross strategy is a popular trading signal that occurs when a short-term moving average crosses above a long-term moving average, indicating a potential bullish turn in the market.

## Features
- **Data Fetching**: Automatically retrieves historical data of the S&P 500.
- **Moving Averages Calculation**: Calculates the short-term and long-term moving averages.
- **Signal Identification**: Identifies Golden Cross and Death Cross signals.
- **Performance Metrics**: Evaluates the performance of the strategy over time.

## Requirements
- Python 3.x
- Pandas: For data manipulation and analysis.
- Matplotlib: For plotting graphs and visualizing data.

## Installation
1. Clone the repository:
2. Install the required packages:
   ```
   pip install pandas matplotlib
   ```

## Usage
Run the script with:
```
python trader.py
```

## Configuration
You can configure the following parameters in the script:
- Short-term moving average period (default: 50 days)
- Long-term moving average period (default: 200 days)

## Output
The script outputs:
- A graph showing the S&P 500 price along with the short-term and long-term moving averages.
- Trading signals (Golden Cross and Death Cross points).
- The overall profit or loss from following this strategy.

## Disclaimer
This script is for educational purposes only and is not intended as financial advice. Past performance is not indicative of future results.

## Contributions
Contributions are welcome. Please feel free to submit a pull request or open an issue.
