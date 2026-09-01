# PDFDecrypter (PDF 密碼移除與解鎖工具) 🔓📑

輕量便捷的 PDF 權限密碼移除與解鎖工具，使用 `pypdf` 解析受保護的 PDF 文件，輸入密碼後自動輸出無密碼保護之全新 PDF 檔案。

## 🌟 核心功能 / Features

- 🖱️ **支援檔案拖曳（Drag & Drop）**：命令列提示時可直接將 PDF 拖曳至視窗中自動解析路徑。
- 🔓 **快速移除加密權限**：驗證密碼後完整解密，解除列印、複製與標註限制。
- 🛡️ **安全無毒**：純本機離線處理，不需上傳至第三方轉換網站，保護敏感臨床資料與個資安全。

## 📂 檔案結構 / File Structure

```text
PDFDecrypter/
├── PDFDecrypter.py    # PDF 解密核心原始碼
├── PDFDecrypter.spec  # PyInstaller 打包設定檔
└── README.md          # 專案說明文件
```

## 🚀 使用方式 / Usage

```bash
pip install pypdf
python PDFDecrypter.py
```
依終端機提示輸入或拖曳檔案路徑、輸入檔案密碼，預設會輸出 `[原檔名]_unlocked.pdf`。

## 📄 授權 / License

MIT License
