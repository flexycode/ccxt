# -*- coding: utf-8 -*-

from ccxt.async.hitbtc import hitbtc
import base64
import math
import json
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import OrderNotFound


class hitbtc2 (hitbtc):

    def describe(self):
        return self.deep_extend(super(hitbtc2, self).describe(), {
            'id': 'hitbtc2',
            'name': 'HitBTC v2',
            'countries': 'HK',  # Hong Kong
            'rateLimit': 1500,
            'version': '2',
            'hasCORS': True,
            # older metainfo interface
            'hasFetchOHLCV': True,
            'hasFetchTickers': True,
            'hasFetchOrder': True,
            'hasFetchOrders': False,
            'hasFetchOpenOrders': True,
            'hasFetchClosedOrders': True,
            'hasFetchMyTrades': True,
            'hasWithdraw': True,
            'hasFetchCurrencies': True,
            # new metainfo interface
            'has': {
                'fetchCurrencies': True,
                'fetchOHLCV': True,
                'fetchTickers': True,
                'fetchOrder': True,
                'fetchOrders': False,
                'fetchOpenOrders': True,
                'fetchClosedOrders': True,
                'fetchMyTrades': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': 'M1',
                '3m': 'M3',
                '5m': 'M5',
                '15m': 'M15',
                '30m': 'M30',  # default
                '1h': 'H1',
                '4h': 'H4',
                '1d': 'D1',
                '1w': 'D7',
                '1M': '1M',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27766555-8eaec20e-5edc-11e7-9c5b-6dc69fc42f5e.jpg',
                'api': 'https://api.hitbtc.com',
                'www': 'https://hitbtc.com',
                'doc': 'https://api.hitbtc.com',
            },
            'api': {
                'public': {
                    'get': [
                        'symbol',  # Available Currency Symbols
                        'symbol/{symbol}',  # Get symbol info
                        'currency',  # Available Currencies
                        'currency/{currency}',  # Get currency info
                        'ticker',  # Ticker list for all symbols
                        'ticker/{symbol}',  # Ticker for symbol
                        'trades/{symbol}',  # Trades
                        'orderbook/{symbol}',  # Orderbook
                        'candles/{symbol}',  # Candles
                    ],
                },
                'private': {
                    'get': [
                        'order',  # List your current open orders
                        'order/{clientOrderId}',  # Get a single order by clientOrderId
                        'trading/balance',  # Get trading balance
                        'trading/fee/{symbol}',  # Get trading fee rate
                        'history/trades',  # Get historical trades
                        'history/order',  # Get historical orders
                        'history/order/{id}/trades',  # Get historical trades by specified order
                        'account/balance',  # Get main acccount balance
                        'account/transactions',  # Get account transactions
                        'account/transactions/{id}',  # Get account transaction by id
                        'account/crypto/address/{currency}',  # Get deposit crypro address
                    ],
                    'post': [
                        'order',  # Create new order
                        'account/crypto/withdraw',  # Withdraw crypro
                        'account/crypto/address/{currency}',  # Create new deposit crypro address
                        'account/transfer',  # Transfer amount to trading
                    ],
                    'put': [
                        'order/{clientOrderId}',  # Create new order
                        'account/crypto/withdraw/{id}',  # Commit withdraw crypro
                    ],
                    'delete': [
                        'order',  # Cancel all open orders
                        'order/{clientOrderId}',  # Cancel order
                        'account/crypto/withdraw/{id}',  # Rollback withdraw crypro
                    ],
                    'patch': [
                        'order/{clientOrderId}',  # Cancel Replace order
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': -0.01 / 100,
                    'taker': 0.1 / 100,
                },
                'funding': {
                    'tierBased': False,
                    'percentage': False,
                    'withdraw': {
                        'BTC': 0.0009,
                        'ETH': 0.00958,
                        'BCH': 0.0018,
                        'USDT': 5,
                        'BTG': 0.0005,
                        'LTC': 0.003,
                        'ZEC': 0.0001,
                        'XMR': 0.09,
                        '1ST': 0.84,
                        'ADX': 5.7,
                        'AE': 6.7,
                        'AEON': 0.01006,
                        'AIR': 565,
                        'AMP': 9,
                        'ANT': 6.7,
                        'ARDR': 2,
                        'ARN': 18.5,
                        'ART': 26,
                        'ATB': 0.0004,
                        'ATL': 27,
                        'ATM': 504,
                        'ATS': 860,
                        'AVT': 1.9,
                        'BAS': 113,
                        'BCN': 0.1,
                        'BET': 124,
                        'BKB': 46,
                        'BMC': 32,
                        'BMT': 100,
                        'BNT': 2.57,
                        'BQX': 4.7,
                        'BTM': 40,
                        'BTX': 0.04,
                        'BUS': 0.004,
                        'CCT': 115,
                        'CDT': 100,
                        'CDX': 30,
                        'CFI': 61,
                        'CLD': 0.88,
                        'CND': 574,
                        'CNX': 0.04,
                        'COSS': 65,
                        'CSNO': 16,
                        'CTR': 15,
                        'CTX': 146,
                        'CVC': 8.46,
                        'DBIX': 0.0168,
                        'DCN': 120000,
                        'DCT': 0.02,
                        'DDF': 342,
                        'DENT': 6240,
                        'DGB': 0.4,
                        'DGD': 0.01,
                        'DICE': 0.32,
                        'DLT': 0.26,
                        'DNT': 0.21,
                        'DOGE': 2,
                        'DOV': 34,
                        'DRPU': 24,
                        'DRT': 240,
                        'DSH': 0.017,
                        'EBET': 84,
                        'EBTC': 20,
                        'EBTCOLD': 6.6,
                        'ECAT': 14,
                        'EDG': 2,
                        'EDO': 2.9,
                        'ELE': 0.00172,
                        'ELM': 0.004,
                        'EMC': 0.03,
                        'EMGO': 14,
                        'ENJ': 163,
                        'EOS': 1.5,
                        'ERO': 34,
                        'ETBS': 15,
                        'ETC': 0.002,
                        'ETP': 0.004,
                        'EVX': 5.4,
                        'EXN': 456,
                        'FRD': 65,
                        'FUEL': 123.00105,
                        'FUN': 202.9598309,
                        'FYN': 1.849,
                        'FYP': 66.13,
                        'GNO': 0.0034,
                        'GUP': 4,
                        'GVT': 1.2,
                        'HAC': 144,
                        'HDG': 7,
                        'HGT': 1082,
                        'HPC': 0.4,
                        'HVN': 120,
                        'ICN': 0.55,
                        'ICO': 34,
                        'ICOS': 0.35,
                        'IND': 76,
                        'INDI': 5913,
                        'ITS': 15.0012,
                        'IXT': 11,
                        'KBR': 143,
                        'KICK': 112,
                        'LA': 41,
                        'LAT': 1.44,
                        'LIFE': 13000,
                        'LRC': 27,
                        'LSK': 0.3,
                        'LUN': 0.34,
                        'MAID': 5,
                        'MANA': 143,
                        'MCAP': 5.44,
                        'MIPS': 43,
                        'MNE': 1.33,
                        'MSP': 121,
                        'MTH': 92,
                        'MYB': 3.9,
                        'NDC': 165,
                        'NEBL': 0.04,
                        'NET': 3.96,
                        'NTO': 998,
                        'NXC': 13.39,
                        'NXT': 3,
                        'OAX': 15,
                        'ODN': 0.004,
                        'OMG': 2,
                        'OPT': 335,
                        'ORME': 2.8,
                        'OTN': 0.57,
                        'PAY': 3.1,
                        'PIX': 96,
                        'PLBT': 0.33,
                        'PLR': 114,
                        'PLU': 0.87,
                        'POE': 784,
                        'POLL': 3.5,
                        'PPT': 2,
                        'PRE': 32,
                        'PRG': 39,
                        'PRO': 41,
                        'PRS': 60,
                        'PTOY': 0.5,
                        'QAU': 63,
                        'QCN': 0.03,
                        'QTUM': 0.04,
                        'QVT': 64,
                        'REP': 0.02,
                        'RKC': 15,
                        'RVT': 14,
                        'SAN': 2.24,
                        'SBD': 0.03,
                        'SCL': 2.6,
                        'SISA': 1640,
                        'SKIN': 407,
                        'SMART': 0.4,
                        'SMS': 0.0375,
                        'SNC': 36,
                        'SNGLS': 4,
                        'SNM': 48,
                        'SNT': 233,
                        'STEEM': 0.01,
                        'STRAT': 0.01,
                        'STU': 14,
                        'STX': 11,
                        'SUB': 17,
                        'SUR': 3,
                        'SWT': 0.51,
                        'TAAS': 0.91,
                        'TBT': 2.37,
                        'TFL': 15,
                        'TIME': 0.03,
                        'TIX': 7.1,
                        'TKN': 1,
                        'TKR': 84,
                        'TNT': 90,
                        'TRST': 1.6,
                        'TRX': 1395,
                        'UET': 480,
                        'UGT': 15,
                        'VEN': 14,
                        'VERI': 0.037,
                        'VIB': 50,
                        'VIBE': 145,
                        'VOISE': 618,
                        'WEALTH': 0.0168,
                        'WINGS': 2.4,
                        'WTC': 0.75,
                        'XAUR': 3.23,
                        'XDN': 0.01,
                        'XEM': 15,
                        'XUC': 0.9,
                        'YOYOW': 140,
                        'ZAP': 24,
                        'ZRX': 23,
                        'ZSC': 191,
                    },
                    'deposit': {
                        'BTC': 0.0003,
                        'ETH': 0,
                        'BCH': 0,
                        'USDT': 0,
                        'BTG': 0,
                        'LTC': 0,
                        'ZEC': 0,
                        'XMR': 0,
                        '1ST': 0,
                        'ADX': 0,
                        'AE': 0,
                        'AEON': 0,
                        'AIR': 0,
                        'AMP': 0,
                        'ANT': 0,
                        'ARDR': 0,
                        'ARN': 0,
                        'ART': 0,
                        'ATB': 0,
                        'ATL': 0,
                        'ATM': 0,
                        'ATS': 0,
                        'AVT': 0,
                        'BAS': 0,
                        'BCN': 0,
                        'BET': 0,
                        'BKB': 0,
                        'BMC': 0,
                        'BMT': 0,
                        'BNT': 0,
                        'BQX': 0,
                        'BTM': 0,
                        'BTX': 0,
                        'BUS': 0,
                        'CCT': 0,
                        'CDT': 0,
                        'CDX': 0,
                        'CFI': 0,
                        'CLD': 0,
                        'CND': 0,
                        'CNX': 0,
                        'COSS': 0,
                        'CSNO': 0,
                        'CTR': 0,
                        'CTX': 0,
                        'CVC': 0,
                        'DBIX': 0,
                        'DCN': 0,
                        'DCT': 0,
                        'DDF': 0,
                        'DENT': 0,
                        'DGB': 0,
                        'DGD': 0,
                        'DICE': 0,
                        'DLT': 0,
                        'DNT': 0,
                        'DOGE': 0,
                        'DOV': 0,
                        'DRPU': 0,
                        'DRT': 0,
                        'DSH': 0,
                        'EBET': 0,
                        'EBTC': 0,
                        'EBTCOLD': 0,
                        'ECAT': 0,
                        'EDG': 0,
                        'EDO': 0,
                        'ELE': 0,
                        'ELM': 0,
                        'EMC': 0,
                        'EMGO': 0,
                        'ENJ': 0,
                        'EOS': 0,
                        'ERO': 0,
                        'ETBS': 0,
                        'ETC': 0,
                        'ETP': 0,
                        'EVX': 0,
                        'EXN': 0,
                        'FRD': 0,
                        'FUEL': 0,
                        'FUN': 0,
                        'FYN': 0,
                        'FYP': 0,
                        'GNO': 0,
                        'GUP': 0,
                        'GVT': 0,
                        'HAC': 0,
                        'HDG': 0,
                        'HGT': 0,
                        'HPC': 0,
                        'HVN': 0,
                        'ICN': 0,
                        'ICO': 0,
                        'ICOS': 0,
                        'IND': 0,
                        'INDI': 0,
                        'ITS': 0,
                        'IXT': 0,
                        'KBR': 0,
                        'KICK': 0,
                        'LA': 0,
                        'LAT': 0,
                        'LIFE': 0,
                        'LRC': 0,
                        'LSK': 0,
                        'LUN': 0,
                        'MAID': 0,
                        'MANA': 0,
                        'MCAP': 0,
                        'MIPS': 0,
                        'MNE': 0,
                        'MSP': 0,
                        'MTH': 0,
                        'MYB': 0,
                        'NDC': 0,
                        'NEBL': 0,
                        'NET': 0,
                        'NTO': 0,
                        'NXC': 0,
                        'NXT': 0,
                        'OAX': 0,
                        'ODN': 0,
                        'OMG': 0,
                        'OPT': 0,
                        'ORME': 0,
                        'OTN': 0,
                        'PAY': 0,
                        'PIX': 0,
                        'PLBT': 0,
                        'PLR': 0,
                        'PLU': 0,
                        'POE': 0,
                        'POLL': 0,
                        'PPT': 0,
                        'PRE': 0,
                        'PRG': 0,
                        'PRO': 0,
                        'PRS': 0,
                        'PTOY': 0,
                        'QAU': 0,
                        'QCN': 0,
                        'QTUM': 0,
                        'QVT': 0,
                        'REP': 0,
                        'RKC': 0,
                        'RVT': 0,
                        'SAN': 0,
                        'SBD': 0,
                        'SCL': 0,
                        'SISA': 0,
                        'SKIN': 0,
                        'SMART': 0,
                        'SMS': 0,
                        'SNC': 0,
                        'SNGLS': 0,
                        'SNM': 0,
                        'SNT': 0,
                        'STEEM': 0,
                        'STRAT': 0,
                        'STU': 0,
                        'STX': 0,
                        'SUB': 0,
                        'SUR': 0,
                        'SWT': 0,
                        'TAAS': 0,
                        'TBT': 0,
                        'TFL': 0,
                        'TIME': 0,
                        'TIX': 0,
                        'TKN': 0,
                        'TKR': 0,
                        'TNT': 0,
                        'TRST': 0,
                        'TRX': 0,
                        'UET': 0,
                        'UGT': 0,
                        'VEN': 0,
                        'VERI': 0,
                        'VIB': 0,
                        'VIBE': 0,
                        'VOISE': 0,
                        'WEALTH': 0,
                        'WINGS': 0,
                        'WTC': 0,
                        'XAUR': 0,
                        'XDN': 0,
                        'XEM': 0,
                        'XUC': 0,
                        'YOYOW': 0,
                        'ZAP': 0,
                        'ZRX': 0,
                        'ZSC': 0,
                    },
                },
            },
        })

    def currency_id(self, currency):
        if currency == 'BitClave':
            return 'CAT'
        return currency

    def fee_to_precision(self, symbol, fee):
        return self.truncate(fee, 8)

    async def fetch_markets(self):
        markets = await self.publicGetSymbol()
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = market['id']
            baseId = market['baseCurrency']
            quoteId = market['quoteCurrency']
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = base + '/' + quote
            lot = float(market['quantityIncrement'])
            step = float(market['tickSize'])
            precision = {
                'price': self.precision_from_string(market['tickSize']),
                'amount': self.precision_from_string(market['quantityIncrement']),
            }
            taker = float(market['takeLiquidityRate'])
            maker = float(market['provideLiquidityRate'])
            result.append(self.extend(self.fees['trading'], {
                'info': market,
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': True,
                'lot': lot,
                'step': step,
                'taker': taker,
                'maker': maker,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': lot,
                        'max': None,
                    },
                    'price': {
                        'min': step,
                        'max': None,
                    },
                    'cost': {
                        'min': lot * step,
                        'max': None,
                    },
                },
            }))
        return result

    async def fetch_currencies(self, params={}):
        currencies = await self.publicGetCurrency(params)
        result = {}
        for i in range(0, len(currencies)):
            currency = currencies[i]
            id = currency['id']
            # todo: will need to rethink the fees
            # to add support for multiple withdrawal/deposit methods and
            # differentiated fees for each particular method
            precision = 8  # default precision, todo: fix "magic constants"
            code = self.common_currency_code(id)
            payin = currency['payinEnabled']
            payout = currency['payoutEnabled']
            transfer = currency['transferEnabled']
            active = payin and payout and transfer
            status = 'ok'
            if 'disabled' in currency:
                if currency['disabled']:
                    status = 'disabled'
            type = 'crypto' if (currency['crypto']) else 'fiat'
            result[code] = {
                'id': id,
                'code': code,
                'type': type,
                'payin': payin,
                'payout': payout,
                'transfer': transfer,
                'info': currency,
                'name': currency['fullName'],
                'active': active,
                'status': status,
                'fee': None,  # todo: redesign
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': math.pow(10, -precision),
                        'max': math.pow(10, precision),
                    },
                    'price': {
                        'min': math.pow(10, -precision),
                        'max': math.pow(10, precision),
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                    'withdraw': {
                        'min': None,
                        'max': math.pow(10, precision),
                    },
                },
            }
        return result

    async def fetch_balance(self, params={}):
        await self.load_markets()
        type = self.safe_string(params, 'type', 'trading')
        method = 'privateGet' + self.capitalize(type) + 'Balance'
        balances = await getattr(self, method)()
        result = {'info': balances}
        for b in range(0, len(balances)):
            balance = balances[b]
            code = balance['currency']
            currency = self.common_currency_code(code)
            account = {
                'free': float(balance['available']),
                'used': float(balance['reserved']),
                'total': 0.0,
            }
            account['total'] = self.sum(account['free'], account['used'])
            result[currency] = account
        return self.parse_balance(result)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1d', since=None, limit=None):
        timestamp = self.parse8601(ohlcv['timestamp'])
        return [
            timestamp,
            float(ohlcv['open']),
            float(ohlcv['max']),
            float(ohlcv['min']),
            float(ohlcv['close']),
            float(ohlcv['volumeQuote']),
        ]

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'period': self.timeframes[timeframe],
        }
        if limit:
            request['limit'] = limit
        response = await self.publicGetCandlesSymbol(self.extend(request, params))
        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    async def fetch_order_book(self, symbol, params={}):
        await self.load_markets()
        orderbook = await self.publicGetOrderbookSymbol(self.extend({
            'symbol': self.market_id(symbol),
            # 'limit': 100,  # default = 100, 0 = unlimited
        }, params))
        return self.parse_order_book(orderbook, None, 'bid', 'ask', 'price', 'size')

    def parse_ticker(self, ticker, market=None):
        timestamp = self.parse8601(ticker['timestamp'])
        symbol = None
        if market:
            symbol = market['symbol']
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'bid'),
            'ask': self.safe_float(ticker, 'ask'),
            'vwap': None,
            'open': self.safe_float(ticker, 'open'),
            'close': self.safe_float(ticker, 'close'),
            'first': None,
            'last': self.safe_float(ticker, 'last'),
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_float(ticker, 'volume'),
            'quoteVolume': self.safe_float(ticker, 'volumeQuote'),
            'info': ticker,
        }

    async def fetch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        tickers = await self.publicGetTicker(params)
        result = {}
        for i in range(0, len(tickers)):
            ticker = tickers[i]
            id = ticker['symbol']
            market = self.markets_by_id[id]
            symbol = market['symbol']
            result[symbol] = self.parse_ticker(ticker, market)
        return result

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        ticker = await self.publicGetTickerSymbol(self.extend({
            'symbol': market['id'],
        }, params))
        if 'message' in ticker:
            raise ExchangeError(self.id + ' ' + ticker['message'])
        return self.parse_ticker(ticker, market)

    def parse_trade(self, trade, market=None):
        timestamp = self.parse8601(trade['timestamp'])
        symbol = None
        if market:
            symbol = market['symbol']
        else:
            id = trade['symbol']
            if id in self.markets_by_id:
                market = self.markets_by_id[id]
                symbol = market['symbol']
            else:
                symbol = id
        fee = None
        if 'fee' in trade:
            currency = market['quote'] if market else None
            fee = {
                'cost': float(trade['fee']),
                'currency': currency,
            }
        orderId = None
        if 'clientOrderId' in trade:
            orderId = trade['clientOrderId']
        price = float(trade['price'])
        amount = float(trade['quantity'])
        cost = price * amount
        return {
            'info': trade,
            'id': str(trade['id']),
            'order': orderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': trade['side'],
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        response = await self.publicGetTradesSymbol(self.extend({
            'symbol': market['id'],
        }, params))
        return self.parse_trades(response, market, since, limit)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        # their max accepted length is 32 characters
        uuid = self.uuid()
        parts = uuid.split('-')
        clientOrderId = ''.join(parts)
        clientOrderId = clientOrderId[0:32]
        amount = float(amount)
        request = {
            'clientOrderId': clientOrderId,
            'symbol': market['id'],
            'side': side,
            'quantity': self.amount_to_precision(symbol, amount),
            'type': type,
        }
        if type == 'limit':
            request['price'] = self.price_to_precision(symbol, price)
        else:
            request['timeInForce'] = 'FOK'
        response = await self.privatePostOrder(self.extend(request, params))
        order = self.parse_order(response)
        id = order['id']
        self.orders[id] = order
        return order

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        return await self.privateDeleteOrderClientOrderId(self.extend({
            'clientOrderId': id,
        }, params))

    def parse_order(self, order, market=None):
        created = None
        if 'createdAt' in order:
            created = self.parse8601(order['createdAt'])
        updated = None
        if 'updatedAt' in order:
            updated = self.parse8601(order['updatedAt'])
        if not market:
            market = self.markets_by_id[order['symbol']]
        symbol = market['symbol']
        amount = self.safe_float(order, 'quantity')
        filled = self.safe_float(order, 'cumQuantity')
        status = order['status']
        if status == 'new':
            status = 'open'
        elif status == 'suspended':
            status = 'open'
        elif status == 'partiallyFilled':
            status = 'open'
        elif status == 'filled':
            status = 'closed'
        id = str(order['clientOrderId'])
        price = self.safe_float(order, 'price')
        if price is None:
            if id in self.orders:
                price = self.orders[id]['price']
        remaining = None
        cost = None
        if amount is not None:
            if filled is not None:
                remaining = amount - filled
                if price is not None:
                    cost = filled * price
        return {
            'id': id,
            'timestamp': created,
            'datetime': self.iso8601(created),
            'created': created,
            'updated': updated,
            'status': status,
            'symbol': symbol,
            'type': order['type'],
            'side': order['side'],
            'price': price,
            'amount': amount,
            'cost': cost,
            'filled': filled,
            'remaining': remaining,
            'fee': None,
            'info': order,
        }

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        response = await self.privateGetHistoryOrder(self.extend({
            'clientOrderId': id,
        }, params))
        numOrders = len(response)
        if numOrders > 0:
            return self.parse_order(response[0])
        raise OrderNotFound(self.id + ' order ' + id + ' not found')

    async def fetch_open_order(self, id, symbol=None, params={}):
        await self.load_markets()
        response = await self.privateGetOrderClientOrderId(self.extend({
            'clientOrderId': id,
        }, params))
        return self.parse_order(response)

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = None
        request = {}
        if symbol:
            market = self.market(symbol)
            request['symbol'] = market['id']
        response = await self.privateGetOrder(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = None
        request = {}
        if symbol:
            market = self.market(symbol)
            request['symbol'] = market['id']
        if limit:
            request['limit'] = limit
        if since:
            request['from'] = self.iso8601(since)
        response = await self.privateGetHistoryOrder(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        request = {
            # 'symbol': 'BTC/USD',  # optional
            # 'sort': 'DESC',  # or 'ASC'
            # 'by': 'timestamp',  # or 'id'	String	timestamp by default, or id
            # 'from':	'Datetime or Number',  # ISO 8601
            # 'till':	'Datetime or Number',
            # 'limit': 100,
            # 'offset': 0,
        }
        market = None
        if symbol:
            market = self.market(symbol)
            request['symbol'] = market['id']
        if since:
            request['from'] = self.iso8601(since)
        if limit:
            request['limit'] = limit
        response = await self.privateGetHistoryTrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    async def fetch_order_trades(self, id, symbol=None, params={}):
        # The id needed here is the exchange's id, and not the clientOrderID, which is
        # the id that is stored in the unified api order id. In order the get the exchange's id,
        # you need to grab it from order['info']['id']
        await self.load_markets()
        trades = await self.privateGetHistoryOrderIdTrades(self.extend({
            'id': id,
        }, params))
        return self.parse_trades(trades)

    async def create_deposit_address(self, currency, params={}):
        currencyId = self.currency_id(currency)
        response = await self.privatePostAccountCryptoAddressCurrency({
            'currency': currencyId,
        })
        address = response['address']
        return {
            'currency': currency,
            'address': address,
            'status': 'ok',
            'info': response,
        }

    async def fetch_deposit_address(self, currency, params={}):
        currencyId = self.currency_id(currency)
        response = await self.privateGetAccountCryptoAddressCurrency({
            'currency': currencyId,
        })
        address = response['address']
        return {
            'currency': currency,
            'address': address,
            'status': 'ok',
            'info': response,
        }

    async def withdraw(self, code, amount, address, params={}):
        currency = self.currency(code)
        response = await self.privatePostAccountCryptoWithdraw(self.extend({
            'currency': currency['id'],
            'amount': float(amount),
            'address': address,
        }, params))
        return {
            'info': response,
            'id': response['id'],
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = '/api' + '/' + self.version + '/'
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            url += api + '/' + self.implode_params(path, params)
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            url += self.implode_params(path, params)
            if method == 'GET':
                if query:
                    url += '?' + self.urlencode(query)
            else:
                if query:
                    body = self.json(query)
            payload = self.encode(self.apiKey + ':' + self.secret)
            auth = base64.b64encode(payload)
            headers = {
                'Authorization': "Basic " + self.decode(auth),
                'Content-Type': 'application/json',
            }
        url = self.urls['api'] + url
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body):
        if code == 400:
            if body[0] == "{":
                response = json.loads(body)
                if 'error' in response:
                    if 'message' in response['error']:
                        message = response['error']['message']
                        if message == 'Order not found':
                            raise OrderNotFound(self.id + ' order not found in active orders')
                        elif message == 'Insufficient funds':
                            raise InsufficientFunds(self.id + ' ' + message)
            raise ExchangeError(self.id + ' ' + body)

    async def request(self, path, api='public', method='GET', params={}, headers=None, body=None, proxy=''):
        response = await self.fetch2(path, api, method, params, headers, body, proxy)
        if 'error' in response:
            raise ExchangeError(self.id + ' ' + self.json(response))
        return response
