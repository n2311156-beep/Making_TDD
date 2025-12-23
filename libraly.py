from enum import Enum

class BookStatus(Enum):
  AVAILABLE = 0
  LENDING = 1
  OVERDUE = 2

class Libraly:
  def __init__(self, books):
    self.books = books
    self.days = {name: 0 for name in books}
  def rent_book(self, name):
    if name not in self.books:
      return False
    if (self.books[name] == BookStatus.LENDING) or (self.books[name] == BookStatus.OVERDUE):
      return False
    self.books[name] = BookStatus.LENDING
    self.days[name] = 0
    return True
  def return_book_in_deadline(self, name):
    self.books[name] = BookStatus.AVAILABLE
    self.days[name] = 0
    return True
  def return_book_after_deadline(self, name):
    overdue = self.days[name] - 7
    self.books[name] = BookStatus.AVAILABLE
    self.days[name] = 0
    return overdue
  def return_book(self,name):
    if self.books[name] == BookStatus.OVERDUE:
      return self.return_book_after_deadline(name)
    elif self.books[name] == BookStatus.LENDING:
      return self.return_book_in_deadline(name)
    else:
      return False

  def get_book_status(self, name):
    return self.books[name]
  def pass_days(self, day):
    for name in self.books:
      if self.books[name] == BookStatus.LENDING:
        self.days[name] += day
        if self.days[name] > 7:
          self.books[name] = BookStatus.OVERDUE
    return True
