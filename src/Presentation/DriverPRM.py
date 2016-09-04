import pyodbc


class UserInput(object):

    def get_tickers(self):
        tickers = []

        input_correct = False
        count = 0
        sentinel_value = "-1"

        while not input_correct and count < 10:
            print()
            ticker = input('Please enter an EPIC code of a share( -1 to finish): ')
            ticker = ticker.upper().replace(" ", "")
            try:
                if self.valid(ticker) and ticker not in tickers:
                    tickers.append(ticker)
                    count += 1
                    if count == 10:
                        print("You have reached the maximum number of 10 shares in a portfolio")
                        return tickers
                        # break

                elif ticker == sentinel_value:
                    return tickers

                else:
                    print()
                    print("Invalid entry. Possible causes: EPIC already exists or ")
                    print("entered code is incorrect. Refer to the table at the top")

            except ValueError:
                print()
                print("Invalid entry. An EPIC code is a combination of alphabetic characters that represent a share ")
                print()


    @staticmethod
    def get_period_from_user():
        calendar_period = []
        print()
        print("please enter the assessment period in the following format yyyy-mm-dd......")  # RE-WORD
        print()
        start_date = input("FROM:  ")  # DO ERROR CATCHING
        end_date = input("TO:  ")  # DO ERROR CATCHING

        calendar_period.append(start_date)  # ????
        calendar_period.append(end_date)
        return calendar_period

    @staticmethod
    def valid(ticker):
        cnxn = pyodbc.connect('driver={SQL Server};server=localhost;database=PRM;Integrated Security=True')
        cursor = cnxn.cursor()
        cursor.execute("SELECT distinct epic FROM [dbo].[SHARE]")
        if ticker.upper() in [ticker[0] for ticker in cursor.fetchall()]:
            return True
        else:
            return False


test = UserInput()
print(test.get_tickers())
#print(type(test.tickers[1]))

# print(type(test.calendar_period))
# #
# # test.get_period_from_user()
# # print(test.get_calendar_period())
