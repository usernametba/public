import logging
from kiteconnect import KiteConnect
import datetime
import json
import time


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    elif isinstance(x, datetime.date):
        return x.isoformat()
    else:
        raise TypeError("Unknown type")



logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="xxxxxxxxxxxxxxxxxxxxx")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.


kite.set_access_token("zzzzzzzzzzzzzzzzzzzzzzzz")

# Place an order

"""
try:
    order_id = kite.place_order(tradingsymbol="INFY",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_NRML)

    logging.info("Order placed. ID is: {}".format(order_id))
except Exception as e:
    logging.info("Order placement failed: {}".format(e.message))

# Fetch all orders
kite.orders()

# Get instruments
kite.instruments()

# Place an mutual fund order
kite.place_mf_order(
    tradingsymbol="INF090I01239",
    transaction_type=kite.TRANSACTION_TYPE_BUY,
    amount=5000,
    tag="mytag"
)

# Cancel a mutual fund order
kite.cancel_mf_order(order_id="order_id")

# Get mutual fund instruments
kite.mf_instruments()
"""
print(kite.quote("NSE","TCS"))

#print(kite.instruments(exchange="NSE")) #Lists all instruments & their instrument_token
print(kite.mf_sips(sip_id=None))
#print(kite.historical("738561", "2018-01-01", "2018-04-28", day, continuous=False))
print(kite.holdings())
instruments_all=kite.instruments()
instruments_data=json.dumps(instruments_all, sort_keys=True, indent=4,default=datetime_handler)
print (instruments_data)
#Get historical data for Rs. 2000 a month
#print(kite.historical("738561", "2018-01-01", "2018-04-28", day, continuous=False))


# Place an order

def place_order(scrip,transact_type,quant):
    if transact_type==buy_scrip:
        try:
            order_id = kite.place_order(tradingsymbol=scrip,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))
        time.sleep(3600)
        try:
            order_id = kite.place_order(tradingsymbol=scrip,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))

    elif transact_type==sell_scrip:
        try:
            order_id = kite.place_order(tradingsymbol=scrip,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))
        time.sleep(3600)
        try:
            order_id = kite.place_order(tradingsymbol=scrip,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))
