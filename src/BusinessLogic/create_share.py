from BusinessLogic.share import Share


def create_share(str_share_name):
    return Share(str_share_name)


def shares_maker(list_of_epic_strings):
    list_of_shares = []
    for epic in list_of_epic_strings:
        list_of_shares.append(create_share(epic))
    return list_of_shares


#test

mylst = shares_maker(["BP", "SHELL"])

print(mylst)

print(mylst[0].get_historical_prices())




