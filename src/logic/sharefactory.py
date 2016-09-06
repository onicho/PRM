from logic.share import Share


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





# x = ShareFactory.create('^FTSE', '2009-01-01','2014-12-31')
#
# for price in x.historical_prices:
#     print(price)
#
#
# print(len(x.historical_prices))




