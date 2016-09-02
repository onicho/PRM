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


class ShareFactory(object):
    @staticmethod
    def create(ticker):
        s = Share(ticker)
        dbo = Database(connection)
        # can also look up descriptors
        s.historical_price = dbo.get_historical_price(ticker)
        return s



# test

mylst = ShareGenerator.shares_maker(["ERM", "AML", "CGL", "NG"])

print(type(mylst[0]))

#print(mylst[0].get_historical_prices())

shares = [Share(x) for x in ["ERM", "AML"]]