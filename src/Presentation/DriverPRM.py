class DriverPRM(object):
    """
        Class DriverPRM is the 'main' class of the module,
        which contains the main method.
        Interation with the user occurs in this class

    """

    def __init__(self):
        self.temp_portfolio = []

    def get_epic_codes_from_user(
            self):  # let's start with return calculators, so they can enter anything between 1-10 EPICs
        print()
        print("if you want to calculate return for a share ......")
        input_correct = False
        count = 0

        while not input_correct and count < 10:
            epic = input('Please enter an EPIC code of a share: ')
            epic = epic.upper().replace(" ", "")
            try:
                if (4 >= len(epic) >= 2) and str(epic).isalpha():
                    self.temp_portfolio.append(epic)
                    count += 1
                    if count == 10:
                        print("You have reached the maximum num of share in a portfolio 10 ")
                        break
                    addepic = input("If you don;t want to add any more shares type STOP, else carry on:  ")
                    if addepic == 'stop':
                        break
                else:
                    print()
                    print("An EPIC code is an abbreviation 2-4 characters long.  Please  try again.")
                    print()

            except ValueError:
                print()
                print("Invalid entry. You have to enter numbers 0-9. Please try again.")
                print()

    def get_temp_portfolio(self):
        return self.temp_portfolio


test = DriverPRM()
test.get_epic_codes_from_user()
print(test.get_temp_portfolio())
