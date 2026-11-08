import json
#新增書籍
def add_book(books: list) -> None:
    
    while True:

        book_id = input("請輸入書籍編號：")

        duplicate = False

        # 檢查書籍編號是否重複
        for book in books:
            if book["id"] == book_id:
                duplicate = True
                break

        if duplicate:
            print("書籍編號已存在，請重新輸入。")

        else:
            break

    title = input("請輸入書名：")
    author = input("請輸入作者：")

    while True:

        try:
            price = int(input("請輸入價格："))

            if price <= 0:
                print("價格須為大於 0 的整數，請重新輸入。")

            else:
                break

        except ValueError:
            print("價格須為大於 0 的整數，請重新輸入。")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "price": price,
        "borrowed": False
    }

    books.append(new_book)

    print("新增成功。")
#查詢書籍
def search_books(books: list, keyword: str) -> list:
    """
    根據書名關鍵字搜尋書籍。

    Args:
        books: 所有書籍資料。
        keyword: 使用者輸入的搜尋關鍵字。

    Returns:
        符合搜尋條件的書籍列表。
    """
    result = [
        book for book in books
        if keyword.lower() in book["title"].lower()
    ]

    return result
#變更借閱狀態
def borrow_book(books: list, book_id: str) -> None:
    """
    切換指定書籍的借閱狀態。

    Args:
        books: 所有書籍資料。
        book_id: 要切換狀態的書籍編號。
    """

    book_id = book_id.strip()

    for book in books:

        if book["id"] == book_id:

            book["borrowed"] = not book["borrowed"]

            status = "已借出" if book["borrowed"] else "可借閱"

            print(f"「{book['title']}」的狀態已變更為：{status}")

            return

    print("查無此書籍編號")
#顯示最後 3 筆書籍
def get_last_three_books(books: list) -> list:
    """
    取得最後三本書籍。

    Args:
        books: 所有書籍資料。

    Returns:
        最後三本書籍的列表。
    """
    return books[-3:]
#最後 3 筆書籍統計
def get_total_price(books: list) -> int:
    """
    計算所有書籍的總價值。

    Args:
        books: 所有書籍資料。

    Returns:
        所有書籍的價格總和。
    """
    prices = [book["price"] for book in books]

    return sum(prices)

def get_book_statistics(books: list) -> None:
    """
    統計書籍數量。

    Args:
        books: 所有書籍資料。
    """
    total_books = len(books)

    borrowed_books = [
        book for book in books
        if book["borrowed"]
    ]

    available_books = [
        book for book in books
        if not book["borrowed"]
    ]

    borrowed_count = len(borrowed_books)
    available_count = len(available_books)

    print("\n--- 書籍統計 ---")
    print("書籍總數：", total_books)
    print("已借出數量：", borrowed_count)
    print("可借閱數量：", available_count)

def save_books(books: list) -> None:
    """
    將書籍資料儲存至 JSON 檔案。

    Args:
        books: 所有書籍資料。
    """
    with open('books.json', 'w', encoding='UTF-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

    print(f"已匯出 {len(books)} 筆書籍資料至 output.json。")