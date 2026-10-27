
import subprocess, os, sys

wav_dir = os.environ.get("TEMP", "C:/Users/王威/AppData/Local/Temp")
m4a_dir = os.path.join(wav_dir, "m4a_out")
os.makedirs(m4a_dir, exist_ok=True)

ids = sys.argv[1:] if len(sys.argv) > 1 else []
if not ids:
    # 从题库读
    import re
    with open(r"D:\work\Hermes\testprep-app\src\data\questions.ts", encoding="utf-8") as f:
        content = f.read()
    ids = sorted(set(i for i in re.findall(r'"id"\s*:\s*"([^"]+)"', content) if i.startswith("toeic-l-") or i.startswith("toefl-l-")))

for aid in ids:
    wav_path = os.path.join(wav_dir, "testprep-audio-fix", f"{aid}.wav")
    if not os.path.exists(wav_path):
        # 尝试线上下载
        wav_path = os.path.join(wav_dir, f"{aid}.wav")
    m4a_path = os.path.join(m4a_dir, f"{aid}.m4a")
    
    if not os.path.exists(wav_path):
        print(f"WAV not found: {aid}")
        continue
    
    # ffmpeg 转码: AAC 128k 44.1kHz mono
    cmd = ["ffmpeg", "-y", "-i", wav_path, "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-ac", "1", m4a_path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        print(f"✓ {aid}.m4a")
    else:
        print(f"✗ {aid}: {r.stderr[:200]}")

print("Done.")
