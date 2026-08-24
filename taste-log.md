# 韡寧的 UI 品味檔（她挑出來的「好看」）

> 會成長的檔案。生成 UI 前**先讀**，讓產出偏向她的品味；她挑完後**追加紀錄**。
> 目標：讓「好看」從抽象變成她本人的具體偏好，越用越準。

## 怎麼維護（每輪流程）
1. 生成一批 UI（用 style-library.md 選不同風格，標註每個用了哪個風格 #）。
2. 韡寧挑喜歡的（和明確不喜歡的）。
3. 在「紀錄」區追加：日期、她選/嫌哪個、原話、歸納。
4. 反覆出現的偏好升級到「已確認偏好」。

## 已確認偏好（當規則，生成時務必套用）

- **語言：一律繁體中文（台灣用語），嚴禁簡體字。** 她是台灣人，簡體字是直接扣分。
- **字體必須配合風格美學**（她對字體極敏感，會用「字體有沒有對上設計」來判斷好壞）：
  - 圓潤/柔和風格（Glassmorphism、Claymorphism、Soft UI）→ 用**圓體**（如 Baloo 2、Quicksand、Varela Round、Zen Maru Gothic）。
  - 編輯/Swiss/權威/敘事風 → 用**襯線報紙體**（如 Noto Serif TC、Playfair Display、Newsreader）。她明講 Swiss 想要「報紙體」。
  - Neubrutalism/展示 → 粗展示字（Archivo Black、Space Grotesk）——她說 #38 是唯一字體對上的。
  - **避免每個都用 Inter/Helvetica** 那種通用預設 → 她覺得「太有 AI 風、太通用」（嫌 Real-Time Monitoring #31 太有 AI 感）。
- **避免「通用 AI 感」**：不要一看就是 AI 生的那種安全樣板；每個風格要有自己鮮明的字體與細節。

## 紀錄（每輪追加，最新在上）

### 2026-08-24（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（curl 連線逾時無回應，HTTP exit 56），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- 本批風格（避開近 3 天用過的 #10/#26/#40/#37/#09/#51/#01/#43/#24/#52/#35/#12/#02/#18/#39/#44/#32/#49，優先挑選至今完全沒用過的風格，並跨 A/B/C/D 族群）：Dark Mode / OLED #07（全新族群，避免 Inter，改用 Instrument Sans + Space Mono，做成深夜專注工作模式 App「夜半」，純黑底單一螢光綠強調色）、Accessible / Ethical #08（全新族群，套用配方指定的無障礙專用字體 Atkinson Hyperlegible + Noto Sans TC，做成高對比視障友善網路銀行「安視銀行」，WCAG AAA 對比、大按鈕、鍵盤可完全操作）、Retro-Futurism #11（全新族群，配方建議 Orbitron/Press Start 2P 已多輪重複，改用全新組合 Michroma + Rajdhani，做成復古未來太空電台 App「電波電台」）、Feature-Rich Showcase #22（B 組 landing 結構全新類型，避免 Inter，改用 Onest + Noto Sans TC，做成團隊協作 SaaS 功能總覽頁「整備」）、Predictive Dashboard #34（BI 儀表板全新類型，避免 Inter/JetBrains Mono，改用 Red Hat Text + Roboto Mono，虛線邊框區分實際/預測值，做成庫存需求預測後台「先知」）、Spatial UI #55（D 組最後一個全新類型，本質上是毛玻璃+景深的柔和風格，依「圓潤風配圓體」偏好改用 Nunito + Quicksand，做成智慧家庭空間控制中心 App「境」）。全數繁體中文文案，中文字元皆保留 Noto Sans/Serif TC 作為 fallback。D 組 38–57 目前已全數使用過至少一次。

### 2026-08-23（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（curl CONNECT tunnel 403，WebFetch 回 EGRESS_BLOCKED），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- ⚠️ 本輪 GH_TOKEN 直連 GitHub API（publish.py）仍被環境閘道擋下（403），改用 GitHub MCP 工具（push_files）發布，已確認 commit 成功（e470c4b7）。
- ⚠️ 本輪 Telegram 通知（步驟 8）也被環境網路政策擋下（curl CONNECT tunnel 403，WebFetch 同樣回 EGRESS_BLOCKED），與 Firebase 同一機制擋下，非帳號或 bot token 問題。畫廊已正常生成並發布到 GitHub，只是這次沒有 Telegram 訊息推播，請直接看連結：https://raw.githack.com/weiwei0607/ui-daily/master/reviews/2026-08-23/index.html
- 本批風格（避開近 3 天用過的 #04/#13/#17/#29/#46/#47/#10/#26/#40/#37/#09/#51/#01/#43/#24/#52/#35/#12，並優先挑選至今完全沒用過的風格）：Neumorphism #02（全新族群，柔和同色系浮雕本質上也是「圓潤風」，依偏好套圓體，改用全新組合 Comfortaa + Kosugi Maru，避免 Inter，做成靜心冥想 App「靜語」）、Zero Interface #18（全新族群，隱形 UI 以內容/文字為主，比照「敘事/編輯配報紙體」精神，改用 Fraunces + Noto Serif TC，做成一次只記一件事的極簡筆記「留白」）、Bento Box #39（全新族群，避免預設 Inter，改用 Figtree + Noto Sans TC，做成生活記帳 App「格子帳」）、Memphis Revival #44（全新族群，配方建議 Archivo Black 已在前幾輪 Neubrutalism 系列重複出現，改用 Righteous + Poppins 做出同樣分量的孟菲斯塗鴉感，做成潮流玩具盲盒商店「怪奇盒」）、Drill-Down Dashboard #32（BI 儀表板全新類型，避免 Inter/JetBrains Mono，改用 Albert Sans + IBM Plex Mono，做成電商後台銷售下鑽分析「鑽點」）、Parallax Storytelling #49（配方建議 Playfair 已多輪重複使用，改用全新組合 Bitter + Noto Serif TC 延續「敘事配報紙體」偏好，做成老屋改造紀實故事頁「時光修復」）。全數繁體中文文案，中文字元皆保留 Noto Sans/Serif TC 作為 fallback。

### 2026-08-22（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（連線逾時 HTTP 000），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- ⚠️ 本輪 GH_TOKEN 直連 GitHub API（publish.py）再度被環境閘道擋下（403），改用 GitHub MCP 工具（push_files）發布。
- ⚠️ 本輪 Telegram 通知（步驟 8）也被環境網路政策擋下（`api.telegram.org` 連線逾時 HTTP 000），與 Firebase 同一機制擋下，非帳號或 bot token 問題。畫廊已正常生成並發布到 GitHub，只是這次沒有 Telegram 訊息推播，請直接看連結：https://raw.githack.com/weiwei0607/ui-daily/master/reviews/2026-08-22/index.html
- 本批風格（避開近 3 天用過的 #19/#56/#06/#57/#53/#33/#04/#13/#17/#29/#46/#47/#10/#26/#40/#37/#09/#51，並優先挑選至今完全沒用過的風格）：Minimalism/Swiss #01（延續她要「報紙體」的偏好，Noto Serif TC + Lora，全新族群，做成質感選物雜誌訂閱「讀誌」）、AI-Native #43（全新族群，避免 Inter 改用 Schibsted Grotesk + Noto Sans TC，做成 AI 智慧郵件助理「信匣」）、Social Proof-Focused #24（landing 結構型，全新族群，避免撞前幾輪的字體改用 Geologica + Noto Sans TC，做成 B2B SaaS 企業導入見證頁「導軌」）、Pixel Art/Retro Gaming #52（全新族群，避免與 08-19 Vaporwave 重複的 Press Start 2P + VT323，改用 Pixelify Sans + Space Mono 做出更純粹的 Game Boy 綠像素感，做成復古遊戲成就追蹤 App「PIXELQUEST」）、User Behavior Dashboard #35（BI 儀表板全新類型，避免 Inter/JetBrains Mono 改用 Public Sans + Roboto Mono，做成用戶行為分析後台「行為雷達」）、Flat Design 2.0 #12（全新族群，配方建議 Open Sans 偏通用，改用 Be Vietnam Pro + Noto Sans TC，做成產地直送生鮮雜貨電商「菜籃仔」）。全數繁體中文文案，中文字元皆保留 Noto Sans/Serif TC 作為 fallback。

### 2026-08-21（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（CONNECT tunnel 403），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- ⚠️ 本輪 GH_TOKEN 直連 GitHub API 的 `/user` 端點測試回 200，但 publish.py 實際用到的 repo 範圍端點（`/repos/.../git/ref/...`）仍被環境閘道擋下（403「GitHub access is not enabled for this session」），與前幾輪一致，改用 GitHub App／MCP 工具（push_files）發布。
- ⚠️ 本輪 Telegram 通知（步驟 8）仍被環境網路政策擋下（`api.telegram.org` 連線逾時/000），與 Firebase 同一機制擋下，非帳號或 bot token 問題。畫廊已正常生成並發布到 GitHub，只是這次沒有 Telegram 訊息推播，請直接看連結：https://raw.githack.com/weiwei0607/ui-daily/master/reviews/2026-08-21/index.html
- 本批風格（避開近 3 天用過的 #38/#14/#27/#41/#30/#48/#19/#56/#06/#57/#53/#33/#04/#13/#17/#29/#46/#47，並刻意避免與近期重複的字體組合）：Aurora UI #10（全新族群，避免預設 Inter，改用 Instrument Sans，做成靈光 AI 寫作靈感助理 SaaS）、Trust & Authority #26（延續「編輯/權威風配報紙體」偏好，換掉前幾輪用過的 Playfair/Newsreader，改用全新組合 Source Serif 4 + Noto Serif TC，做成恆信法律事務所官網）、Y2K Revival #40（全新族群，配方建議 Orbitron 已用於 #41 Cyberpunk，改用 Audiowide + Rajdhani 做出鉻銀感但避免重複，做成千禧特快復古潮流電商）、Sales Intelligence #37（BI 儀表板全新類型，避免 Inter，改用 Lexend + IBM Plex Mono，做成業務戰情室銷售智庫）、Claymorphism #09（延續「圓潤風配圓體」偏好，換掉前幾輪用過的 Baloo 2/Quicksand/Zen Maru Gothic，改用全新組合 Fredoka + M PLUS Rounded 1c，做成軟軟習慣養成 App）、HUD / Sci-Fi #51（全新族群，配方建議 Orbitron+Share Tech Mono 中 Orbitron 已用於本批 Y2K 和先前 Cyberpunk，改用 Chakra Petch + Share Tech Mono，做成天穹防禦系統監控主控台）。全數繁體中文文案，中文字元皆保留 Noto Sans/Serif TC 作為 fallback。

### 2026-08-20（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（連線逾時，HTTP 000，連續第 4 次），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- ⚠️ 本輪 GH_TOKEN 直連 GitHub API（publish.py）被環境閘道擋下（403「GitHub access is not enabled for this session」），改用 GitHub App／MCP 工具（push_files）發布，已確認 commit 成功。
- ⚠️ 本輪 Telegram 通知（步驟 8）也被環境網路政策擋下（api.telegram.org CONNECT tunnel failed, 403），與 Firebase 同一機制擋下。畫廉已正常生成並發布到 GitHub，只是這次沒有 Telegram 訊息推播，請直接看連結：https://raw.githack.com/weiwei0607/ui-daily/master/reviews/2026-08-20/index.html
- 本批風格（避開近 3 天用過的 #19/#56/#06/#57/#53/#33/#38/#14/#27/#41/#30/#48/#09/#54/#26/#36/#42/#45/#03/#50/#31，並刻意避免與近期重複的字體組合）：Brutalism #04（延續她喜歡「字體對得上設計」的方向，粗野展示字改用 Anton + Space Mono，避免和 #38/#54 的 Archivo Black+Space Grotesk 重複，做成街頭系咖啡烘豆所）、Skeuomorphism #13（全新族群，質感/仿真風不套用「圓體」也不套「報紙體」規則——因其本質是仿實體材質而非圓潤或編輯敘事，改用 Roboto Slab + Nunito Sans 做出木紋皮革的溫暖手感，做成類比錄音室混音控台）、Inclusive Design #17（全新族群，依配方使用 Atkinson Hyperlegible 這款專為無障礙設計的可讀字體，避免 Inter，做成長者友善居家服務預約平台）、Heatmap & Density Dashboard #29（BI 儀表板全新類型，避免用 Inter/JetBrains Mono 撞前幾輪的 Sora/Manrope/IBM Plex，改用全新的 Outfit + JetBrains Mono 組合，做成機房溫控與流量密度監控台）、Dimensional Layering #46（全新族群，中性層次風改用 Hanken Grotesk 避免與 #53 的 Plus Jakarta Sans 重複，做成動態設計師作品集）、Exaggerated Minimalism #47（配方建議 Space Grotesk 已在前幾輪重複出現多次，改用更符合「巨型展示字」精神的 Big Shoulders Display + Archivo，做成極簡眼鏡新品官網）。全數繁體中文文案，中文字元皆保留 Noto Sans/Serif TC 作為 fallback。

### 2026-08-19（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（CONNECT 403，連續第 3 次），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- ⚠️ 本輪 Telegram 通知（步驟 8）也被環境網路政策擋下（api.telegram.org CONNECT 403，gateway policy denial），與 Firebase 同一機制擋下，非帳號或 bot token 問題。畫廉已正常生成並發布到 GitHub，只是這次沒有 Telegram 訊息推播，請直接看連結：https://raw.githack.com/weiwei0607/ui-daily/master/reviews/2026-08-19/index.html
- 本批風格（避開近 3 天用過的 #38/#14/#27/#41/#30/#48/#09/#54/#26/#36/#42/#45/#03/#50/#31，並刻意避免與近期重複的字體組合）：Soft UI Evolution #19（延續「圓潤風配圓體」偏好，改用全新組合 Baloo 2 + Varela Round，做成好眠睡眠 App）、E-Ink / Paper #56（延續「報紙體」偏好，Noto Serif TC + Space Mono，做成讀墨深度閱讀日報，全新族群）、Vibrant Block #06（高飽和色塊風，換掉配方預設的 Space Grotesk，改用 Unbounded + DM Sans 避免與 #38/#54 重複，做成音樂節售票頁）、Gen Z Chaos #57（配方建議的 Clash Display 非 Google Fonts 可靠取得，改用同樣有個性的 Bricolage Grotesque + IBM Plex Mono，做成潮玩交易所）、Bento Grids #53（避免用 Inter，改用 Plus Jakarta Sans，做成產品設計師作品集）、Comparative Dashboard #33（BI 儀表板全新類型，避免用 Inter/JetBrains Mono 撞前幾輪，改用 Sora + Roboto Mono，做成廣告成效比較看板）。全數繁體中文文案，中文字元皆保留 Noto Sans/Serif TC 作為 fallback。

### 2026-08-18（6 個，#01–06）
- ⚠️ Firebase ❤️ 讀取本輪仍被環境網路政策擋下（CONNECT 403），無法讀取上一批按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- 本批風格（避開近 3 天用過的 #09/#26/#36/#42/#45/#43/#54/#56）：Neubrutalism #38（她先前按讚過但因簡體字被清掉，這次用繁體重做，Archivo Black + Space Grotesk）、Liquid Glass #14（延續「玻璃風配圓體」教訓，改用 Zen Maru Gothic + Quicksand，不再用 Inter）、Storytelling #27（延續「敘事配報紙體」，Newsreader + Noto Serif TC）、Cyberpunk #41（全新族群，Orbitron + Share Tech Mono，避免用 Inter）、Executive Summary Dashboard #30（儀表板但換用 Manrope + JetBrains Mono，不是預設 Inter）、Kinetic Typography #48（全新族群，Bebas Neue + Work Sans 展示字）。中文字元一律用字型堆疊 fallback 到 Noto Sans/Serif TC，確保英文展示字與中文都到位。全數繁體中文文案。

### 2026-08-17 第 2 批（6 個，#07–12）
- ⚠️ Firebase ❤️ 讀取仍被環境網路政策擋下（`b-battle-580b5-default-rtdb.firebaseio.com` CONNECT 403），本輪無法讀取第 1 批的按讚結果，沿用「已確認偏好」規則生成，等下次能連線時再回補。
- 本批風格：Claymorphism #09（圓體 Baloo 2，延續她要「圓潤風配圓體」的偏好）、Neubrutalism v2 #54（延續她喜歡的 #38 方向，配色更協調）、Trust & Authority #26（延續她要「報紙體」的偏好，改用 Playfair+Noto Serif TC 但換一種結構，避免和 #50 重複）、Financial Dashboard #36（避免整頁 Inter，改用 IBM Plex Sans + JetBrains Mono）、Organic Biophilic #42（Cormorant Garamond + Nunito，全新族群）、Vaporwave #45（Press Start 2P + VT323，全新族群）。全數繁體中文文案。

### 2026-08-17 第 1 批（4 個）
- ❌ Glassmorphism #03：字體不好看 → 她要「圓一點」。歸納：玻璃風配圓體。
- ❌ Swiss Modernism #50：字體不好看 → 她要「報紙體」。歸納：Swiss/編輯風配襯線報紙體。
- ❌ Real-Time Monitoring #31：「太有你（AI）的風格了」。歸納：避免通用 AI 樣板感。
- ❤️ Neubrutalism #38：「只有這個設計字體對得上」。歸納：字體與設計一致＝她認可的方向。
- 🔴 全部：都是簡體字 → 一律改繁體。
