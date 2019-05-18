import requests
import json
import base64


class eleme(object):

    def __init__(self):
        self.code_img = "https://h5.ele.me/restapi/eus/v3/captchas"
        self.get_logincode = "https://h5.ele.me/restapi/eus/login/mobile_send_code"
        self.get_reallogin = "https://h5.ele.me/restapi/eus/login/login_by_mobile"
        self.loginheaders = {
            
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "accept":"*/*",
            "content-type":"application/json; charset=utf-8",
            "content-length":"113",
            "origin":"https://h5.ele.me",
            "referer":"https://h5.ele.me/login/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
     
        }

    def get_code(self):
        data = {
            "captcha_hash":"",
            "captcha_value":"",
            "mobile":"18028787283",
            "scf":"ms",

        }
        self.se = requests.Session()
        #初次请求 拿到cookies，返回验证码提示
        res = self.se.post(self.get_logincode,headers=self.loginheaders,data=json.dumps(data))
        print(res.text)

        # 请求验证码地址，获取code ，此时会返回captcha_hash值
        img_data={
            "captcha_str":"18028787283"
        }
        res = self.se.post(self.code_img,headers=self.loginheaders,data=json.dumps(img_data))
        res_json = json.loads(res.text)
        captcha_hash = res_json["captcha_hash"]
        b64_code = res_json["captcha_image"].split(",")[1]
        img_type = res_json["captcha_image"].split(",")[0].split(";")[0].split("/")[-1]
        with open("1."+img_type,"wb") as f:
            f.write(base64.b64decode(b64_code + (4-len(b64_code) %4) *"="))
        code_input = input("code")

        # 获得验证码后再次请求上一个url get_logincode 地址，验证正确后得到valid_token
        data["captcha_value"] = code_input
        data["captcha_hash"] = captcha_hash
        res = self.se.post(self.get_logincode,headers=self.loginheaders,data=json.dumps(data))
        print("获取validate_token",res.text)
        token = json.loads(res.text)["validate_token"]

        # login 登录需要 mobile scf validate_code validate_token 上一步最后一个token已经全部得到，post 请求login
        login_data = {
            "mobile":"18028787283",
            "scf":"ms",
            "validate_token":token,
            "validate_code":input("手机验证码") ,

        }
        res = self.se.post(self.get_reallogin,headers=self.loginheaders,data=json.dumps(login_data))
        print(res.text)
        headers_afterlogin={
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'referer':'https://h5.ele.me/msite/food/',
            'user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Mobile Safari/537.36',
            'x-shard':'loc=114.10957,22.54362'
        }
        url='https://h5.ele.me/restapi/shopping/v3/restaurants?latitude='+str(39.99287)+'&longitude='+str(116.31025)+'&keyword=&offset='+str(1)+'&limit=8&extras[]=activities&extras[]=tags&terminal=h5&rank_id=10fe946cb6b440ad8c386796b921a79b&brand_ids[]=&restaurant_category_ids[]=209&restaurant_category_ids[]=212&restaurant_category_ids[]=214&restaurant_category_ids[]=266&restaurant_category_ids[]=267&restaurant_category_ids[]=268&restaurant_category_ids[]=269&restaurant_category_ids[]=354&restaurant_category_ids[]=362&restaurant_category_ids[]=370&restaurant_category_ids[]=378&restaurant_category_ids[]=386&restaurant_category_ids[]=394&restaurant_category_ids[]=402&restaurant_category_ids[]=410&restaurant_category_ids[]=418&restaurant_category_ids[]=426&restaurant_category_ids[]=434&restaurant_category_ids[]=442&restaurant_category_ids[]=450&restaurant_category_ids[]=458&restaurant_category_ids[]=466&restaurant_category_ids[]=474&restaurant_category_ids[]=482&restaurant_category_ids[]=490&restaurant_category_ids[]=498&restaurant_category_ids[]=746&restaurant_category_ids[]=754&restaurant_category_ids[]=762&restaurant_category_ids[]=770&restaurant_category_ids[]=778&restaurant_category_ids[]=786&restaurant_category_ids[]=794&restaurant_category_ids[]=802&restaurant_category_ids[]=810&restaurant_category_ids[]=818&restaurant_category_ids[]=826&restaurant_category_ids[]=834&restaurant_category_ids[]=842&restaurant_category_ids[]=850&restaurant_category_ids[]=858&restaurant_category_ids[]=866&restaurant_category_ids[]=874&restaurant_category_ids[]=882&restaurant_category_ids[]=890&restaurant_category_ids[]=898&restaurant_category_ids[]=906&restaurant_category_ids[]=914&restaurant_category_ids[]=922&restaurant_category_ids[]=930&restaurant_category_ids[]=938&restaurant_category_ids[]=946&restaurant_category_ids[]=954&restaurant_category_ids[]=221&restaurant_category_ids[]=222&restaurant_category_ids[]=223&restaurant_category_ids[]=224&restaurant_category_ids[]=225&restaurant_category_ids[]=226&restaurant_category_ids[]=227&restaurant_category_ids[]=228&restaurant_category_ids[]=232&restaurant_category_ids[]=263&restaurant_category_ids[]=506&restaurant_category_ids[]=514&restaurant_category_ids[]=522&restaurant_category_ids[]=530&restaurant_category_ids[]=538&restaurant_category_ids[]=546&restaurant_category_ids[]=554&restaurant_category_ids[]=562&restaurant_category_ids[]=570&restaurant_category_ids[]=578&restaurant_category_ids[]=586&restaurant_category_ids[]=594&restaurant_category_ids[]=602&restaurant_category_ids[]=610&restaurant_category_ids[]=618&restaurant_category_ids[]=626&restaurant_category_ids[]=634&restaurant_category_ids[]=642&restaurant_category_ids[]=650&restaurant_category_ids[]=658&restaurant_category_ids[]=666&restaurant_category_ids[]=674&restaurant_category_ids[]=682&restaurant_category_ids[]=690&restaurant_category_ids[]=698&restaurant_category_ids[]=706&restaurant_category_ids[]=218&restaurant_category_ids[]=234&restaurant_category_ids[]=236&restaurant_category_ids[]=962&restaurant_category_ids[]=970&restaurant_category_ids[]=978&restaurant_category_ids[]=986&restaurant_category_ids[]=994&restaurant_category_ids[]=1002&restaurant_category_ids[]=1010&restaurant_category_ids[]=1018&restaurant_category_ids[]=1026&restaurant_category_ids[]=1034&restaurant_category_ids[]=240&restaurant_category_ids[]=241&restaurant_category_ids[]=242&restaurant_category_ids[]=249&restaurant_category_ids[]=250&restaurant_category_ids[]=714&restaurant_category_ids[]=722&restaurant_category_ids[]=730&restaurant_category_ids[]=738&restaurant_category_ids[]=346&restaurant_category_ids[]=1042&restaurant_category_ids[]=1050&restaurant_category_ids[]=1058&restaurant_category_ids[]=1066&restaurant_category_ids[]=1074&restaurant_category_ids[]=1082&restaurant_category_ids[]=1090&restaurant_category_ids[]=1098&restaurant_category_ids[]=1106&restaurant_category_ids[]=1114&restaurant_category_ids[]=1122&restaurant_category_ids[]=1130&restaurant_category_ids[]=1138&restaurant_category_ids[]=1146&restaurant_category_ids[]=1154&restaurant_category_ids[]=1162&restaurant_category_ids[]=1170&restaurant_category_ids[]=1178&restaurant_category_ids[]=1186&restaurant_category_ids[]=1194&restaurant_category_ids[]=1202&restaurant_category_ids[]=1210&restaurant_category_ids[]=1218&restaurant_category_ids[]=1226&restaurant_category_ids[]=1234&restaurant_category_ids[]=1250&restaurant_category_ids[]=1258&restaurant_category_ids[]=1266&restaurant_category_ids[]=1274&restaurant_category_ids[]=1282&restaurant_category_ids[]=1290&restaurant_category_ids[]=1298&restaurant_category_ids[]=1306&restaurant_category_ids[]=1314&restaurant_category_ids[]=1322&restaurant_category_ids[]=1330&restaurant_category_ids[]=1338&restaurant_category_ids[]=1346&restaurant_category_ids[]=1354&restaurant_category_ids[]=1362&order_by=12' 
        res = self.se.get(url,headers=headers_afterlogin)
        print(res.text)
        return res

    def run(self):
        res = self.get_code()

elm = eleme()
elm.run()
