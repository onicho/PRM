from BusinessLogic.share import Share


class ShareGenerator:
    @staticmethod
    def create_share(str_share_name):
        return Share(str_share_name)

    @staticmethod
    def shares_maker(list_of_epic_strings):
        list_of_shares = []
        for epic in list_of_epic_strings:
            list_of_shares.append(ShareGenerator.create_share(epic))
        return list_of_shares




# test

mylst = ShareGenerator.shares_maker(["ERM", "AML", "CGL", "NG"])

print(mylst)

print(mylst[0].get_historical_prices())
