📚 簡易書籍管理系統

1151 Scripting 程式語言｜期中考

使用 Python 製作的命令列書籍管理系統，透過 JSON 儲存書籍資料，提供書籍瀏覽、新增、查詢、借閱狀態管理及資料匯出等功能。

📌 專案簡介

本專案使用 Python 設計簡易書籍管理系統，透過 list 與 dict 管理書籍資料，並使用 JSON 檔案讀取及匯出資料。

✨ 系統功能
📖 顯示全部書籍
➕ 新增書籍
🔍 查詢書籍
🔄 變更借閱狀態
📊 顯示最後 3 筆書籍與統計
💾 匯出書籍資料
🚪 離開系統
📂 專案架構
text
專案目錄/
│
├── app.py
├── books.json
├── README.md
├── .gitignore
├── LICENSE
│
└── pkg/
    ├── __init__.py
    └── book_tools.py

檔案	說明
app.py	系統主程式
books.json	初始書籍資料
README.md	專案說明文件
.gitignore	Git 忽略設定
LICENSE	專案授權
pkg/__init__.py	套件初始化檔案
pkg/book_tools.py	書籍管理函式
🛠️ 使用技術
Python
List 與 Dictionary
Function（函式）
Type Hints（型別提示）
JSON 資料讀取與寫入
Exception Handling（例外處理）
List Comprehension（列表推導式）
String Formatting（字串格式化）
🚀 執行方式
1. 下載專案
bash
git clone 你的 GitHub Repository 網址

2. 進入專案資料夾
bash
cd 專案資料夾名稱

3. 執行程式
bash
python app.py

📋 操作選單
text
--- 簡易書籍管理系統 ---
1. 顯示全部書籍
2. 新增書籍
3. 查詢書籍
4. 變更借閱狀態
5. 顯示最後 3 筆書籍與統計
6. 匯出書籍資料
7. 離開系統
------------------------
請選擇功能：

💾 資料匯出方式

選擇主選單中的 6. 匯出書籍資料，系統會將目前的書籍資料匯出至 output.json。

使用 UTF-8 編碼儲存，並保留中文顯示。

📄 License

本專案使用 MIT License。