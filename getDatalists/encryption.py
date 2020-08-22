import binascii
import re
from Crypto.Cipher import AES
#pip install pycrypto
 
'''
來源
https://blog.csdn.net/wang_hugh/article/details/83994750
'''

class AESCBC:
    def __init__(self):
        self.key = '12345678901234567890123456789012' #定義key值
        self.mode = AES.MODE_CBC
        self.iv = b'1234567890123456' #定義iv值
        self.bs = 16  # block size
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
 
    def encrypt(self, text):
        generator = AES.new(self.key, self.mode,self.iv)    #这里的key 和IV 一样 ，可以按照自己的值定义
        crypt = generator.encrypt(self.PADDING(text))
        # crypted_str = base64.b64encode(crypt)   #输出Base64
        crypted_str =binascii.b2a_hex(crypt)       #输出Hex
        result = crypted_str.decode()
        return result
 
    def decrypt(self, text):
        generator = AES.new(self.key, self.mode,self.iv)
        text += (len(text) % 4) * '='
        #decrpyt_bytes = base64.b64decode(text)           #输出Base64
        decrpyt_bytes = binascii.a2b_hex(text)           #输出Hex
        meg = generator.decrypt(decrpyt_bytes)
        # 去除解码后的非法字符
        try:
            result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('', meg.decode())
        except Exception:
            result = '解码失败，请重试!'
        return result
 
 
if __name__ == '__main__':
    aes = AESCBC()
 
    #to_encrypt = 'Ilinke255672262019-07-0518810165'
    to_decrypt = '37953a43399e2a0dfd0cb945b90c2310e5e140e32cadaec1e12805728f4e8181d25aea821e57515b23ae22a7887b8395'
 
    #print("\n加密前:{0}\n加密后：{1}\n".format(to_encrypt,aes.encrypt(to_encrypt)))
    print("解密前:{0}\n解密后：{1}".format(to_decrypt,aes.decrypt(to_decrypt)))