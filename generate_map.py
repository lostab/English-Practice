#!/usr/bin/env python3
"""生成 wow_map.html —— 魔兽世界巫妖王之怒 多级下钻互动地图（单文件版）"""
import json, base64, os

BASE = "D:/work/Hermes/testprep-app"

# 1. 读取数据
with open(f"{BASE}/.mapdata.json", "r") as f:
    MAPS = json.load(f)          # {tag: [b64, height, width]}
with open(f"{BASE}/.zones.json", "r", encoding="utf-8") as f:
    ZONES = json.load(f)
with open(f"{BASE}/leaflet.css", "r", encoding="utf-8") as f:
    LEAFLET_CSS = f.read()
with open(f"{BASE}/leaflet.js", "r", encoding="utf-8") as f:
    LEAFLET_JS = f.read()

# 2. 生成 JS 数据块（把 base64 数据注入 JS 变量）
js_images = []
for tag, (b64, h, w) in MAPS.items():
    js_images.append(f'"{tag}":{{b:"{b64}",w:{w},h:{h}}}')
js_images_str = ",\n".join(js_images)
js_zones = json.dumps(ZONES, ensure_ascii=False)

# 3. 组装 HTML（模板 + 占位符替换，避免 f-string 大括号问题）
TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>魔兽世界：巫妖王之怒 (WotLK 3.3.5) 世界地图</title>
<style>
@@LEAFLET_CSS@@
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; margin:0; padding:0; }
html,body { width:100%; height:100%; background:#0a0e17; color:#d4af37; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Microsoft YaHei",sans-serif; overflow:hidden; }
#header { position:absolute; top:0; left:0; right:0; height:54px; background:linear-gradient(180deg,#151d2e,#0a0e17); border-bottom:2px solid #8c6d1f; display:flex; align-items:center; gap:12px; padding:0 14px; z-index:1000; box-shadow:0 4px 16px rgba(0,0,0,.8); }
.logo { flex:0 0 auto; }
.logo h1 { font-size:15px; color:#f3f4f6; font-weight:800; letter-spacing:1px; margin:0; text-shadow:0 0 8px rgba(212,175,55,.4); }
.logo span { font-size:10px; color:#9aa4b5; display:block; }
.tabs { display:flex; gap:5px; background:#202a3f; padding:3px; border-radius:7px; border:1px solid #37415a; }
.tab-btn { background:transparent; border:none; color:#aab4c8; padding:5px 12px; border-radius:5px; font-size:12px; cursor:pointer; font-weight:600; transition:.2s; }
.tab-btn.active,.tab-btn:hover { background:#b8860b; color:#fff; box-shadow:0 2px 8px rgba(184,134,11,.5); }
.spacer { flex:1; }
.lang-btn { background:#202a3f; border:1px solid #37415a; color:#fbbf24; padding:5px 12px; border-radius:5px; font-size:12px; cursor:pointer; font-weight:700; }
.lang-btn:hover { background:#2c3854; }
#map { position:absolute; top:54px; bottom:0; left:0; right:0; background:#060a12; }
.path-btn { position:absolute; top:62px; left:12px; z-index:1001; background:#202a3f; border:1px solid #8c6d1f; color:#e8d9a8; padding:6px 12px; border-radius:5px; font-size:12px; cursor:pointer; display:none; align-items:center; gap:6px; }
.path-btn:hover { background:#2c3854; }
#zoom-hint { position:absolute; bottom:18px; right:14px; z-index:1000; background:rgba(10,14,23,.85); border:1px solid #8c6d1f; color:#c9b97e; padding:6px 12px; border-radius:6px; font-size:11px; pointer-events:none; }
.sidebar-toggle { position:absolute; bottom:20px; left:16px; z-index:1000; background:#202a3f; border:2px solid #8c6d1f; color:#fbbf24; width:46px; height:46px; border-radius:50%; font-size:20px; display:flex; align-items:center; justify-content:center; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,.6); }
.sidebar-toggle:hover { background:#2c3854; }
#sidebar { position:absolute; top:54px; left:-290px; width:290px; bottom:0; background:rgba(13,18,30,.94); backdrop-filter:blur(12px); border-right:2px solid #8c6d1f; z-index:999; transition:left .3s ease; display:flex; flex-direction:column; box-shadow:6px 0 22px rgba(0,0,0,.55); }
#sidebar.open { left:0; }
.sb-head { padding:14px 16px; border-bottom:1px solid #37415a; font-weight:700; color:#fbbf24; font-size:14px; display:flex; justify-content:space-between; align-items:center; }
.sb-content { flex:1; overflow-y:auto; padding:10px; }
.zone-item { padding:10px 12px; margin-bottom:6px; border-radius:6px; background:rgba(32,42,63,.55); border:1px solid #37415a; cursor:pointer; transition:.2s; }
.zone-item:hover { background:#2c3854; border-color:#b8860b; }
.zone-item .nm { font-size:13px; font-weight:600; color:#f3f4f6; }
.zone-item .lv { font-size:11px; color:#9aa4b5; margin-top:2px; }
/* Wow 风格弹窗 */
.leaflet-popup-content-wrapper,.leaflet-popup-tip { background:rgba(15,21,36,.96)!important; color:#f3f4f6!important; border:2px solid #b8860b; border-radius:8px; box-shadow:0 10px 34px rgba(0,0,0,.95); }
.leaflet-popup-content h3 { margin:0 0 6px; color:#fbbf24; font-size:14px; border-bottom:1px dashed #4b5563; padding-bottom:5px; display:flex; align-items:center; gap:8px; }
.badge { font-size:10px; padding:2px 7px; border-radius:3px; background:#8c1f1f; color:#fff; }
.badge.blue { background:#1f4e8c; }
.leaflet-popup-content p { margin:4px 0 0; font-size:12px; color:#c9d2e0; line-height:1.55; }
.leaflet-popup-content .act { margin-top:10px; display:flex; gap:6px; }
.btn-enter { background:linear-gradient(180deg,#b8860b,#8c6d1f); border:none; color:#fff; font-weight:700; font-size:12px; padding:6px 14px; border-radius:4px; cursor:pointer; }
.btn-enter:hover { filter:brightness(1.15); }
/* 区域热区 */
.zone-heat { fill:rgba(184,134,11,.14); stroke:#d4af37; stroke-width:2; stroke-dasharray:5,4; cursor:pointer; transition:fill .2s; }
.zone-heat:hover { fill:rgba(184,134,11,.32); }
@media(max-width:768px) { .logo span { display:none; } .logo h1 { font-size:12px; } .tab-btn { padding:4px 7px; font-size:11px; } }
</style>
</head>
<body>

<div id="header">
  <div class="logo">
    <h1 id="ui-title">魔兽世界 · 巫妖王之怒</h1>
    <span id="ui-subtitle">WotLK 3.3.5 世界地图 — 点击区域下钻查看细节</span>
  </div>
  <div class="tabs">
    <button class="tab-btn active" data-c="azeroth" onclick="switchContinent('azeroth',this)">艾泽拉斯</button>
    <button class="tab-btn" data-c="northrend" onclick="switchContinent('northrend',this)">诺森德</button>
    <button class="tab-btn" data-c="outland" onclick="switchContinent('outland',this)">外域</button>
  </div>
  <div class="spacer"></div>
  <button class="lang-btn" id="langBtn" onclick="toggleLang()">EN</button>
</div>

<div id="map"></div>

<button class="path-btn" id="backBtn" onclick="goOverview()">← <span id="backLabel">返回世界地图</span></button>

<div id="zoom-hint">🖱 滚轮缩放 · 拖动平移 · 点击区域进入</div>

<div class="sidebar-toggle" onclick="toggleSidebar()">🗺️</div>
<div id="sidebar">
  <div class="sb-head"><span id="sbTitle">区域导航</span><span style="cursor:pointer;font-size:16px" onclick="toggleSidebar()">✕</span></div>
  <div class="sb-content" id="sbList"></div>
</div>

<script>
@@LEAFLET_JS@@
</script>
<script>
/* ===== 地图图片数据（base64 内嵌） ===== */
const IMGS = {
@@IMGS@@
};
const ZONES = @@ZONES@@;
let curLang = 'zh';
let curContinent = 'azeroth';
let curView = 'overview';  // 'overview' or zone key
let overlay = null, heatLayer = null, markerLayer = null;

const map = L.map('map', {
  crs: L.CRS.Simple,
  minZoom: -2,
  maxZoom: 3,
  zoomSnap: 0.25,
  zoomDelta: 0.5,
  attributionControl: false,
  zoomControl: false
});
L.control.zoom({position:'bottomright'}).addTo(map);
heatLayer = L.layerGroup().addTo(map);
markerLayer = L.layerGroup().addTo(map);

function t(zh, en) { return curLang === 'zh' ? zh : en; }

function loadOverview(contKey) {
  const c = ZONES[contKey];
  const img = IMGS[c.overview];
  curView = 'overview';
  if (overlay) map.removeLayer(overlay);
  heatLayer.clearLayers();
  markerLayer.clearLayers();
  map.setMaxBounds(null);

  const bounds = [[0,0],[img.h,img.w]];
  overlay = L.imageOverlay('data:image/jpeg;base64,'+img.b, bounds).addTo(map);
  map.fitBounds(bounds, {padding:[10,10]});

  // 区域热区 + 标签
  c.zones.forEach(function(z) {
    const cx = z.x * img.w, cy = z.y * img.h;
    const w = z.w * img.w, h = z.h * img.h;
    const rect = [[cy-h/2, cx-w/2],[cy+h/2, cx-w/2],[cy+h/2, cx+w/2],[cy-h/2, cx+w/2],[cy-h/2, cx-w/2]];
    const poly = L.polygon(rect, {className:'zone-heat', interactive:true});
    poly.on('click', function() { enterZone(contKey, z); });
    heatLayer.addLayer(poly);

    const lblIcon = L.divIcon({
      className:'zone-label',
      html:'<div style="color:#ffe9a8;font-weight:800;font-size:13px;text-shadow:0 1px 3px #000,0 0 8px #000,0 0 12px rgba(0,0,0,.9);white-space:nowrap;transform:translate(-50%,-50%)">' + t(z.zh,z.en) + '</div>',
      iconSize:[0,0]
    });
    const lbl = L.marker([cy, cx], {icon:lblIcon, interactive:false});
    markerLayer.addLayer(lbl);
  });

  document.getElementById('backBtn').style.display = 'none';
  updateSidebar();
  map.setView([[0,0],[img.h,img.w]].center !== undefined ? map.getCenter() : [img.h/2, img.w/2], map.getZoom());
}

function enterZone(contKey, z) {
  const img = IMGS[z.img];
  curView = z.key;
  if (overlay) map.removeLayer(overlay);
  heatLayer.clearLayers();
  markerLayer.clearLayers();
  map.setMaxBounds(null);

  const bounds = [[0,0],[img.h,img.w]];
  overlay = L.imageOverlay('data:image/jpeg;base64,'+img.b, bounds).addTo(map);
  map.fitBounds(bounds, {padding:[10,10]});

  document.getElementById('backBtn').style.display = 'flex';
  document.getElementById('backLabel').textContent = curLang==='zh' ? '返回 '+ZONES[contKey].nameZh : 'Back to '+ZONES[contKey].nameEn;
  updateSidebar();
}

function goOverview() {
  loadOverview(curContinent);
}

function switchContinent(key, btn) {
  document.querySelectorAll('.tab-btn').forEach(function(b){ b.classList.remove('active'); });
  if (btn) btn.classList.add('active');
  curContinent = key;
  loadOverview(key);
}

function updateSidebar() {
  const c = ZONES[curContinent];
  document.getElementById('sbTitle').textContent = curLang==='zh' ? c.nameZh+' 区域' : c.nameEn+' Zones';
  const box = document.getElementById('sbList');
  box.innerHTML = '';
  c.zones.forEach(function(z) {
    const div = document.createElement('div');
    div.className = 'zone-item';
    div.innerHTML = '<div class="nm">' + t(z.zh,z.en) + '</div><div class="lv">' + z.desc + '</div>';
    div.onclick = function() { enterZone(curContinent, z); toggleSidebar(); };
    box.appendChild(div);
  });
}

function toggleLang() {
  curLang = curLang === 'zh' ? 'en' : 'zh';
  document.getElementById('langBtn').textContent = curLang==='zh' ? 'EN' : '中';
  document.getElementById('ui-title').textContent = t('魔兽世界 · 巫妖王之怒', 'World of Warcraft · WotLK');
  document.getElementById('ui-subtitle').textContent = t('WotLK 3.3.5 世界地图 — 点击区域下钻查看细节', 'WotLK 3.3.5 World Map — click a zone to zoom in');
  document.querySelectorAll('.tab-btn').forEach(function(b) {
    const k = b.getAttribute('data-c');
    b.textContent = t(ZONES[k].nameZh, ZONES[k].nameEn);
  });
  if (curView === 'overview') loadOverview(curContinent);
  else {
    const c = ZONES[curContinent];
    const z = c.zones.find(function(x){ return x.key===curView; });
    if (z) enterZone(curContinent, z);
  }
}

function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
}

// 初始加载
window.addEventListener('load', function() {
  loadOverview('azeroth');
});
</script>
</body>
</html>
"""

html = TEMPLATE
html = html.replace("@@LEAFLET_CSS@@", LEAFLET_CSS)
html = html.replace("@@LEAFLET_JS@@", LEAFLET_JS)
html = html.replace("@@IMGS@@", js_images_str)
html = html.replace("@@ZONES@@", js_zones)

with open(f"{BASE}/wow_map.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"生成完成: {len(html)/1024/1024:.1f} MB -> wow_map.html")
print(f"图片数: {len(MAPS)}, 大陆数: {len(ZONES)}")
print(f"占位符残留: {html.count('@@')}")