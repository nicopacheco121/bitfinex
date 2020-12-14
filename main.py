import bitfinex
from config import TICKERS

# send the market data to out db:
while True:
  for ticker in TICKERS:
  biftinex.guardado_historico_bitfinex(ticker)



