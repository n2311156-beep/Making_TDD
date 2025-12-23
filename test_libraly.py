import unittest
from libraly import Libraly,BookStatus


class TestLibraly(unittest.TestCase):

    def setUp(self):
        self.books = {
            "SF": 0,
            "mystery": 0,
            "fantasy": 0
        }
        self.lb = Libraly(self.books)
    
    def test_rent_book(self):
        result = self.lb.rent_book("SF")
        self.assertTrue(result)
        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.LENDING)

    def test_return_book_in_deadline(self):
        self.lb.rent_book("SF")
        result = self.lb.return_book_in_deadline("SF")
        self.assertTrue(result)
        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.AVAILABLE)


    def test_overdue_status(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(10)

        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.OVERDUE)

    def test_return_book_after_deadline(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(10)
        overdue = self.lb.return_book_after_deadline("SF")

        self.assertEqual(overdue, 3)
        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.AVAILABLE)

    def test_rent_lenting_book(self):
        self.lb.rent_book("SF")
        result = self.lb.rent_book("SF")
        self.assertEqual(result, False)

    def test_rent_overdue_book(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(10)
        result = self.lb.rent_book("SF")
        self.assertEqual(result, False)

    def test_pass_days_of_available_book(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(10)
        self.assertEqual(self.lb.days["SF"], 10)
        self.assertEqual(self.lb.days["mystery"], 0)

    def test_rent_invalid_book(self):
        self.assertEqual(self.lb.rent_book("adventure"), 0)

    def test_return_book(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(5)
        self.lb.rent_book("mystery")
        self.lb.pass_days(5)
        self.assertEqual(self.lb.return_book("SF"), 3)
        self.assertEqual(self.lb.return_book("mystery"), True)     

    def test_reset_days(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(5)
        self.lb.rent_book("mystery")
        self.lb.pass_days(5)
        self.lb.return_book("SF")
        self.lb.return_book("mystery")
        self.assertEqual(self.lb.days["SF"], 0)
        self.assertEqual(self.lb.days["mystery"], 0)


if __name__ == "__main__":
    unittest.main()
