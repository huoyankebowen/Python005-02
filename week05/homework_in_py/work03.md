作业三：请用自己的语言描述如下问题：
====
1. 在你目前的工作场景中，哪个业务适合使用 rabbitmq？ 引入 rabbitmq 主要解决什么问题?（非相关工作可以以设计淘宝购物和结账功能为例来描述）
    * 上游與下游系統，結帳和購物功能間的聯繫。消費者購買多件商品時使用購物車，即是緩存的功能;結帳清空購物車時，採集數據，存到數據庫，其過程中做為緩存。
2. 如何避免消息重复投递或重复消费？
    * 判斷資料是否存在，再去創建，以避免重複沖值、扣款。尹老師的例子，寫入訊息前，先做加減，例如: 將金額從100扣10為90，系統先判斷資料是否為90，若已經是90則不再做加減。
    * 利用數據庫的唯一約束。

3. 交换机 fanout、direct、topic 有什么区别？
    * fanout: 不處理routing_key。只需將queue連到交換機上。一個傳送到交換機的訊息都會被轉發到與該交換機繫結的所有佇列上。每臺子網內的主機都獲得了一份複製的訊息，轉發訊息也最快的。
    * direct: 處理routing_key。需要將一個queue連到交換機上，要求該訊息與一個特定的路由鍵完全匹配。
    * topic: 將routing_key和某模式進行匹配。此時queue需要連到一個模式上。符號“#”匹配一個或多個詞，符號“*”匹配不多不少一個詞。因此“audit.#”能夠匹配到“audit.irs.corporate”，但是“audit.*” 只會匹配到“audit.irs”
4. 架构中引入消息队列是否利大于弊？你认为消息队列有哪些缺点？
    * 系統的可用性降低：很多服務都依賴於MQ，一旦MQ故障，系統崩潰。
    * 系統變的複雜，序列考慮問題變多：發送消息重複，多了，亂序，丟掉。
    * 一致性問題：系統A給BCD發送，只有都成功才返回成功，結果BC成功，但是D失敗，但是返回頁面結果是成功。
