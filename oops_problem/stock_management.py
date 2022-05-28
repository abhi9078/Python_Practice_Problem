import os
import json


class Stock(object):
    def __init__(self, s_name=None, s_price=None, s_quantity=None):
        self.s_name = s_name
        self.s_price = s_price
        self.s_quantity = s_quantity
        self.stock = {}
        self.filename = 'stock.json'

    def __str__(self):
        return '[Stock_Name: {0} | Stock_price: {1} | Stock_quantity: {2}]'.format(self.s_name, 
                                                                                   self.s_price, self.s_quantity)

    def __repr__(self):
        return '[Stock_Name: {0} | Stock_price: {1} | Stock_quantity: {2}]'.format(self.s_name,
                                                                                   self.s_price, self.s_quantity)

    def add_stock(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                stock_file = open(self.filename, 'r')
                data = json.load(stock_file)
                stock_file.close()
            else:
                stock_file = open(self.filename, 'a')
                data = {}

            contact = self.get_details_from_user()
            data[contact['Stock_Name']] = contact
            stock_file = open(self.filename, 'a')
            json.dump(data, stock_file, indent=2)  # indent is for
            stock_file.close()
            print('Stock Added Successfully!')
        except Exception as e:
            print('There was an error! Contact was not added.')
            print(e)
        # finally:
        #     stock_file.close()

    def get_details_from_user(self):
        try:
            self.stock['Stock_Name'] = str(input('Enter Stock\'s Name: '))
            self.stock['Stock_price'] = int(input('Enter Stock\'s Price: '))
            self.stock['Stock_quantity'] = int(input('Enter Stock\'s Quantity: '))
            return self.stock
        except KeyboardInterrupt as error:
            raise error

    # To display ALL the Stock in our Portfolio
    def display_stock(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            stock_file = open(self.filename, 'r')
            data = json.load(stock_file)
            stock_file.close()
            # print(data)
            if data:
                for records in data.values():
                    print(records)
            stock_file.close()
        else:
            print("No Stock Available, Please Purchase some")


if __name__ == '__main__':
    my_stock = Stock()
    print("1 to Add Stock\n"
          "2 to Display Stock")
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            my_stock.add_stock()
        elif choice == 2:
            my_stock.display_stock()

