#Create a function which takes as input two dicts with structure mentioned,
#then computes and returns the total price of stock.

def get_price(stock_dict, prices_dict):

    total_price = 0

    for good, qty in stock_dict.items():
        if qty > 0:
            if prices_dict.get(good):      #None if we haven`t price for some fruit in stock
                total_price = total_price + prices_dict.get(good)

    return f"Total price of your stock is {total_price}"

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(get_price(stock, prices))