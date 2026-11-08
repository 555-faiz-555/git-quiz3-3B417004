import json

from pkg.book_tools import (
    add_book,
    search_books,
    borrow_book,
    get_last_three_books,
    get_total_price,
    get_book_statistics,
    save_books
)


# 讀取 JSON
with open('books.json', 'r', encoding='UTF-8') as f:
    books = json.load(f)


while True:

    print("\n--- 簡易書籍管理系統 ---")
    print("1. 顯示全部書籍")
    print("2. 新增書籍")
    print("3. 查詢書籍")
    print("4. 變更借閱狀態")
    print("5. 顯示最後 3 筆書籍與統計")
    print("6. 匯出書籍資料")
    print("7. 離開系統")
    print("------------------------")

    choice = input("請選擇功能：")

    if choice == "1":

        
        print("\n--- 全部書籍 ---")

        print(
            f"{'編號':<4}"
            f"{'書籍編號':<6}"
            f"{'書名':<14}"
            f"{'作者':<7}"
            f"{'價格':<4}"
            f"狀態"
        )
        
        for i, book in enumerate(books, start=1):

            status = "已借出" if book["borrowed"] else "可借閱"

            print(
                f"{i:>4}"
                f"{book['id']:>6}"
                f"{book['title']:>15}"
                f"{book['author']:>8}"
                f"{book['price']:>6}"
                f"{status:>6}"
            )
        

    elif choice == "2":
        add_book(books)

    elif choice == "3":

        keyword = input("請輸入書名關鍵字：")

        result = search_books(books, keyword)

        if len(result) > 0:

            print("\n--- 查詢結果 ---")

            print(
                f"{'編號':<4}"
                f"{'書籍編號':<6}"
                f"{'書名':<14}"
                f"{'作者':<7}"
                f"{'價格':<4}"
                f"狀態"
            )

            for i, book in enumerate(result, start=1):

                status = "已借出" if book["borrowed"] else "可借閱"

                print(
                    f"{i:>4}"
                    f"{book['id']:>6}"
                    f"{book['title']:>15}"
                    f"{book['author']:>8}"
                    f"{book['price']:>6}"
                    f"{status:>6}"
                )

        else:
            print("找不到符合的書籍！")

    elif choice == "4":

        book_id = input("請輸入書籍編號：")

        borrow_book(books, book_id)

    elif choice == "5":

        print("\n--- 最後 3 筆書籍 ---")
        print(
            f"{'編號':<4}"
            f"{'書籍編號':<6}"
            f"{'書名':<14}"
            f"{'作者':<7}"
            f"{'價格':<4}"
            f"狀態"
                    )
        

        last_three = get_last_three_books(books)
        

        for i, book in enumerate(last_three, start=1):

            status = "已借出" if book["borrowed"] else "可借閱"

            print(
                f"{i:>4}"
                f"{book['id']:>6}"
                f"{book['title']:>15}"
                f"{book['author']:>8}"
                f"{book['price']:>6}"
                f"{status:>6}"
            )
        
        
        get_book_statistics(books)

        print(f"價格合計： {get_total_price(books):,} 元")
        print("平均價格：", get_total_price(books) / len(books), "元")

    elif choice == "6":

        save_books(books)

    elif choice == "7":

        print("感謝使用書籍管理系統！")

        break

    else:
        print("無效的選項，請重新輸入！")