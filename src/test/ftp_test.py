from NiceFlow.common.ftp_util import MyFTP

if __name__ == "__main__":

    host_address = "localhost"
    username = "mobaxterm"
    password = "111"
    my_ftp = MyFTP(host_address)
    my_ftp.login(username, password)

    # 下载单个文件
    my_ftp.upload_file("C:/Users/xiaow/Desktop/11/AAA.json", "/AAA_.json")

    # 下载目录
    # my_ftp.download_file_tree("G:/ftp_test/", "App/AutoUpload/ouyangpeng/I12/")

    # 上传单个文件
    # my_ftp.upload_file("G:/ftp_test/Release/XTCLauncher.apk", "/App/AutoUpload/ouyangpeng/I12/Release/XTCLauncher.apk")
    # my_ftp.upload_file("G:/ftp_test/Python编程快速上手__让繁琐工作自动化.pdf", "/App/AutoUpload/ouyangpeng/I12/Release/Python编程快速上手__让繁琐工作自动化.pdf")

    # 上传目录
    # my_ftp.upload_file_tree("G:/ftp_test/", "/App/AutoUpload/ouyangpeng/I12/")

    my_ftp.close()