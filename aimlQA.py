import json
import aiml

print("請輸入訂餐內容: \r\n"
      "範例: 排骨便當{數字}個 {姓名} \r\n"
      "雞腿便當 3 個 Jason \r\n"
      "排骨便當 2 個 Jason \r\n")

print("結帳 \r\n"
      "{姓名} {訂餐內容} 共計{總金額}元 \r\n")

kernal = aiml.Kernel()
kernal.learn('order-AIML.xml')

meals = {'chicken': 80, 'pork': 90}
username = ''
kernal.respond("初始化")
while True:
    try:
        req = input("請輸入訂餐內容")

        if req == "結帳":
            res = kernal.respond("當前訂單")
            resJson = json.loads(str(res))
            pork_num = resJson["pork"]
            chicken_num = resJson["chicken"]
            total = (meals["pork"] * pork_num) + (meals["pork"] * chicken_num)
            text = "總金額為"
            if resJson["pork"] > 0:
                text += "排骨便當" + str(meals["pork"]) + "元 共" + str(resJson["pork"]) + "個 "

            if resJson["chicken"] > 0:
                text += "雞腿便當" + str(meals["chicken"]) + "元" + str(resJson["chicken"]) + "個"

            text += "共" + str(total)
            print(text)

        else:
            kernal.respond(req)
            res = kernal.respond("當前訂單")
            resJson = json.loads(str(res))

            text = resJson["username"] + "訂購了 "
            if resJson["pork"] > 0:
                text += "排骨便當" + str(resJson["pork"]) + "個 "

            if resJson["chicken"] > 0:
                text += "雞腿便當" + str(resJson["chicken"]) + "個"

            print(text)
    except:
        print("something wrong!")
