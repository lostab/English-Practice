# -*- coding: utf-8 -*-
"""一次性修复 apple-welcome-home 17 页项目的 spec 文件并做最终检查"""
import os, re, collections, subprocess, json

PROJ = "D:/work/Hermes/testprep-app/pptmaster_project/projects/apple-welcome-home_ppt169_20261015"
OUT = os.path.join(PROJ, "svg_output")
DECLARED = {"44", "28", "24", "20", "18", "15", "14", "13"}

print("=" * 60)
print("STEP 1: design_spec.md Page Count 12 -> 17")
ds_path = os.path.join(PROJ, "design_spec.md")
ds = open(ds_path, encoding="utf-8").read()
ds = re.sub(r"(\|\s*Page Count\s*\|\s*)12(\s*\|)", r"\g<1>17\g<2>", ds)
open(ds_path, "w", encoding="utf-8").write(ds)
m = re.search(r"Page Count.*\| (\d+) \|", ds)
print("  新 Page Count:", m.group(1) if m else "?")

print("=" * 60)
print("STEP 2: 逐文件检查")
report = {"slides": [], "errors": 0}
for f in sorted(os.listdir(OUT)):
    if not f.endswith(".svg"):
        continue
    path = os.path.join(OUT, f)
    c = open(path, encoding="utf-8").read()
    errs = []

    # a) XML 基本合法性 (标签配对粗略检查)
    if c.count("<svg") != 1 or not c.rstrip().endswith("</svg>"):
        errs.append("SVG 标签不完整")

    # b) 未转义 &
    for mm in re.finditer(r"&(?!(amp|lt|gt|quot|apos);)", c):
        if "<![CDATA[" not in c[:mm.start()]:
            errs.append(f"未转义 & 在偏移 {mm.start()}")
            break

    # c) 字号门禁
    sizes = collections.Counter(re.findall(r'font-size="(\d+)"', c))
    bad_sizes = {s: n for s, n in sizes.items() if s not in DECLARED and n >= 3}
    if bad_sizes:
        errs.append(f"字号超限 {bad_sizes}")

    # d) 页码检查
    pageno = re.findall(r">(\d+)\s*/\s*\d+<", c)
    fileslug = re.search(r"slide_(\d+)_", f)
    if not pageno:
        errs.append("无页码")
    elif fileslug and pageno and pageno[-1] != fileslug.group(1):
        errs.append(f"页码 {pageno[-1]} != 文件序号 {fileslug.group(1)}")

    # e) 图片引用存在性
    imgs = set(os.listdir(os.path.join(PROJ, "images")))
    for mm in re.finditer(r'href="\.\./images/([^"]+)"', c):
        if mm.group(1) not in imgs:
            errs.append(f"图片缺失 {mm.group(1)}")

    # f) 泄漏数据扫描
    leaks = [r"85%", r"NeuralEngine\s*6T", r"16核", r"¥\d{3}", r"\$\d+\.\d+",
             r"Local\s*85%", r"HomeOS\s*2\.\d+", r"Thread\s*1\.\d+", r"Matter\s*1\.\d+",
             r"EAL5", r"6GB", r"Kirin\s*9"]
    for pat in leaks:
        if re.search(pat, c):
            errs.append(f"泄漏数据 [{pat}]")

    status = "PASS" if not errs else "FAIL"
    report["slides"].append({"file": f, "status": status, "errors": errs})
    if errs:
        report["errors"] += 1
    print(f"  [{status}] {f}")
    for e in errs:
        print(f"         - {e}")

print("=" * 60)
print("STEP 3: spec_lock.md 与 design_spec.md 一致性")
sl = open(os.path.join(PROJ, "spec_lock.md"), encoding="utf-8").read()
n_rhythm = len(re.findall(r"^P\d+: ", sl, re.M))
print(f"  spec_lock page_rhythm: {n_rhythm} 页 (应为 17)")
if n_rhythm != 17:
    print("  -> 需要修复 page_rhythm")
n_imgs = len(re.findall(r"images/\S+", sl))
print(f"  spec_lock images: {n_imgs} 项")

print("=" * 60)
result = {"ok": report["errors"] == 0 and n_rhythm == 17}
print("FINAL:", "PASS" if result["ok"] else "FAIL", f"({report['errors']} 个错误)")
with open(os.path.join(PROJ, "validation", "preflight.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)