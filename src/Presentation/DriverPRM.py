class DriverPRM(object):
    """
        Class DriverPRM is the 'main' class of the module,
        which contains the main method.
        Interation with the user occurs in this class

    """

    def __init__(self):
        self.share_epics = []
        self.calendar_period = []

    def get_epic_codes_from_user(
            self):  # let's start with return calculators, so they can enter anything between 1-10 EPICs
        print()
        print("if you want to calculate return for a share ......")
        print()
        input_correct = False
        count = 0
        sentinel_value = "-1"

        while not input_correct and count < 10:
            epic = input('Please enter an EPIC code of a share( -1 to finish): ')
            epic = epic.upper().replace(" ", "")
            try:
                if (4 >= len(epic) >= 2) and str(epic).isalpha():
                    self.share_epics.append(epic)
                    count += 1
                    if count == 10:
                        print("You have reached the maximum num of share in a portfolio 10 ")
                        break
                elif epic == sentinel_value:
                    break

                    # addepic = input("If you don;t want to add any more shares type STOP, else carry on:  ")
                    # if addepic == 'stop':
                    #     break
                else:
                    print()
                    print("An EPIC code is an abbreviation 2-4 characters long.  Please  try again.")
                    print()

            except ValueError:
                print()
                print("Invalid entry. You have to enter numbers 0-9. Please try again.")
                print()

    def get_period_from_user(self):
        print()
        print("please enter the assessment period in the following format yyyy-mm-dd......")  # RE-WORD
        print()
        start_date = input("FROM:  ")  # DO ERROR CATCHING
        end_date = input("TO:  ")  # DO ERROR CATCHING

        self.calendar_period.append(start_date)  # ????
        self.calendar_period.append(end_date)

    def get_calendar_period(self):
        return self.calendar_period

    def get_share_epics(self):
        return self.share_epics


# test = DriverPRM()
# test.get_epic_codes_from_user()
# print(test.get_share_epics())
# print(type(test.get_share_epics()))
#
# test.get_period_from_user()
# print(test.get_calendar_period())
