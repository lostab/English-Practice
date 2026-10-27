# -*- coding: utf-8 -*-
"""更新 spec 到 23 页并同步 §IX 大纲"""
import os, re

PROJ = "D:/work/Hermes/testprep-app/pptmaster_project/projects/apple-welcome-home_ppt169_20261015"
TOTAL = 23

# ---------- 1) spec_lock.md ----------
sl_path = os.path.join(PROJ, "spec_lock.md")
sl = open(sl_path, encoding="utf-8").read()

# page_rhythm 重建 23 行
rhythm_lines = []
for i in range(1, TOTAL + 1):
    r = "dense"
    if i in (1, 2, TOTAL):
        r = "anchor"
    rhythm_lines.append(f"- P{i:02d}: {r}")
rhythm_block = "## page_rhythm\n" + "\n".join(rhythm_lines) + "\n"
sl = re.sub(r"## page_rhythm\n.*?(?=\n## |\Z)", rhythm_block, sl, flags=re.S)
open(sl_path, "w", encoding="utf-8").write(sl)
print(f"spec_lock page_rhythm -> {TOTAL} 行")

# ---------- 2) design_spec.md ----------
ds_path = os.path.join(PROJ, "design_spec.md")
ds = open(ds_path, encoding="utf-8").read()

# Page Count
ds = re.sub(r"(\|\s*Page Count\s*\|\s*)\d+(\s*\|)", rf"\g<1>{TOTAL}\g<2>", ds)

# §IX 大纲：重建 23 条（简单版本）
outline = ["## IX. Content Outline", "### Part 1: Executive Insight Deck"]
titles = {
    1: "Cover",
    2: "Agenda · 目录导览",
    3: "执行摘要：五大核心洞察",
    4: "战略演进回顾：从 Siri 到 Welcome Home",
    5: "发布会全景：四线产品",
    6: "HomeView 硬件参数表",
    7: "HomeView 软件与隐私三层架构",
    8: "Apple TV 4K（第4代）深度拆解",
    9: "HomePod mini 2 深度拆解",
    10: "华为智能中控屏 S2 深拆",
    11: "小米智能家庭屏 11 深拆",
    12: "三大核心硬件对比矩阵",
    13: "语音助手生态对比",
    14: "无线协议与 Matter 生态",
    15: "市场格局与生态规模",
    16: "战略定位对比",
    17: "三室两厅解决方案与价格",
    18: "三大生态入口形态",
    19: "Siri / 小艺 / 小爱 本地化",
    20: "未来趋势预判：四大趋势",
    21: "优势劣势矩阵（SWOT）",
    22: "结论与行动建议",
    23: "致谢 · 数据来源与方法论",
}
for num in range(1, TOTAL + 1):
    outline.append(f"\n#### Slide {num:02d} - {titles[num]}\n- **Title**: {titles[num]}\n- **Core message**: 详见对应 SVG 页\n- **Content**:\n  - • 官方口径，详见 SVG 页")
outline_text = "\n".join(outline)

# 替换 §IX 之后内容（保留前面段落结构）
idx = ds.find("## IX. Content Outline")
if idx != -1:
    # 找到下一个一级段落（## X 等）
    tail = ds[idx:]
    nxt = re.search(r"\n## [A-Z]+", tail[20:])
    if nxt:
        ds = ds[:idx] + outline_text + "\n"
    else:
        ds = ds[:idx] + outline_text + "\n"
    open(ds_path, "w", encoding="utf-8").write(ds)
    print(f"design_spec §IX 重建 {TOTAL} 条")
else:
    print("design_spec: §IX 未找到")

# 校验
sl = open(sl_path, encoding="utf-8").read()
ds = open(ds_path, encoding="utf-8").read()
print("spec_lock P 行数:", len(re.findall(r"P\d+: ", sl, re.M)))
m = re.search(r"Page Count.*\| (\d+) \|", ds)
print("design_spec Page Count:", m.group(1) if m else "?")
print("§IX 标题数:", len(re.findall(r"#### Slide", ds)))