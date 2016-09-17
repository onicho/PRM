import pyodbc
from datetime import *
from colorama import *
import re


def get_tickers():
    """
    Prompts user input, and accepts EPIC codes (tickers) of the shares to be
    processed

    :return: a list of share EPIC codes
    :rtype: list[str]
    """
    tickers = []

    correct = False
    count = 0
    sentinel = "0"

    while not correct and count < 10:
        print()
        ticker = input(Fore.LIGHTGREEN_EX +
                       'Please enter an EPIC code of a share( or 0 to finish):'
                       + '\033[30m')
        ticker = ticker.upper().replace(" ", "")

        if valid_epic(ticker) and ticker not in tickers:
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
            print('\033[31m' + "Invalid entry." + '\033[30m')
            print("Possible reasons: ")
            print("     * EPIC has already been entered")
            print("     * EPIC is spelt incorrectly.")
            print("     * EPIC is not in FTSE100 or not in the PRM database")


def valid_epic(ticker):
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


def get_period():
    """
    Prompts user input to for the start date and the end date of the time period
    that is used by class ShareFactory to create shares.

    :return: start and end dates of the time period in the 'yyyy-mm-dd' format
    :rtype: list[str]
    """
    today = date.today()
    days = timedelta(days=31)
    delta = today - days

    period = []

    print()
    # print("Enter start and end dates in the following format" + '\033[4m' +
    #       " yyyy-mm-dd " + '\033[30m')

    correct = False

    while not correct:
        print()

        start = str(input(Fore.LIGHTGREEN_EX + "Enter a start date FROM:  " +
                          '\033[30m')).replace(" ", "")

        if valid_date(start):

            if datetime.strptime(start, "%Y-%m-%d").date() <= delta:
                period.append(start)
                break

            else:
                print()
                print('\033[31m' + "Invalid entry." + '\033[30m')
                print("Possible reasons: ")
                print("     *The date appears to be after " +
                      delta.strftime("%Y-%m-%d") +
                      " Enter an earlier date.")

        else:
            print()
            print('\033[31m' + "Invalid entry." + '\033[30m')
            print("     *Please check the format of your date")
            print("     *The date should be between 2009-01-01 and " +
                  delta.strftime("%Y-%m-%d"))

    while not correct:
        print()
        end = str(input(Fore.LIGHTGREEN_EX + "Enter the end date TO:  " +
                        '\033[30m')).replace(" ", "")

        d = datetime.strptime(period[0], "%Y-%m-%d").date()

        if valid_date(end):

            if d + days <= datetime.strptime(end, "%Y-%m-%d").date() < today:

                period.append(end)
                correct = True

            else:
                print()
                print('\033[31m' + "Invalid entry." + '\033[30m')
                print("     *The earliest end date can be " + (d + days).
                      strftime("%Y-%m-%d"))
                print("     *The latest end date can be " + str(today -
                                                                timedelta(
                                                                    days=1)))

                print("     *The current version of the system works with "
                      "monthly share prices")

        else:
            print()
            print('\033[31m' + "Invalid entry." + '\033[30m')
            print("     *Please check the format of your date")
            print("     *The date should be between " +
                  (d + days).strftime("%Y-%m-%d") + " and " + str(date.today() -
                                                                  timedelta(1)))

    return period


def valid_date(dt):
    """
    Checks that entered date exists in the calendar of the PRM database

    :param dt: calendar dtae
    :type dt: str ('yyyy-mm-dd')
    :return: boolean
    """

    cnxn = pyodbc.connect(
        'driver={SQL Server};server=localhost;database=PRM;'
        'Integrated Security=True')
    cursor = cnxn.cursor()

    cursor.execute("SELECT distinct CALENDAR_DATE FROM [dbo].[CALENDAR]")

    if dt in [str(d[0]) for d in cursor.fetchall()]:

        return True

    else:
        return False


def get_rfr():
    """
    Prompts user input - the risk free rate for calculations
    :return: float
    """

    input_correct = False
    risk = 0

    while not input_correct:

        try:
            print()
            rfr = float(
                (input(Fore.LIGHTGREEN_EX +
                       "Enter Risk Free Rate as percentage:  " +
                       '\033[30m')).replace(" ", ""))

            if 0 < rfr < 100:

                risk = rfr
                input_correct = True

            else:
                print()
                print('\033[31m' + "Invalid entry." + '\033[30m')
                print(
                    "     *The percentage value should be a number that is "
                    "higher than 0% but less than 100%")
                print("     *Please try again")

        except ValueError:
            print()
            print('\033[31m' + "Invalid entry." + '\033[30m')
            print("     *Please enter a valid number")

    return risk
