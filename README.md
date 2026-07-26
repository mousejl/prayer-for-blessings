---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: 'cb53e4af-2a6b-4068-ae3a-2d1042e22aa4'
  PropagateID: 'cb53e4af-2a6b-4068-ae3a-2d1042e22aa4'
  ReservedCode1: 'c68aa397-209b-48f5-afe4-a060d125cf84'
  ReservedCode2: 'c68aa397-209b-48f5-afe4-a060d125cf84'
---

# 禅心祈福

一个纯前端的线上祈福应用，以禅意美学为核心，提供上香、许愿、供灯等祈福体验。

## 功能

- **上香** — 三种香型可选（檀香、沉香、清香），香炉最多同时燃三炷香，带实时烟雾动画
- **许愿** — 六种祈愿类型，写下心愿，查看祈福墙
- **供灯** — 为观音、弥勒、药师、地藏、文殊、财神供灯，供灯环呼吸动画
- **敲钟** — Web Audio API 合成寺庙铜钟音效
- **背景音乐** — 三首真实寺庙诵经录音（心经、大悲咒、六字大明咒），可切换曲目、调节音量
- **签到** — 每日签到，连续打卡统计
- **节气/佛诞日** — 24 节气 + 13 佛诞日数据，当天自动提醒
- **分享** — 复制链接、微信分享、生成祈福海报

## 技术特点

- 单 HTML 文件，零依赖，浏览器直接运行
- Canvas 烟雾粒子动画
- Web Audio API 合成音效（钟声、供灯叮声）
- 预录制真实诵经音频（22050Hz WAV），浏览器 `<audio>` 播放
- 全响应式适配：手机（含 iPhone SE / 横屏）、平板、PC、超宽屏
- localStorage 持久化存储所有数据，无需后端

## 项目结构

```
prayer-for-blessings/
├── zen-blessing.html        # 主页面（含全部 HTML/CSS/JS）
├── audio/
│   ├── heart_loop.wav       # 心经诵经音频（120s 循环）
│   ├── compassion_loop.wav  # 大悲咒诵经音频（120s 循环）
│   └── mantra_loop.wav      # 六字大明咒诵经音频（120s 循环）
├── README.md
└── .gitignore
```

## 部署手册

### 方式一：本地直接运行

最简单的方式，无需任何服务器：

1. 克隆仓库
   ```bash
   git clone https://gitee.com/mousejl/prayer-for-blessings.git
   ```
2. 用浏览器打开
   ```bash
   # macOS
   open prayer-for-blessings/zen-blessing.html
   # Windows
   start prayer-for-blessings/zen-blessing.html
   # Linux
   xdg-open prayer-for-blessings/zen-blessing.html
   ```

> 注意：背景音乐需要通过 HTTP 服务访问才能播放，直接打开文件（file:// 协议）时浏览器会阻止音频加载。如需背景音乐，请使用方式二。

### 方式二：本地 HTTP 服务器

推荐方式，可正常播放背景音乐：

1. 克隆仓库
   ```bash
   git clone https://gitee.com/mousejl/prayer-for-blessings.git
   cd prayer-for-blessings
   ```
2. 启动本地服务器（任选一种）

   **Python（推荐，系统自带）**
   ```bash
   # Python 3
   python3 -m http.server 8080
   # Python 2
   python -m SimpleHTTPServer 8080
   ```

   **Node.js**
   ```bash
   npx serve -l 8080
   ```

   **PHP**
   ```bash
   php -S localhost:8080
   ```

3. 浏览器访问 `http://localhost:8080/zen-blessing.html`

### 方式三：GitHub Pages

1. 在 GitHub 创建新仓库（如 `prayer-for-blessings`）
2. 推送代码
   ```bash
   git remote add github https://github.com/<你的用户名>/prayer-for-blessings.git
   git push github main
   ```
3. 进入 GitHub 仓库 → Settings → Pages
4. Source 选择 `main` 分支，目录选 `/ (root)`
5. 点击 Save，等待部署完成（约 1 分钟）
6. 访问 `https://<你的用户名>.github.io/prayer-for-blessings/zen-blessing.html`

### 方式四：Vercel

1. 注册 [Vercel](https://vercel.com) 账号（支持 GitHub 登录）
2. 点击 "New Project" → Import Git Repository
3. 选择你的 GitHub 仓库（或直接粘贴 Gitee 仓库的 Git URL）
4. Framework Preset 选择 "Other"
5. Output Directory 保持默认（root）
6. 点击 Deploy
7. 部署完成后获得访问地址，如 `https://prayer-for-blessings.vercel.app/zen-blessing.html`

### 方式五：Netlify

1. 注册 [Netlify](https://www.netlify.com/) 账号
2. 点击 "Add new site" → "Import an existing project"
3. 连接 GitHub 仓库（或拖拽项目文件夹到页面）
4. Build command 留空，Publish directory 设为根目录
5. 点击 Deploy site
6. 获得访问地址，如 `https://random-name.netlify.app/zen-blessing.html`

### 方式六：Cloudflare Pages

1. 注册 [Cloudflare](https://dash.cloudflare.com/) 账号
2. 进入 Workers & Pages → Create → Pages → Connect to Git
3. 选择 GitHub 仓库
4. Framework preset 选择 "None"
5. Build command 留空，Build output directory 设为 `/`
6. 点击 Save and Deploy
7. 获得 `https://<项目名>.pages.dev/zen-blessing.html` 访问地址

## 自定义部署

### 修改音频文件

音频文件位于 `audio/` 目录，支持 WAV 格式。如需替换：

1. 准备新的 WAV 音频文件（建议 22050Hz 单声道，文件更小）
2. 替换对应文件：`heart_loop.wav`（心经）、`compassion_loop.wav`（大悲咒）、`mantra_loop.wav`（六字大明咒）
3. 如文件名不同，需修改 `zen-blessing.html` 中 `audioFiles` 对象的路径

### 修改采样率降低体积

当前音频为 22050Hz 单声道 16bit WAV，约 5MB/文件。如需更小体积：

```python
import wave, struct

with wave.open('audio/heart_loop.wav', 'rb') as w:
    rate = w.getframerate()
    frames = w.getnframes()
    data = w.readframes(frames)

# 降采样到 8000Hz
ratio = rate // 8000
resampled = data[::ratio]  # 简单降采样

with wave.open('audio/heart_loop_8k.wav', 'wb') as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(8000)
    w.writeframes(resampled)
```

### 添加 HTTPS 证书（本地部署）

如需在本地通过 HTTPS 访问（某些浏览器 API 要求安全上下文）：

```bash
# 使用 mkcert 生成本地证书
brew install mkcert
mkcert -install
mkcert localhost

# 使用 Python 启动 HTTPS 服务器
python3 -c "
import http.server, ssl
server = http.server.HTTPServer(('localhost', 8443), http.server.SimpleHTTPRequestHandler)
server.socket = ssl.wrap_socket(server.socket, certfile='localhost.pem', keyfile='localhost-key.pem', server_side=True)
server.serve_forever()
"
```

## 浏览器兼容性

| 浏览器 | 最低版本 | 备注 |
|--------|----------|------|
| Chrome | 49+ | 完全支持 |
| Firefox | 52+ | 完全支持 |
| Safari | 10.1+ | 完全支持 |
| Edge | 14+ | 完全支持 |
| iOS Safari | 10.3+ | 音频需用户点击后播放 |
| Android Chrome | 49+ | 完全支持 |

> 移动端浏览器因自动播放策略限制，背景音乐需要用户点击播放按钮后才能开始。

## 常见问题

**Q: 背景音乐没有声音？**
A: 浏览器要求用户交互后才能播放音频，请点击页面上的播放按钮。确保通过 HTTP 服务器访问（非 file:// 协议）。

**Q: 手机端音频播放卡顿？**
A: 移动端浏览器可能对音频缓冲有限制，建议使用 Chrome 或 Safari 最新版本。

**Q: 如何清除所有数据？**
A: 在浏览器控制台执行 `localStorage.clear()` 并刷新页面。

**Q: Gitee Pages 还能用吗？**
A: Gitee Pages 免费版已于 2026 年下架，建议使用 GitHub Pages、Vercel、Netlify 或 Cloudflare Pages 替代。

## 许可证

MIT

> AI生成