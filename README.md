---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: 'e009b858-889c-4232-aa03-5b4e6eee8da7'
  PropagateID: 'e009b858-889c-4232-aa03-5b4e6eee8da7'
  ReservedCode1: 'aed1760a-39de-4951-abc0-253f337f67e5'
  ReservedCode2: 'aed1760a-39de-4951-abc0-253f337f67e5'
---

# 禅心祈福

一个纯前端的线上祈福应用，以禅意美学为核心，提供上香、许愿、供灯等祈福体验。

## 功能

- **上香** — 三种香型可选（檀香、沉香、清香），香炉最多同时燃三炷香，带实时烟雾动画
- **许愿** — 六种祈愿类型，写下心愿，查看祈福墙
- **供灯** — 为观音、弥勒、药师、地藏、文殊、财神供灯，供灯环呼吸动画
- **敲钟** — Web Audio API 合成寺庙铜钟音效
- **签到** — 每日签到，连续打卡统计
- **节气/佛诞日** — 24 节气 + 13 佛诞日数据，当天自动提醒
- **分享** — 复制链接、微信分享、生成祈福海报

## 技术特点

- 单 HTML 文件，零依赖，浏览器直接运行
- Canvas 烟雾粒子动画
- Web Audio API 合成音效（钟声、念经、供灯叮声）
- 全响应式适配：手机（含 iPhone SE / 横屏）、平板、PC、超宽屏
- localStorage 持久化存储所有数据，无需后端

## 使用方式

### 本地运行

直接用浏览器打开 `zen-blessing.html` 即可。

### Gitee Pages

1. 将仓库设为公开
2. 进入 Gitee 仓库 → 服务 → Gitee Pages → 启动
3. 访问 `https://mousejl.gitee.io/prayer-for-blessings/zen-blessing.html`

## 预览

手机端与 PC 端均自适应，暗色禅意风格，金色点缀，动画细腻。

## 许可证

MIT

> AI生成