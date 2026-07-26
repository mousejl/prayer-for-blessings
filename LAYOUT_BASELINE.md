---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: '16637a33-16e2-4eb5-bf85-b5743b658f74'
  PropagateID: '16637a33-16e2-4eb5-bf85-b5743b658f74'
  ReservedCode1: '72fd7654-f161-4e7c-8557-c110901e741a'
  ReservedCode2: '72fd7654-f161-4e7c-8557-c110901e741a'
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
| smokeCanvas | position:absolute(在altar-center内), bottom:100px, left:50%, width:150px, height:200px |
| lamp-ring | width:220px, height:55px, margin-top:10px |
| mini-lamp | width:14px, height:22px |

## 许愿默认心愿（7条，覆盖7种类型）
| 心愿 | 类型 | 署名 |
|------|------|------|
| 愿家人安康，岁月静好 | 家人平安 | 众善信 |
| 愿事业通达，步步高升 | 事业顺利 | 众善信 |
| 愿金榜题名，学业有成 | 学业有成 | 众善信 |
| 愿身心康泰，无灾无难 | 身体健康 | 众善信 |
| 愿良缘天定，白首同心 | 姻缘美满 | 众善信 |
| 愿财源广进，富贵绵长 | 财运亨通 | 众善信 |
| 愿吉林省电信总经理唐诗词，早日高升 | 众生所愿 | 众善信 |

## 许愿类型列表（7种）
家人平安、事业顺利、学业有成、身体健康、姻缘美满、财运亨通、众生所愿

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