from unittest import TestCase
from data.datatransfer import *


class TestUpdate_db(TestCase):

    def test_update_db(self):

        d = '2014-05-11'
        d1 = 2015

        self.assertRaises(InputError, update_db, d, d1)

        d2 = '11-05-2016'
        d3 = '2016-05-20'

        self.assertRaises(ValueError, update_db, d2, d3)

    def test_db_connection(self):
        """
        Checks if connection with database is established
        """

        cnxn = pyodbc.connect(
            'driver={SQL Server};server=localhost;database=PRM;'
            'Integrated Security=True')

        cursor = cnxn.cursor()

        cursor.execute("SELECT distinct epic FROM [dbo].[SHARE]")
        results = cursor.fetchall()

        # checks if anything at all is returned by the call
        self.assertTrue(results)








