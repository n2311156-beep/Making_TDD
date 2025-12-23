# 図書館クラス
### 仕様
- 図書館の本は借りることができ、本が貸し出された状態で一定期間が経過すると延滞状態になる。本に対する操作を行う各メソッドは以下のものである。
### メソッド
- 本を貸し出す
  - 入力: 本の名前
  - 出力: 貸し出されたかどうか`True | False`
- 本を返却する
  - 入力: 本の名前
  - 出力: 期限内なら成功フラグ、延滞中なら延滞日数
- 本を期限内に返却する
  - 入力: 本の名前
  - 出力: 返却されたかどうか`True | False`
- 延滞中の本を返却する
  - 入力: 本の名前
  - 出力: 延滞日数
- 本の状態を取得する
  - 入力: 本の名前
  - 出力: 本の状態
- 時間を経過させる
  - 入力:経過させる時間
  - 出力: 成功したかどうか
### テストシナリオ
- 本を借りると本は貸し出し可能状態から貸し出し中状態になる
- 貸し出し中状態の本を返却すると本は貸し出し中状態から貸し出し可能状態になる
- 本を貸し出し中状態にしたまま一定日数が経過すると延滞状態になる
- 延滞状態の本を返却すると延滞日数が返され、本は貸し出し可能状態になる
- 貸し出し中や延滞中の本を借りようとすると失敗し、`false`が返される
- 貸し出し可能状態の本はどれだけ日数を経過させても貸出期間が経過せず、貸し出し可能状態のままである
- 図書館に存在しない本を借りようとすると失敗し、`false`が返される
- 本の返却時にその本の状態をシステムが判定し、期限内の返却と延滞中の本の返却に分岐する
- 返却した本は貸出期間がリセットされる
## TDDサイクル
#### テストケース①: 本を借りると本は貸し出し可能状態から貸し出し中状態になる

```python
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
        self.assertEqual(self.lb.get_book_status("SF"), 1)
```

実装①

```python
class Libraly:
  def __init__(self, books):
    self.books = books
  def rent_book(self, name):
    self.books[name] = 1
    return True
　def return_book(self, name):
    
  def return_book_in_deadline(self, name):
    return True
  def return_book_after_deadline(self, name):
    return overdue
  def get_book_status(self, name):
    return self.books[name]
  def pass_days(self, day):
    return True
```

#### テストケース②: 貸し出し中状態の本を返却すると本は貸し出し中状態から貸し出し可能状態になる

```python
def test_return_book_in_deadline(self):
  self.lb.rent_book("SF")
  result = self.lb.return_book_in_deadline("SF")
  self.assertTrue(result)
  self.assertEqual(self.lb.get_book_status("SF"), 0)
```
実装②
```python
def return_book_in_deadline(self, name):
  self.books[name] = 0
  return True
```

#### テストケース③: 本を貸し出し中状態にしたまま一定日数が経過すると延滞状態になる

```python
def test_overdue_status(self):
  lb.rent_book("SF")
  lb.pass_days(10)

  self.assertEqual(self.lb.get_book_status("SF"), 2)
```

実装③
```diff
def __init__(self, books):
  self.books = books
+  self.days = {name: 0 for name in books}
def rent_book(self, name):
  self.books[name] = 1
+  self.days[name] = 0
  return True

def pass_days(self, day):
  for name in self.books:
    if self.books[name] == 1:
      self.days[name] += day
      if self.days[name] > 7:
        self.books[name] = 2

```

#### テストケース④: 延滞状態の本を返却すると延滞日数が返され、本は貸し出し可能状態になる
```python
def test_return_book_after_deadline(self):
      self.lb.rent_book("SF")
      self.lb.pass_days(10)
      overdue = self.lb.return_book_after_deadline("SF")

      self.assertEqual(overdue, 3)
      self.assertEqual(self.lb.get_book_status("SF"), 0)
  
```

実装④
```diff
def return_book_after_deadline(self, name):
+  overdue = self.days[name] - 7
+  self.books[name] = 0
+  return overdue
```

#### テストケース⑤: 貸し出し中や延滞中の本を借りようとすると失敗し、`false`が返される
```python
def test_rent_lenting_book(self):
    self.lb.rent_book("SF")
    result = self.lb.rent_book("SF")
    self.assertEqual(result, False)
def test_rent_overdue_book(self):
    self.lb.rent_book("SF")
    self.lb.pass_days(10)
    result = self.lb.rent_book("SF")
    self.assertEqual(result, False)
```

実装⑤
```diff
def rent_book(self, name):
+  if (self.books[name] == 1) or (self.books[name] == 2):
+    return False
  self.books[name] = 1
  self.days[name] = 0
  return True
```

#### テストケース⑥: 貸し出し可能状態の本はどれだけ日数を経過させても貸し出し時間が経過せず、貸し出し可能状態のままである
```python
def test_pass_days_of_available_book(self):
  self.lb.rent_book("SF")
  self.lb.pass_days(10)
  self.assertEqual(self.lb.days["SF"], 10)
  self.assertEqual(self.lb.days["mystery"], 0)
```
実装⑥(変更無し)
```diff
def pass_days(self, day):
  for name in self.books:
    if self.books[name] == 1:
      self.days[name] += day
      if self.days[name] > 7:
        self.books[name] = 2
```

#### テストケース⑦: 図書館に存在しない本を借りようとすると失敗し、`false`が返される
```python
def test_rent_invalid_book(self):
   self.assertEqual(self.lb.rent_book("adventure"), 0)
```

実装⑦
```diff
def rent_book(self, name):
+  if name not in self.books:
+    return False
  if (self.books[name] == 1) or (self.books[name] == 2):
    return False
  self.books[name] = 1
  self.days[name] = 0
  return True
```

#### テストケース⑧: 本の返却時にその本の状態をシステムが判定し、期限内の返却と延滞中の本の返却に分岐する
```python
def test_return_book(self):
  self.lb.rent_book("SF")
  self.lb.pass_days(5)
  self.lb.rent_book("mystery")
  self.lb.pass_days(5)
  self.assertEqual(self.lb.return_book("SF"), 3)
  self.assertEqual(self.lb.return_book("mystery"), True)    
```

実装⑧
```diff
def return_book(self,name):
  if self.books[name] == 2:
    return self.return_book_after_deadline(name)
  elif self.books[name] == 1:
    return self.return_book_in_deadline(name)
  else:
    return False
```

#### テストケース⑨: 返却した本は貸出期間がリセットされる
```python
def test_reset_days(self):
  self.lb.rent_book("SF")
  self.lb.pass_days(5)
  self.lb.rent_book("mystery")
  self.lb.pass_days(5)
  self.lb.return_book("SF")
  self.lb.return_book("mystery")
  self.assertEqual(self.lb.days["SF"], 0)
  self.assertEqual(self.lb.days["mystery"], 0)
```
実装⑨
```diff
def return_book_in_deadline(self, name):
  self.books[name] = 0
+  self.days[name] = 0
  return True
def return_book_after_deadline(self, name):
  overdue = self.days[name] - 7
  self.books[name] = 0
+  self.days[name] = 0
  return overdue
```

## リファクタリング(本の状態をEnumで管理)

```diff
-    from libraly import Libraly
+    from libraly import Libraly, BookStatus

    def test_rent_book(self):
        result = self.lb.rent_book("SF")
        self.assertTrue(result)
-        self.assertEqual(self.lb.get_book_status("SF"), 1)
+        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.LENDING)
    def test_return_book_in_deadline(self):
        self.lb.rent_book("SF")
        result = self.lb.return_book_in_deadline("SF")
        self.assertTrue(result)
-        self.assertEqual(self.lb.get_book_status("SF"), 0)
+        self.assertEqual(self.lb.get_book_status("SF"), BookSatus.AVAILABLE)
    def test_overdue_status(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(10)

-        self.assertEqual(self.lb.get_book_status("SF"), 2)
+        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.OVERDUE)
    def test_return_book_after_deadline(self):
        self.lb.rent_book("SF")
        self.lb.pass_days(10)
        overdue = self.lb.return_book_after_deadline("SF")

        self.assertEqual(overdue, 3)
-        self.assertEqual(self.lb.get_book_status("SF"), 0)
+        self.assertEqual(self.lb.get_book_status("SF"), BookStatus.AVAILABLE)
```

```diff
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
-    if (self.books[name] == 1) or (self.books[name] == 2):
+    if (self.books[name] == BookStatus.LENDING) or (self.books[name] == BookStatus.OVERDUE):
      return False
-    self.books[name] = 1
+    self.books[name] = BookStatus.LENDING
    self.days[name] = 0
    return True
  def return_book_in_deadline(self, name):
-    self.books[name] = 0
+    self.books[name] = BookStatus.AVAILABLE
    self.days[name] = 0
    return True
  def return_book_after_deadline(self, name):
    overdue = self.days[name] - 7
-    self.books[name] = 0
+    self.books[name] = BookStatus.AVAILABLE
    self.days[name] = 0
    return overdue
  def return_book(self,name):
-    if self.books[name] == 2:
+    if self.books[name] == BookStatus.OVERDUE:
      return self.return_book_after_deadline(name)
-    elif self.books[name] == 1:
+    elif self.books[name] == BookStatus.LENDING:
      return self.return_book_in_deadline(name)
    else:
      return False

  def get_book_status(self, name):
    return self.books[name]
  def pass_days(self, day):
    for name in self.books:
-     if self.books[name] == 1:
+     if self.books[name] == BookStatus.LENDING:
        self.days[name] += day
        if self.days[name] > 7:
-         self.books[name] = 2
+         self.books[name] = BookStatus.OVERDUE
    return True
```
