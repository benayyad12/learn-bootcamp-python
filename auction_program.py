# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_higher_bidder(bids_dict):
    winner = ""
    max = 0
    for bidder in bids_dict:
        bidder_amount = bids_dict[bidder]
        if bidder_amount > max:
            max = bidder_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {max}")

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

name = input("What is your name? ")
price = int(input("What's your bid?: $"))

bids = {}
bids[name] = price

bidding_continue = input("Is there any other who want to bid? Type 'yes' or 'no' .")
should_continue=True

while should_continue:
    name = input("What is your name? ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    bidding_continue = input("Is there any other who want to bid? Type 'yes' or 'no' .")
    if bidding_continue == 'no':
        should_continue = False
        find_higher_bidder(bids)
    elif bidding_continue == 'yes':
        print("\n" * 20)




