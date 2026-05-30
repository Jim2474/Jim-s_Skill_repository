# {MONTH}月账单逐笔明细

> 统计时间：{YEAR}年{MONTH}月1日 - {MONTH}月{LAST_DAY}日
> 说明：已退款项目已全部剔除，投资类交易不计入
> 支付宝小荷包支出单独列出，购物按平台分类，外卖单独标

---

## 一、收入明细

### 生活费/转账收入（小计 ¥{TRANSFER_INCOME_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 备注 |
| ---- | ---: | :--: | -------- | ---- |
{TRANSFER_INCOME_ROWS}

### 其他收入（小计 ¥{OTHER_INCOME_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 备注 |
| ---- | ---: | :--: | -------- | ---- |
{OTHER_INCOME_ROWS}

**收入合计：¥{TOTAL_INCOME}**

---

## 二、支出明细

### 🏠 住宿/房租（小计 ¥{RENT_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{RENT_ROWS}

### 🛵 吃饭-外卖（小计 ¥{TAKEOUT_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{TAKEOUT_ROWS}

### 🍜 吃饭-正餐/食材（小计 ¥{MEAL_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{MEAL_ROWS}

### 🧋 吃饭-奶茶/零食（小计 ¥{SNACK_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{SNACK_ROWS}

### 👔 购物-服饰（小计 ¥{CLOTHING_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{CLOTHING_ROWS}

### 📦 购物-京东（小计 ¥{JD_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{JD_ROWS}

### 📦 购物-拼多多（小计 ¥{PDD_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{PDD_ROWS}

### 📦 购物-淘宝（小计 ¥{TAOBAO_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{TAOBAO_ROWS}

### 💰 支付宝小荷包（小计 ¥{XHB_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{XHB_ROWS}

### 🚗 交通（小计 ¥{TRANSPORT_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{TRANSPORT_ROWS}

### 🎮 娱乐（小计 ¥{ENTERTAINMENT_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{ENTERTAINMENT_ROWS}

### 💊 医疗健康（小计 ¥{MEDICAL_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{MEDICAL_ROWS}

### 📚 学习（小计 ¥{EDUCATION_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{EDUCATION_ROWS}

### 📎 其他支出（小计 ¥{OTHER_EXPENSE_TOTAL}）

| 日期 | 金额 | 来源 | 交易对方 | 商品/说明 | 支付方式 |
| ---- | ---: | :--: | -------- | --------- | -------- |
{OTHER_EXPENSE_ROWS}

**支出合计：¥{TOTAL_EXPENSE}**

---

## 三、汇总

| 项目 | 金额 |
| ---- | ---: |
| 总收入 | ¥{TOTAL_INCOME} |
| 总支出 | ¥{TOTAL_EXPENSE} |
| **净结余** | **¥{NET_BALANCE}** |

---

## 四、支出分类汇总

| 分类 | 金额 | 占比 | 笔数 |
| ---- | ---: | ---: | ---: |
| 吃饭 | ¥{FOOD_TOTAL} | {FOOD_PERCENT}% | {FOOD_COUNT} |
| 购物 | ¥{SHOPPING_TOTAL} | {SHOPPING_PERCENT}% | {SHOPPING_COUNT} |
| 支付宝小荷包 | ¥{XHB_TOTAL} | {XHB_PERCENT}% | {XHB_COUNT} |
| 住宿/房租 | ¥{RENT_TOTAL} | {RENT_PERCENT}% | {RENT_COUNT} |
| 交通 | ¥{TRANSPORT_TOTAL} | {TRANSPORT_PERCENT}% | {TRANSPORT_COUNT} |
| 娱乐 | ¥{ENTERTAINMENT_TOTAL} | {ENTERTAINMENT_PERCENT}% | {ENTERTAINMENT_COUNT} |
| 医疗健康 | ¥{MEDICAL_TOTAL} | {MEDICAL_PERCENT}% | {MEDICAL_COUNT} |
| 学习 | ¥{EDUCATION_TOTAL} | {EDUCATION_PERCENT}% | {EDUCATION_COUNT} |
| 其他支出 | ¥{OTHER_EXPENSE_TOTAL} | {OTHER_EXPENSE_PERCENT}% | {OTHER_EXPENSE_COUNT} |

---

## 五、各平台收支统计

| 平台 | 收入 | 支出 | 笔数 |
| ---- | ---: | ---: | ---: |
| 微信 | ¥{WECHAT_INCOME} | ¥{WECHAT_EXPENSE} | {WECHAT_COUNT} |
| 支付宝 | ¥{ALIPAY_INCOME} | ¥{ALIPAY_EXPENSE} | {ALIPAY_COUNT} |
| 银行 | ¥{BANK_INCOME} | ¥{BANK_EXPENSE} | {BANK_COUNT} |
| 支付宝(花呗) | ¥{HUABEI_INCOME} | ¥{HUABEI_EXPENSE} | {HUABEI_COUNT} |

---

## 六、投资明细（不计入支出）

| 日期 | 金额 | 来源 | 投资类型 | 说明 |
| ---- | ---: | :--: | -------- | ---- |
{INVESTMENT_ROWS}

**投资合计：¥{TOTAL_INVESTMENT}**

---

*报告生成时间：{GENERATED_DATE}*
