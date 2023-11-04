# -*- coding:utf-8 -*-

import base64
import hashlib
from Crypto.Cipher import AES
from loguru import logger


class EncryptData:
    def __init__(self, key):
        self.key = self.md5_16(key).encode("utf-8")  # 初始化密钥
        self.length = 16  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        self.un_pad = lambda date: date[0:-ord(date[-1])]  # 截断函数，去除填充的字符

    def md5_16(self, text: str):
        md5_str = hashlib.md5(text.encode()).hexdigest()
        return md5_str[8:24]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        en_text = text + (chr(add) * add)
        return en_text

    def encrypt(self, encrData) -> str:  # 加密函数
        a = self.pad(encrData)
        res = self.aes.encrypt(a.encode("utf-8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData) -> str:  # 解密函数
        res = base64.decodebytes(decrData.encode("utf-8"))
        try:
            msg = self.aes.decrypt(res).decode("utf-8")
        except UnicodeDecodeError as e:
            logger.error('解密失败,请检查密码是否正确')
            return None
        return self.un_pad(msg)


if __name__ == '__main__':
    aes_key = "9999999999999999"
    # aes_text = "happy_new_years_2022"
    eg = EncryptData(aes_key.encode("utf-8"))
    # encrypt_data = eg.encrypt(aes_text)
    print("明文数据数据:", eg.decrypt("q9y4jgO+nA9X3KoxnGi/1N3ebB0svaIsIESeHKA2oyA="))
    # print("加密后数据:", encrypt_data)
