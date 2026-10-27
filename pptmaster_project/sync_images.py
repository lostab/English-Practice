# -*- coding: utf-8 -*-
"""同步 design_spec.md §VIII 与 spec_lock.md images，让 7 张图两边注册一致"""
import os, re

PROJ = "D:/work/Hermes/testprep-app/pptmaster_project/projects/apple-welcome-home_ppt169_20261015"
DS = os.path.join(PROJ, "design_spec.md")
SL = os.path.join(PROJ, "spec_lock.md")

# ---------- 1) spec_lock.md: 补 hv_lineup.jpg ----------
sl = open(SL, encoding="utf-8").read()
if "hv_lineup.jpg" not in sl:
    sl = sl.replace(
        "- hv_color.jpg: images/hv_color.jpg | source=web | crop=adaptive\n",
        "- hv_color.jpg: images/hv_color.jpg | source=web | crop=adaptive\n"
        "- hv_lineup.jpg: images/hv_lineup.jpg | source=web | crop=adaptive\n",
    )
    open(SL, "w", encoding="utf-8").write(sl)
    print("spec_lock: + hv_lineup.jpg")
else:
    print("spec_lock: hv_lineup.jpg 已有")

# ---------- 2) design_spec.md §VIII: 补 hv_atv4k / hv_atv_home / hv_hpm2 ----------
ds = open(DS, encoding="utf-8").read()

# 目标行（放在 hw_s2_product 之后）
new_rows = (
    "| hv_atv4k.jpg | 1280×720 | 16:9 | Apple TV 4K 官图 | photo | none | adaptive | web | sourced | Apple Newsroom (2026-10-13) | no-text | P08 |\n"
    "| hv_atv_home.jpg | 1280×720 | 16:9 | 客厅场景官图 | photo | none | adaptive | web | sourced | Apple Newsroom (2026-10-13) | no-text | P07 |\n"
    "| hv_hpm2.jpg | 1280×720 | 16:9 | HomePod mini 2 官图 | photo | none | adaptive | web | sourced | Apple Newsroom (2026-10-13) | no-text | P08 |\n"
)

# 在 §VIII 表格里 hw_s2_product 行后面插入；若该行不存在则追加到表尾
anchor = "| hw_s2_product.jpg | 1280×720 | 16:9 | 华为中控屏 S2 产品官图 | photo | none | adaptive | web | sourced | Huawei 官网 (consumer.huawei.com) | no-text | P04/P05 |\n"
if anchor in ds:
    if "hv_atv4k.jpg" not in ds:
        ds = ds.replace(anchor, anchor + new_rows)
        open(DS, "w", encoding="utf-8").write(ds)
        print("design_spec §VIII: + 3 行 (atv4k / atv_home / hpm2)")
    else:
        print("design_spec §VIII: 已含 atv4k 等行")
else:
    print("design_spec §VIII: 未找到 hw_s2 锚点行，检查实际内容")
    # 打印表格行，帮助定位
    m = ds.find("## VIII")
    seg = ds[m:m+1500]
    for line in seg.split("\n"):
        if line.startswith("|") and "jpg" in line:
            print("  EXISTING:", line[:100])

# ---------- 3) 校验 ----------
sl = open(SL, encoding="utf-8").read()
ds = open(DS, encoding="utf-8").read()
imgs_dir = set(os.listdir(os.path.join(PROJ, "images")))
print("\n--- 最终一致性 ---")
for img in sorted(imgs_dir):
    in_ds = img in ds
    in_sl = img in sl
    print(f"  {img}: design_spec={'Y' if in_ds else 'N'}  spec_lock={'Y' if in_sl else 'N'}")