import pyodbc
from datetime import *
from colorama import *


def get_tickers():
    """
    Gets user input, i.e. EPIC codes (tickers) of the shares to be processed

    :return: a list of share EPIC codes
    :rtype: list[str]
    """
    tickers = []

    correct = False
    count = 0
    sentinel = "0"

    while not correct and count < 10:
        #print()
        ticker = input(Fore.LIGHTGREEN_EX +
                       'Please enter an EPIC code of a share( or 0 to finish):')
        print('\033[30m')
        ticker = ticker.upper().replace(" ", "")
        try:
            if valid(ticker) and ticker not in tickers:
                tickers.append(ticker)
                count += 1
                if count == 10:
                    print(
                        "You have reached the maximum number of shares for "
                        "processing by the PRM system")
                    return tickers

            elif ticker == sentinel:
                return tickers

            else:
                print()
                print('\033[31m' + "Invalid entry.")
                print('\033[30m')
                print("Possible reasons: ")
                print("     * EPIC has already been entered")
                print("     * EPIC is spelt incorrectly.")
                print("     * EPIC is not in FTSE100 or not in PRM database")
                raise ValueError

        except ValueError:
            print()
            print("Try again or enter 0 (zero) to stop input")
            print()


def valid(ticker):
    """
    Checks that entered EPIC copde exists in the PRM database

    :param ticker: EPIC code / ticker of a share
    :type ticker: str (for example "BP", "LLOY")
    :return: boolean
    """
    cnxn = pyodbc.connect(
        'driver={SQL Server};server=localhost;database=PRM;'
        'Integrated Security=True')

    cursor = cnxn.cursor()
    cursor.execute("SELECT distinct epic FROM [dbo].[SHARE]")

    if ticker.upper() in [ticker[0] for ticker in cursor.fetchall()]:
        return True
    else:
        return False


print(get_tickers())



# def get_period_from_user(self):
#     today = date.today()
#     calendar_period = []
#     print()
#     print(
#         "please enter the assessment period in the following format yyyy-mm-dd......")  # RE-WORD
#     print()
#
#     input_correct = False
#
#     while not input_correct:
#         print()
#         start_date = str(input("FROM:  ")).replace(" ", "")  # DO ERROR CATCHING
#
#         if self.valid_date(start_date):
#             if datetime.strptime(start_date, "%Y-%m-%d").date() < today:
#                 calendar_period.append(start_date)
#                 # input_correct = True
#                 break
#
#             else:
#                 print(
#                     "The date you entered appears to be today's date or the one in the future")
#                 print(
#                     "No stock prices are available yet. Please enter an earlier date.")
#
#         else:
#             print("Invalid entry. Please check the format of your date")
#             print("The time period should be between 2009-01-01 and " + str(
#                 today))
#
#     while not input_correct:
#         print()
#         end_date = str(input("TO:  ")).replace(" ", "")  # DO ERROR CATCHING
#
#         if self.valid_date(end_date):
#             if datetime.strptime(calendar_period[0], "%Y-%m-%d").date() < \
#                     datetime.strptime(end_date, "%Y-%m-%d").date() < today:
#                 calendar_period.append(end_date)
#                 input_correct = True
#             else:
#                 print(
#                     "Dates inconsistency. The end date cannot precede the start date. ")
#                 print("Also the end date cannot be a future or today's date.")
#
#         else:
#             print("Invalid entry. Please check the format of your date")
#             print("The time period should be between 2009-01-01 and " + str(
#                 date.today()))
#     return calendar_period
#
#
#
#
#
#
#
#
# def valid_date(date):
#     cnxn = pyodbc.connect(
#         'driver={SQL Server};server=localhost;database=PRM;Integrated Security=True')
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT distinct CALENDAR_DATE FROM [dbo].[CALENDAR]")
#     if date in [date[0] for date in cursor.fetchall()]:
#         return True
#     else:
#         return False
#
#
# def risk_free_rate():
#     input_correct = False
#
#     while not input_correct:
#
#         try:
#             rfr = float(
#                 (input("Risk Free Rate as percentage % :  ")).replace(" ", ""))
#             if 0 < rfr < 100:
#                 input_correct = True
#             else:
#                 print(
#                     "The risk free percentage is a number that is more than 0% but less than 100%. Try again")
#
#         except ValueError:
#             print("The risk free rate must be a number. Please try again")
#
#     return rfr




