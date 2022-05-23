class CFGMerchCashRegister:

    def __init__(self):
        self.total_items = {
            'T-shirt: Who runs the Code? Girls!': 20,
            'mouse carpet': 10,
            'branded power bank': 35,
            'cool laptop stickers': 5,
            'purple cable holder': 7,
        }
        self.total_price = 0
        self.discount = {'CFG15': 0.15, 'CFG35': 0.35, 'CFG50': 0.50}
        self.purchased_items = []


    def add_item(self):
        item = input('Please make your choice from the 5 cool items we offer: T-shirt: Who runs the Code? Girls!, mouse carpet, branded power bank, cool laptop stickers,purple cable holder')
        if item in self.total_items:
            self.purchased_items.append(item)
        add_more_items = input(
            'To add more items type "Add", to remove the item type "Remove", to contunue to payment "Pay", to cancel '
            'order "Cancel" ').capitalize()
        if add_more_items == 'Add':
            self.add_item()
        elif add_more_items == 'Remove':
            self.remove_item()
        elif add_more_items == 'Pay':
            self.showbag_items()
        elif add_more_items == 'Cancel':
            self.cancel_purchase()


    def remove_item(self):
        removed_item = input('Choose an item to remove')
        if removed_item in self.purchased_items:
            self.purchased_items.remove(removed_item)
        next_step = input(
            'To add more items type "Add", to remove the item type "Remove", to continue to payment "Pay", to cancel '
            'order "Cancel" ').capitalize()
        if next_step == 'Add':
            self.add_item()
        elif next_step == 'Remove':
            self.remove_item()
        elif next_step == 'Pay':
            self.showbag_items()
        elif next_step == 'Cancel':
            self.cancel_purchase()


    def apply_discount(self):
        discount_code = input(' Got a discount? Type the code here ')
        if discount_code in self.discount:
            self.total_price = self.total_price * (1 - self.discount[discount_code])
        else:
            print('Something went wrong. Try again?')
        print('You will pay £', self.total_price)
        print('Thanks for your purchase! Come back soon!')


    def get_total(self):
        for purchased_item in self.purchased_items:
            if purchased_item in self.total_items:
                self.total_price = self.total_price + self.total_items[purchased_item]
        print('You will pay £', self.total_price)
        self.apply_discount()


    def showbag_items(self):
        print('Here is what you got: ')
        for purchased_item in self.purchased_items:
            print(purchased_item, '£', self.total_items[purchased_item])
        self.get_total()

    # cancel
    def cancel_purchase(self):
        self.purchased.clear()
        print('Your basket is free to start again')


# ADD
first_buy = CFGMerchCashRegister()
first_buy.add_item()

# EXAMPLE code run:
#
# Please make your choice from the 5 cool items we offer: T-shirt: Who runs the Code? Girls!, mouse carpet, branded power bank, cool laptop stickers,purple cable holdermouse carpet
# To add more items type "Add", to remove the item type "Remove", to contunue to payment "Pay", to cancel order "Cancel" pay
# Here is what you got:
# mouse carpet £ 10
# You will pay £ 10
#  Got a discount? Type the code here CFG15
# You will pay £ 8.5
# Thanks for your purchase! Come back soon!

#

