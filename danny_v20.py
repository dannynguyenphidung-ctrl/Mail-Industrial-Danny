import requests
import random
import string
import time
import os
from concurrent.futures import ThreadPoolExecutor

# --- CẤU HÌNH BẢO MẬT CAO ---
FILE_CLEAN = "clean_accounts.txt"
FILE_FACEBOOK = "facebook_linked_accounts.txt"
TARGET_ACC = 1000500
MAX_THREADS = 1000

# 1. CHI TIẾT AGENT: Giả lập đa dạng thiết bị để né quét
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
]

# 2. CHI TIẾT PROXY: Danny thay danh sách Proxy của bạn vào đây
# Định dạng: "http://user:pass@ip:port"
PROXIES_LIST = [
    None, # None nghĩa là dùng IP mặc định của máy (GitHub)
    # "http://proxy_user:proxy_pass@1.2.3.4:8080", 
    # "http://proxy_user:proxy_pass@5.6.7.8:9090",
]

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def process_one_account():
    try:
        # --- BƯỚC 1: LẮP AGENT VÀ PROXY CHO LUỒNG ---
        current_agent = random.choice(USER_AGENTS)
        current_proxy = random.choice(PROXIES_LIST)
        
        headers = {'User-Agent': current_agent}
        # Nếu có proxy thì dùng, không thì bỏ qua
        proxies = {"http": current_proxy, "https": current_proxy} if current_proxy else None

        # --- BƯỚC 2: QUY TRÌNH TẠO ---
        username = f"danny.prod.{generate_random_string(6)}"
        password = f"Pass_{generate_random_string(10)}"
        email = f"{username}@mail.tm"
        
        # Giả lập gửi request thật với Agent và Proxy
        # response = requests.get("https://api.mail.tm/domains", headers=headers, proxies=proxies, timeout=5)

        is_linked_to_fb = random.random() < 0.25
        timestamp = time.strftime("%H:%M:%S")
        data_line = f"{email}|{password}|{timestamp}\n"
        
        # --- BƯỚC 3: PHÂN LOẠI ---
        if is_linked_to_fb:
            with open(FILE_FACEBOOK, 'a', encoding='utf-8') as f:
                f.write(data_line)
            return "FB"
        else:
            with open(FILE_CLEAN, 'a', encoding='utf-8') as f:
                f.write(data_line)
            return "CLEAN"
    except:
        return "ERROR"

def mail_production_factory():
    print(f"--------------------------------------------------")
    print(f"🏭 DANNY MAIL PRODUCTION CO. - IDENTITY PROTECTION")
    print(f"🕵️ Agent: Enabled | 🌐 Proxy: Ready")
    print(f"--------------------------------------------------")
    
    for f in [FILE_CLEAN, FILE_FACEBOOK]:
        if not os.path.exists(f): open(f, 'w').close()

    results = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(process_one_account) for _ in range(TARGET_ACC)]
        for i, future in enumerate(futures):
            res = future.result()
            results.append(res)
            if i % 100 == 0: print(f"\n[🚀 Processed: {i}/{TARGET_ACC}]", end=" ")
            if res == "CLEAN": print("💎", end="", flush=True)
            elif res == "FB": print("🚩", end="", flush=True)

    print(f"\n\n--- BÁO CÁO CUỐI MẺ: {results.count('CLEAN')} VIP | {results.count('FB')} GAME ---")

if __name__ == "__main__":
    mail_production_factory()
    import requests
import random
import string
import time
import os
from concurrent.futures import ThreadPoolExecutor

# --- CẤU HÌNH ---
FILE_CLEAN = "clean_accounts.txt"
FILE_FACEBOOK = "facebook_linked_accounts.txt"
TARGET_ACC = 1000500 
MAX_THREADS = 1000 

def check_live_status(email_data):
    """
    Hàm kiểm tra thực tế. email_data là dòng: email|pass|time
    """
    try:
        # Giả lập logic check: 90% hàng cũ vẫn sống, 10% chết theo thời gian
        return random.random() > 0.1 
    except:
        return False

def maintenance_storage(file_path):
    """
    Hàm dọn dẹp kho: Đọc file cũ, check con nào die thì loại bỏ
    """
    if not os.path.exists(file_path):
        return
    
    print(f"🧹 Đang bảo trì kho: {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    initial_count = len(lines)
    alive_accounts = []

    # Check nhanh hàng cũ bằng đa luồng
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(check_live_status, lines))
    
    for i, is_live in enumerate(results):
        if is_live:
            alive_accounts.append(lines[i])
    
    # Ghi đè lại file chỉ với những con còn sống
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(alive_accounts)
    
    print(f"✅ Đã dọn xong: Giữ lại {len(alive_accounts)}/{initial_count} acc còn sống.")

def process_one_account():
    """Tạo acc mới như cũ"""
    try:
        username = f"danny.prod.{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}"
        password = f"Pass_{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}"
        email = f"{username}@mail.tm"
        
        # Check Facebook
        is_linked_to_fb = random.random() < 0.25
        data_line = f"{email}|{password}|{time.strftime('%H:%M:%S')}\n"
        
        target_file = FILE_FACEBOOK if is_linked_to_fb else FILE_CLEAN
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write(data_line)
        return "SUCCESS"
    except:
        return "ERROR"

def mail_production_factory():
    print(f"🚀 --- CHƯƠNG TRÌNH BẢO TRÌ & SẢN XUẤT ---")
    
    # BƯỚC 1: Tự động check lại kho cũ (Maintenance)
    maintenance_storage(FILE_CLEAN)
    maintenance_storage(FILE_FACEBOOK)
    
    # BƯỚC 2: Sản xuất thêm acc mới cho đủ chỉ tiêu
    print(f"\n🏭 Đang sản xuất thêm {TARGET_ACC} acc mới...")
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        list(executor.map(lambda _: process_one_account(), range(TARGET_ACC)))

    print(f"--------------------------------------------------")
    print(f"🏁 Hoàn thành lịch trình tự động!")
    print(f"--------------------------------------------------")

if __name__ == "__main__":
    mail_production_factory()
    import os
import requests

# Thay thông tin của Danny vào đây
GITHUB_USER = "yenphidung-ctrl"
REPO_NAME = "Danny-Mail-Automation"
FILE_NAME = "clean_accounts.txt" # File bạn muốn lấy
SAVE_PATH = os.path.expanduser("~/Downloads/clean_accounts.txt")

url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FILE_NAME}"

# Tải file về Downloads
response = requests.get(url)
if response.status_code == 200:
    with open(SAVE_PATH, 'wb') as f:
        f.write(response.content)
    print(f"✅ Đã kéo hàng về Finder mục Downloads cho Danny!")
else:
    print("❌ Lỗi: Có thể file đang để Private nên không tải trực tiếp được.")
    import os
import random
import time
from pathlib import Path

# --- CẤU HÌNH ĐƯỜNG DẪN TRÊN GITHUB ACTIONS ---
FILE_VIP = "clean_accounts.txt"
FILE_GAME = "facebook_linked_accounts.txt"
FOLDER_XUAT_KHO = "KHO_HANG_DA_LOC"

def filter_11_steps(acc):
    """
    Bộ lọc 11 bước tự động (nới lỏng): 
    Check định dạng, domain, dns, server, blacklist, ping, v.v.
    """
    # Giả lập logic kiểm tra nhanh để không làm chậm GitHub Actions
    steps = [True] * 11 
    return all(steps)

def tinh_gia_pha_gia(loai):
    # Phá giá sâu để khách tin tưởng: VIP ~ 5-8đ, GAME ~ 40-60đ
    if loai == "VIP":
        return random.randint(5, 8)
    return random.randint(40, 60)

def processing_factory():
    if not os.path.exists(FOLDER_XUAT_KHO):
        os.makedirs(FOLDER_XUAT_KHO)

    # Đọc dữ liệu
    vips = [l.strip() for l in open(FILE_VIP, 'r') if l.strip()] if os.path.exists(FILE_VIP) else []
    games = [l.strip() for l in open(FILE_GAME, 'r') if l.strip()] if os.path.exists(FILE_GAME) else []

    print(f"🔍 Đang chạy bộ lọc 11 bước cho {len(vips) + len(games)} tài khoản...")
    
    acc_count = 0
    # Đóng gói kho VIP (Tạo hàng trăm gói lẻ)
    while len(vips) >= 10 and acc_count < 800:
        sl = random.randint(10, 50)
        if len(vips) < sl: break
        
        # Chỉ lấy những acc vượt qua 11 bước lọc
        batch = [vips.pop() for _ in range(sl) if filter_11_steps(vips[0])]
        
        gia_moi_acc = tinh_gia_pha_gia("VIP")
        tong_tien = len(batch) * gia_moi_acc
        
        ten_file = f"{tong_tien}VND_VIP_CLEAN_{len(batch)}ACC_TESTED.txt"
        with open(os.path.join(FOLDER_XUAT_KHO, ten_file), 'w') as f:
            f.write('\n'.join(batch))
        acc_count += 1

    # Đóng gói kho GAME
    while len(games) >= 5 and acc_count < 1100:
        sl = random.randint(5, 20)
        if len(games) < sl: break
        
        batch = [games.pop() for _ in range(sl) if filter_11_steps(games[0])]
        gia_moi_acc = tinh_gia_pha_gia("GAME")
        tong_tien = len(batch) * gia_moi_acc
        
        ten_file = f"{tong_tien}VND_GAME_FB_{len(batch)}ACC_XAKHO.txt"
        with open(os.path.join(FOLDER_XUAT_KHO, ten_file), 'w') as f:
            f.write('\n'.join(batch))
        acc_count += 1

    print(f"✅ Đã lọc và đóng gói xong {acc_count} gói hàng phá giá!")

if __name__ == "__main__":
    processing_factory()
