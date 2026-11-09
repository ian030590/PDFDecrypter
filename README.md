# PDFDecrypter

以命令列輸入已知密碼，移除 PDF 密碼與列印、複製限制

Remove PDF passwords and print or copy restrictions with a known password in a CLI.

![PDFDecrypter 命令列執行畫面 / PDFDecrypter CLI](assets/screenshot.png)

[中文](#中文) · [English](#english)

## 中文

一次處理一份加密 PDF，以 pypdf 讀取檔案，將解密後的頁面寫成不加密的新檔。僅用於你有權解除保護的檔案。

### 功能

- PDF 若設有開啟密碼，必須輸入正確密碼。程式只嘗試你輸入的密碼，密碼錯誤就停止。
- 若檔案可用空白密碼開啟，可直接按 Enter 嘗試解密。
- 未加密的 PDF 不會產生輸出。

### 安裝與執行

需先安裝 Python。下載原始碼後，在專案資料夾開啟終端機並執行：

```bash
python -m pip install pypdf
python PDFDecrypter.py
```

1. 輸入 PDF 路徑。若終端機支援拖曳，也可將檔案拖入後按 Enter。
2. 輸入開啟密碼，輸入內容會顯示於畫面。若可用空白密碼開啟，直接按 Enter。
3. 輸入輸出路徑，或直接按 Enter 使用預設路徑。

處理完成後按 Enter 結束程式。

若要在 Windows 自行建立 `PDFDecrypter.exe`，於同一個資料夾執行：

```bash
python -m pip install pyinstaller
python -m PyInstaller PDFDecrypter.spec
```

建置完成後，可執行 `dist` 中的 `PDFDecrypter.exe`，再依提示輸入路徑與密碼。

### 輸出

預設儲存在來源檔案旁，命名為 `原檔名_unlocked.pdf`，例如 `report.pdf` 會輸出 `report_unlocked.pdf`。也可在提示時指定路徑；同名檔案會被覆寫。

輸出由頁面重建，程式沒有另行複製原檔的中繼資料或書籤。

### 授權

本專案採用 MIT License 授權開源。

## English

Processes one encrypted PDF at a time. It reads the file with pypdf and writes the decrypted pages to a new, unencrypted PDF. Use only with files you are allowed to decrypt.

### Features

- If the PDF has an open password, you must enter the correct password. The tool tries only the password you enter and stops if it is incorrect.
- If the file opens with an empty password, press Enter to try decrypting it.
- Unencrypted PDFs produce no output.

### Install and run

Install Python first. After downloading the source, open a terminal in the project folder and run:

```bash
python -m pip install pypdf
python PDFDecrypter.py
```

1. Enter the PDF path. If your terminal supports it, you can also drag the file into the terminal and press Enter.
2. Enter the open password. Your input is visible on screen. If the file opens with an empty password, press Enter.
3. Enter an output path, or press Enter to use the default.

Press Enter after processing to exit.

To build `PDFDecrypter.exe` on Windows, run these commands in the same folder:

```bash
python -m pip install pyinstaller
python -m PyInstaller PDFDecrypter.spec
```

After building, run `PDFDecrypter.exe` from `dist` and follow the path and password prompts.

### Output

By default, the output is saved beside the source file as `original-name_unlocked.pdf`. For example, `report.pdf` produces `report_unlocked.pdf`. You can enter a different path at the prompt. An existing file at the output path will be overwritten.

The output is rebuilt from pages. The script does not separately copy the original file's metadata or bookmarks.

### License

This project is released under the MIT License.
