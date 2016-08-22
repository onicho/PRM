from BusinessLogic.share import Share


def create_share(share_name):
    return Share(share_name)


def shares_maker(list_of_epic_strings):
    list_of_shares = []
    for epic in list_of_epic_strings:
        list_of_shares.append(create_share(epic))
    return list_of_shares


#test

print(shares_maker(["BP", "SHELL"]))
for myobject in shares_maker(["BP", "SHELL"]):
    print(type(object), "\n")


