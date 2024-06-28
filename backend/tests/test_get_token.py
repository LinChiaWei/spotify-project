import unittest
from models.get_token import Login

class TestGetToken(unittest.TestCase):
    def setUp(self):
        # 如果有需要在測試前做準備的，可以在這裡設定
        pass
    
    def tearDown(self):
        # 如果有需要在測試後做清理的，可以在這裡設定
        pass
    
    def test_get_token(self):
        # 測試你的 get_token 函式
        # 假設你的函式會返回某個格式的 JSON 或其他數據
        expected_response = {...}  # 假設這是你預期的回應
        
        # 假設你有需要的參數，可以在這裡準備
        client_id = 'a5f4717d6cbe43fea2cc354da04490b6'
        redirect_uri = 'http://localhost:8888/callback/'
        client_secret = '4eaba7b3f548455dae6a2ac83d8e39e1'
        scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']
        response_type = 'code'

        # 呼叫你的函式取得實際回應
        l = Login()
        actual_response = l.login()
        # 比較預期回應和實際回應

        
if __name__ == '__main__':
    unittest.main()