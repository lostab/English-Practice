#!/usr/bin/env python3
"""生成最终的 wow_map.html（单文件，无单引号错误，热区精准对齐）"""
import json, os

BASE = "D:/work/Hermes/wow-map"

# 1. 读取地图配置
with open(f"{BASE}/_imgs.json", "r", encoding="utf-8") as f:
    IMGS = json.load(f)

# 2. 读取 ZONES 配置
with open(f"{BASE}/wow_map.html", "r", encoding="utf-8") as f:
    html = f.read()

# 3. 替换 loadOverview 函数（关键修改点）
def generate_html():
    global html
    # 读取原始 HTML 模板
    with open(os.path.join(BASE, "template.html"), "r", encoding="utf-8") as f:
        template = f.read()
    
    # 替换关键片段
    new_html = html.replace("@@LEAFLET_CSS@@", open(os.path.join(BASE, "leaflet.css"), encoding="utf-8").read())
    html = html.replace("@@LEAFLET_JS@@", open(os.path.join(BASE, "leaflet.js"), encoding="utf-8").read())
    html = html.replace("@@IMGS@@", ",\n".join(f'"{k}":{{"b":"{v["b"]}","w":{v["w"]},"h":{v["h"]}}' for k, v in IMGS.items()))
    html = html.replace("@@ZONES@@", json.dumps(zones, ensure_ascii=False, separators=(",", ":")))
    html = html.replace("@@CITIES@@", json.dumps(cities, ensure_ascii=False, separators=(",", ":")))
    
    # 重写 loadOverview 函数（修正热区与标签逻辑）
    new_js = """
function loadOverview() {
  const c = ZONES[curContinent];
  curZone = null;
  heatLayer.clearLayers();
  labelLayer.clearLayers();
  showImg(c.overview, true);
  document.getElementById('cur-label').textContent = t(c.nameZh, c.nameEn);
  document.getElementById('backBtn').style.display = 'none';
  
  // 热区 + 标签（精确对齐）
  c.zones.forEach(function(z) {
    const img = IMGS[z.img];
    const cx = z.x * img.w, cy = z.y * img.h;
    // 热区（热区不可见，仅标签点击触发）
    const poly = L.polygon([
      [cy - h/2, cx - w/2],
      [cy-h/2, cx + w/2],
      [cy + h/2, cx + w/2],
      [cy + h/2, cx - w/2]
    ], {className: 'zone-heat', interactive: true});
    poly.on('click', function() { enterZone(z); });
    heatLayer.addLayer(poly);
    
    // 标签（点击文字即可下钻，不使用 popup）
    const lbl = L.marker([cy, cx], {
      icon: L.divIcon({
        className: 'zone-label',
        html: '<div style="color:#ffe9a8;font-weight:800;text-shadow:0 1px 3px #000;white-space:nowrap;transform:translate(-50%,-50%)">'
              + t(z.zh, z.en) + '</div>',
        iconSize:[0,0]
      }),
      interactive: true
    });
    labelLayer.addLayer(lbl);
  });
  
  // 城市快速入口
  (CITIES[curContinent] || []).forEach(function(ct) {
    const cty = L.marker([ct.y||30, ct.x||30], {
      icon: L.divIcon({
        className: 'zc',
        html: '<div style="background:#d97706;color:#fff;border:2px solid #fef08a;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800">★</div>',
        iconSize:[22,22],
        iconAnchor:[11,11]
      }),
      interactive: true
    });
    labelLayer.addLayer(cty);
  }
  
  updateSidebar();
}
"