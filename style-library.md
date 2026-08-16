# 风格语汇库（57 种 UI 美学方向）

> 来源：joshhu/uitest 的 57 个风格 landing page，已萃取每种的真实配色/字体/招牌技法，融合成可挑选、可组合的「配方卡」。
> **用途**：当页面需要一个「明确的美学方向」（不只是干净），从这里挑一个当主调，照它的配方做。默认仍遵守 SKILL.md 的克制原则——**风格是选出来的，不是堆出来的**。

## 怎么用这个库（重要）

1. **先定情境**：产品站 / 后台 dashboard / 作品集 / 玩乐性页面？情境决定能挑的风格范围。
2. **挑 1 个主调**：从下面选一种最贴合的，照它的「配方」（配色公式 + 字体 + 招牌技法）做。
3. **最多再借 1 个点缀**：主调之外，可以从别的风格借「一个」招牌手法当亮点（见文末「组合规则」）。别同时用两个大声的风格。
4. **落地**：技法能用 Tailwind 表达就用 Tailwind；招牌效果（毛玻璃、内阴影、霓虹）写进 `<style>` 或 `@layer`。参考实现都在本 repo 的 `styles/NN-*.html`，需要时直接开来抄结构。

---

## A. 通用美学 (01–19)

| # | 风格 | 一句话调性 | 配色公式 | 字体 | 招牌技法 |
|---|------|-----------|---------|------|---------|
| 01 | **Minimalism / Swiss** | 少即是多，靠留白与网格 | 米白 `#f5f1e8` + 纯黑 + 一个灰 | Helvetica Neue / Inter | 大量留白、严格网格、无装饰、超大标题 |
| 02 | **Neumorphism** | 柔和凸起，同色系浮雕 | 单一浅灰 `#e8e8e8` 基底，无对比色 | Inter | 双向 `box-shadow`（亮+暗）做凸/凹，`inset` 做按下 |
| 03 | **Glassmorphism** | 毛玻璃透明层叠 | 彩色渐层底 `#667eea→#764ba2→#f093fb` | Inter | `backdrop-filter: blur(20px)` + 半透明白 + 细白边 |
| 04 | **Brutalism** | 粗野、故意「丑」、高冲击 | 三原色 `#ff0000 #0000ff #ffff00` + 黑白 | Inter + Space Mono | 粗黑边、硬阴影（无模糊）、无圆角、错位排版 |
| 05 | **3D / Hyperrealism** | 拟真立体、金属光泽 | 金 `#ffd700` + 银 `#c0c0c0` + 紫蓝渐层 | Inter | 多层渐层做体积、高光、真实材质感 |
| 06 | **Vibrant Block** | 高饱和色块拼贴 | 霓虹青/紫/绿/粉 `#00ffff #bf00ff #39ff14 #ff1493` | Space Grotesk | 大色块、硬边界、粗体标题 |
| 07 | **Dark Mode (OLED)** | 纯黑护眼 + 单一亮色 | `#121212` 底 + 一个荧光（绿 `#39ff14` 或蓝） | Inter | 纯黑省电、单一发光强调色、`text-shadow` 微光 |
| 08 | **Accessible / Ethical** | 高对比、可读性优先 | 蓝 `#0066cc` + 红 `#d32f2f` + 纯黑白（AAA 对比） | Inter | 大字、强对比、清楚 focus 状态、无纯装饰 |
| 09 | **Claymorphism** | 黏土 3D、圆润可爱 | 马卡龙粉蓝绿 `#fdbcb4 #add8e6 #98ff98` | Nunito | 大圆角、柔和双阴影、粗边、鼓起感 |
| 10 | **Aurora UI** | 极光流动漸层 | 蓝紫粉青多色 `#0080ff #8b00ff #ff1493 #00ffff` | Inter | 放射渐层 + `blur` 光晕 + `@keyframes` 缓慢流动 + 毛玻璃 |
| 11 | **Retro-Futurism** | 80 年代对未来的想像 | 青+洋红 `#00ffff #ff006e` on 深蓝 `#1a1a2e` | Orbitron / Press Start 2P | 霓虹 `text-shadow`、网格地平线、扫描线动画 |
| 12 | **Flat Design 2.0** | 扁平、轻阴影、色彩明快 | 明快多色 `#3498db #e74c3c #27ae60 #f39c12` | Open Sans | 无拟真、轻微层次、纯色块、简单图标 |
| 13 | **Skeuomorphism** | 拟物、仿真实材质 | 木纹米 `#deb887` + 灰阶金属 | Georgia | `inset` 阴影、材质渐层、缝线/皮革/木头质感 |
| 14 | **Liquid Glass** | 流动的玻璃（Apple 感） | 紫蓝粉渐层 `#667eea #764ba2 #f093fb` | Inter | 毛玻璃 + 流动 `@keyframes` + 光晕，比 03 更动态 |
| 15 | **Motion-Driven** | 一切靠动画说话 | 中性底，动画抢戏 | Inter | `@keyframes` 主导：进场、悬停、滚动触发 |
| 16 | **Micro-interactions** | 细节反馈让界面「活」 | Tailwind 系统色 `#3b82f6 #ef4444 #22c55e` | Inter | 悬停/点击的微动画、状态过渡、按钮涟漪 |
| 17 | **Inclusive Design** | 无障碍且温暖 | 深蓝 `#003366` + 高对比橙 | Atkinson Hyperlegible | 易读字体、清楚层级、大点击区、友善语气 |
| 18 | **Zero Interface** | 隐形 UI，内容即界面 | 近白 `#fafafa #f5f1e8`，极淡 | Inter | 几乎无边框/按钮、留白引导、微动画提示 |
| 19 | **Soft UI Evolution** | 柔和新拟态进化版 | 粉彩天蓝 `#87ceeb #ffb6c1 #90ee90` | Inter | 柔和阴影 + 细边 + 淡渐层，比 02 更有色彩 |

## B. Landing Page 结构 (20–27)

> 这组重点不是「视觉风格」而是「页面结构策略」，可套在任一视觉风格上。

| # | 结构 | 核心策略 | 什么时候用 |
|---|------|---------|-----------|
| 20 | **Hero-Centric** | 巨大主视觉 + 一句话价值 + 单一 CTA | 品牌/产品首页，主打第一印象 |
| 21 | **Conversion-Optimized** | 全页为转换服务，多处 CTA、社会证明、去除干扰 | 落地页、注册页、卖东西 |
| 22 | **Feature-Rich Showcase** | 分区展示多功能，图文交错 | 功能多的 SaaS |
| 23 | **Minimal & Direct** | 一屏讲完，噪点纹理增质感 | MVP、极简产品 |
| 24 | **Social Proof-Focused** | 评价/logo 墙/数据先行 | 需要建立信任的 B2B |
| 25 | **Interactive Demo** | 让用户在页面里玩产品 | 工具类，「看不如试」 |
| 26 | **Trust & Authority** | 权威感排版（衬线标题 Playfair） | 金融/法律/医疗/顾问 |
| 27 | **Storytelling** | 叙事线带读者走（衬线 Merriweather） | 品牌故事、募资、理念页 |

## C. BI / Analytics Dashboard (28–37)

> 后台/数据界面。共同点：**信息密度高、等宽字体标数字（JetBrains Mono）、语义色（涨绿跌红）独立于品牌色**。参考 dataviz skill 搭配。

| # | 类型 | 重点 |
|---|------|------|
| 28 | **Data-Dense Dashboard** | 高密度、多卡片、Inter + JetBrains Mono，先摘要后细节 |
| 29 | **Heatmap & Density** | 深蓝阶 `#1e293b→#38bdf8` 做热力/密度视觉 |
| 30 | **Executive Summary** | 高管视角：大数字 KPI、少而精、克制 |
| 31 | **Real-Time Monitoring** | 即时跳动、`@keyframes` 脉冲、等宽数字、状态灯 |
| 32 | **Drill-Down** | 可逐层下钻，面包屑 + 展开 |
| 33 | **Comparative** | 并排对比、差异高亮 |
| 34 | **Predictive** | 预测区间用虚线边框区分实际/预测 `#3b82f6 #a855f7` |
| 35 | **User Behavior** | 漏斗、路径、留存曲线 |
| 36 | **Financial** | 深灰 `#334155` + 涨绿 `#10b981`，等宽对齐金额 |
| 37 | **Sales Intelligence** | 管线、目标达成、排行榜 |

## D. 潮流 / 高个性 (38–57)

| # | 风格 | 一句话调性 | 配色 / 字体 | 招牌技法 |
|---|------|-----------|-----------|---------|
| 38 | **Neubrutalism** | 野兽派的可爱版 | 糖果色 `#ff6b6b #ffe66d #4ecdc4` on 米白 / Space Grotesk | 粗黑边 + 硬阴影（偏移无模糊）+ 高饱和块 |
| 39 | **Bento Box** | 便当格子拼版 | 中性 + 重点色 / Inter | 大小不一的圆角卡片网格，一格一信息 |
| 40 | **Y2K Revival** | 千禧金属+荧光 | 洋红/青/黄 `#ff00ff #00ffff #ffff00` / Orbitron | 铬合金渐层、星芒、霓虹字、闪 |
| 41 | **Cyberpunk** | 赛博霓虹夜城 | 洋红+青 on 黑 / Orbitron + Share Tech Mono | 霓虹 `text-shadow`、故障(glitch)动画、扫描线 |
| 42 | **Organic Biophilic** | 自然、植物、大地色 | 森林绿大地 `#3e4a32 #8fbc8f #f5f1e8` / Cormorant Garamond + Nunito | 有机曲线、衬线优雅标题、柔和 |
| 43 | **AI-Native** | AI 产品的科技渐层 | 紫蓝 `#667eea #764ba2` / Inter | 渐层 + 缓动画 + 对话式布局、光效 |
| 44 | **Memphis Revival** | 80s 孟菲斯几何涂鸦 | 糖果色 / Archivo Black + Poppins | `clip-path` 几何碎片、波点、斜线、撞色 |
| 45 | **Vaporwave** | 蒸汽波、故障美学 | 粉+铬 `#ff71ce #c0c0c0` / Press Start 2P + VT323 | 落日网格、雕像、`@keyframes` 故障、日文点缀 |
| 46 | **Dimensional Layering** | 多层 z 轴堆叠景深 | 中性 / Inter | 阴影+错位造景深、层层浮起 |
| 47 | **Exaggerated Minimalism** | 极简但字超大 | 黑白 / Space Grotesk | 巨型字 + 极简元素，靠尺度对比 |
| 48 | **Kinetic Typography** | 会动的文字主导 | 高对比 / Bebas Neue | 文字 `@keyframes`：滚动、变形、逐字进场 |
| 49 | **Parallax Storytelling** | 视差滚动叙事 | 中性 + 衬线 Playfair | 滚动触发的分层视差、章节式 |
| 50 | **Swiss Modernism 2.0** | 瑞士国际主义现代版 | 黑白红经典 / Helvetica Neue | 严格栅格、左对齐、大量留白、无装饰（最安全的高级感底） |
| 51 | **HUD / Sci-Fi** | 科幻抬头显示器 | 荧光青 on 黑 / Orbitron + Share Tech Mono | 边角刻度、扫描动画、发光边框、数据环 |
| 52 | **Pixel Art / Retro Gaming** | 8-bit 像素 | Game Boy 绿 `#8bac0f #0f380f #306230` / Press Start 2P | 像素边、无抗锯齿、硬边框、点阵 |
| 53 | **Bento Grids** | 便当格进阶（更精致） | 中性 / Inter | 同 39 但更克制、留白更足 |
| 54 | **Neubrutalism v2** | 新野兽派精致化 | 黄粉青紫 `#ffe156 #ff6b6b #4ecdc4 #a388ee` / Space Grotesk | 粗边+硬阴影，但配色更协调、圆角回归 |
| 55 | **Spatial UI** | visionOS 空间界面 | 中性透明 / Inter + SF Pro | 3D `perspective` + 毛玻璃 + 悬浮层，景深 |
| 56 | **E-Ink / Paper** | 电子墨水纸感 | 墨黑 `#1a1a1a` on 纸白 `#f5f1eb` / JetBrains Mono + Newsreader | 无阴影、高对比、噪点纸纹、衬线阅读 |
| 57 | **Gen Z Chaos** | Z 世代混乱美学 | 撞色 `#4ecdc4 #ff6b6b #ffe66d #a388ee` / Clash Display + Space Mono | 故意歪斜、虚线、贴纸感、混排字体、动画乱入 |

---

## 组合规则（怎么「搭配」而不搞砸）

**黄金法则：一个大声 + 其余安静。** 一页只能有一个抢戏的美学主张。

1. **结构 + 皮肤 分层想**
   - 先从 B 组挑「结构策略」（Hero / Bento / Storytelling…）＝页面骨架。
   - 再从 A/D 组挑「视觉皮肤」（Glassmorphism / Neubrutalism / Swiss…）＝表面质感。
   - 例：`Bento Box 结构` + `Glassmorphism 皮肤` = 现在很流行的玻璃便当格。

2. **安全的「底」+ 一个「点缀」**
   - 底用低风险的：**Swiss Modernism (50) / Minimalism (01) / Bento (39/53)**——这些当骨架永远不出错。
   - 点缀从高个性组借「一个」手法：一段 Kinetic Typography 的标题、一个 Neubrutalism 的硬阴影按钮、一块 Aurora 的渐层背景。**只借一个。**

3. **别硬凑的组合**
   - 两个高饱和风格叠（Cyberpunk + Memphis）＝灾难。
   - 拟真类（Skeuomorphism / 3D）+ 扁平类（Flat / Swiss）＝打架。
   - 毛玻璃(03/14/55) 要有彩色/复杂背景才有意义，纯白底上看不出来。

4. **配色公式**（不管选哪个风格都成立）
   - 1 主色（品牌）+ 中性灰阶 + 至多 1 强调色。
   - 语义色（成功绿/警告黄/危险红）独立计算，不算进「颜色数」。
   - 深色版单独调，不是把浅色反相。

5. **字体搭配**（从上表直接拿现成组合）
   - 权威感：Playfair Display（标题）+ Inter（正文）
   - 科技感：Orbitron / Space Grotesk（标题）+ Inter（正文）
   - 阅读/叙事：Merriweather / Newsreader / Cormorant（衬线正文）
   - 数据：Inter + JetBrains Mono（数字）
   - 玩乐：Clash Display / Archivo Black / Bebas Neue（展示字）

6. **落地建议**
   - React 项目：结构照旧走 Tailwind + shadcn/ui（见 SKILL.md），把选定风格的「配方」映射成 Tailwind config（颜色、圆角、阴影）+ 少量 `<style>` 招牌效果。
   - 纯 HTML / artifact：直接照 `styles/NN-*.html` 抄骨架再改内容。
   - 永远先问：这个情境需要「有个性」还是「专业干净」？**多数产品/后台选干净（走 SKILL.md 默认），只有作品集、活动页、玩乐性页面才放开个性。**
