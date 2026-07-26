---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: '17bd342d-a477-4686-9296-0ae822795052'
  PropagateID: '17bd342d-a477-4686-9296-0ae822795052'
  ReservedCode1: 'cff1987b-ddb0-494b-9a9c-ddda49058391'
  ReservedCode2: 'cff1987b-ddb0-494b-9a9c-ddda49058391'
---

# 禅心祈福 - 布局参数基线

## 基础样式（桌面端）
| 元素 | 参数 |
|------|------|
| altar-area | flex:1, justify-content:center, overflow:hidden |
| altar-center | flex-direction:column, justify-content:center |
| buddha-wrap | position:relative, align-items:center |
| buddha-light | width:220px, height:220px, opacity:0.06/0.02 |
| buddha-icon | width:80px, height:120px, margin-bottom:8px |
| sticks-row | height:50px, gap:7px, margin-bottom:-2px |
| stick.lit | height:48px |
| burner | width:64px, height:28px |
| smokeCanvas | width:160px, height:200px, bottom:26px |
| lamp-ring | width:200px, height:50px, margin-top:8px |
| mini-lamp | width:14px, height:20px |

## 手机端（max-width:430px）— 当前生效
| 元素 | 参数 |
|------|------|
| altar-center | width:100%, height:480px, position:relative |
| buddha-wrap | position:absolute, top:0, left:50%, transform:translateX(-50%), z-index:2 |
| buddha-icon | width:270px, height:405px, margin-bottom:8px |
| buddha-light | width:720px, height:720px |
| burner-combo | position:absolute, bottom:0, left:50%, transform:translateX(-50%), z-index:3, margin-top:-160px |
| burner | width:70px, height:28px |
| stick.lit | height:50px |
| sticks-row | height:52px, gap:8px |
| smokeCanvas | width:150px, height:200px, bottom:24px |
| lamp-ring | width:220px, height:55px, margin-top:10px |
| mini-lamp | width:14px, height:22px |

## 手机端（max-width:430px）— 原始基线
| 元素 | 参数 |
|------|------|
| top-area | padding-bottom:4px |
| buddha-icon | width:90px, height:135px, margin-bottom:8px |
| buddha-light | width:240px, height:240px |
| burner | width:70px, height:28px |
| stick.lit | height:50px |
| sticks-row | height:52px, gap:8px |
| smokeCanvas | width:150px, height:200px, bottom:24px |
| lamp-ring | width:220px, height:55px, margin-top:10px |
| mini-lamp | width:14px, height:22px |

## 小屏兜底（max-width:360px）
| 元素 | 参数 |
|------|------|
| buddha-icon | width:80px, height:120px, margin-bottom:6px |
| burner | width:62px, height:26px |
| sticks-row | height:44px, gap:7px |
| stick.lit | height:44px |
| smokeCanvas | width:130px, height:180px, bottom:22px |
| lamp-ring | width:190px, height:48px, margin-top:8px |

## 横屏（max-height:500px landscape）
| 元素 | 参数 |
|------|------|
| buddha-icon | width:48px, height:72px, margin-bottom:2px |
| buddha-light | width:120px, height:120px |
| burner | width:48px, height:20px |
| stick.lit | height:28px |
| lamp-ring | width:120px, height:36px, margin-top:4px |

## 平板端（431px~768px）
| 元素 | 参数 |
|------|------|
| buddha-icon | width:72px, height:108px, margin-bottom:7px |
| buddha-light | width:200px, height:200px |
| burner | width:60px, height:26px |

> AI生成