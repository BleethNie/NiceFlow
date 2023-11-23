# coding: utf-8
# import os
from ftplib import FTP


def ftp_connect(host, port, username, password):
    """
    可以实现上传 下载单个文件
    """
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    # ftp.set_pasv(False)
    return ftp


def download_file(ftp, remote_path, local_path):
    """
    从ftp服务器下载文件

    remote_path:远程路径
    local_path：本地路径
    """

    buf_size = 1024
    fp = open(local_path, 'wb')
    ftp.retrbinary('RETR ' + remote_path, fp.write, buf_size)
    ftp.set_debuglevel(0)
    fp.close()


def upload_file(ftp, remote_path, local_path):
    """
    从本地上传文件到ftp
    remote_path:远程路径
    local_path：本地路径

    """
    buf_size = 1024
    fp = open(local_path, 'rb')

    ftp.storbinary('STOR ' + remote_path, fp, buf_size)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    host = '192.168.1.88'  # IP
    port = 21  # 端口
    username = 'mobaxterm'  # 用户名
    password = 'mobaxterm'  # 密码
    ftp = ftp_connect(host, port, username, password)
    # upload_file(ftp, "/2.json", "C:/Users/xiaow/Desktop/11/11.json")
    download_file(ftp, "11.json", "C:/Users/xiaow/Desktop/11/33.json")
    ftp.quit()
