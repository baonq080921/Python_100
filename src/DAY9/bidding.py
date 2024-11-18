import os

def main():

    user_bidder = {}
    while True:
        name_bidders = input("What is your name?: ")
        money_bid = int(input("What is your bid?:$"))
        other_bid = input("Are there any other bidders.Type 'yes' or 'no'.").lower()
        user_bidder[name_bidders] = money_bid
        if other_bid == "yes" or other_bid == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break
    find_highest_bidder(user_bidder)

def  find_highest_bidder(bidding_dictionary):
    # user_winner = ""
    # max_bidding = 0
    # for key in bidding_dictionary:
    #     if bidding_dictionary[key] > max_bidding:
    #         max_bidding = bidding_dictionary[key]
    #         user_winner = key
    # print(f"The winner is {user_winner} with a ${max_bidding}")
    highest_bidder = max([(value,key) for key, value in bidding_dictionary.items()])
    highest_bidder_name = highest_bidder[0]
    highest_bidder_value = highest_bidder[1]
    print(f"The winner is {highest_bidder_name} with a ${highest_bidder_value}")


if __name__ == '__main__':
    main()



