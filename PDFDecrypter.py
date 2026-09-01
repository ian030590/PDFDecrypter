import os
from pypdf import PdfReader, PdfWriter

def main():
    print("=== PDF 密碼移除工具 ===")
    
    # 1. 取得檔案路徑 (使用 strip('\"') 避免拖曳檔案時產生的引號)
    input_file = input("請輸入或拖曳加密的 PDF 檔案到這裡: ").strip('\"')
    
    if not os.path.exists(input_file):
        print("找不到該檔案，請檢查路徑。")
        input("按 Enter 鍵結束程式...")
        return

    # 2. 取得密碼
    password = input("請輸入 PDF 的開啟密碼: ")
    
    # 3. 設定輸出路徑
    output_file = input("請輸入輸出檔案路徑 (直接按 Enter 則預設為「原檔名_unlocked.pdf」): ").strip('\"')
    if not output_file:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_unlocked{ext}"

    # 4. 開始處理 PDF
    try:
        reader = PdfReader(input_file)
        
        # 檢查是否加密
        if not reader.is_encrypted:
            print("此 PDF 並未加密，不需要移除密碼。")
            input("按 Enter 鍵結束程式...")
            return
            
        # 嘗試解密
        if not reader.decrypt(password):
            print("❌ 密碼錯誤，無法解密 PDF！")
            input("按 Enter 鍵結束程式...")
            return
            
        # 將解密後的頁面寫入新的 PDF
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
            
        # 儲存檔案
        with open(output_file, "wb") as f:
            writer.write(f)
            
        print(f"\n✅ 成功！已將解除密碼的檔案儲存至:\n{output_file}")
        
    except Exception as e:
        print(f"\n❌ 處理時發生未知的錯誤: {e}")
        
    # 防止執行檔視窗閃退
    input("\n按 Enter 鍵結束程式...")

if __name__ == "__main__":
    main()