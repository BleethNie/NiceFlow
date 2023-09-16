from sqlalchemy import Column, String, text, Index
from sqlalchemy.dialects import mysql

from like.models.base import TimestampMixin, Base

__all__ = [
    'User',
    'user_table',
    'UserAuth',
    'user_auth_table',
]


class User(Base, TimestampMixin):
    """用户实体"""
    __tablename__ = 'la_user'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_row_format': 'Dynamic',
        'mysql_auto_increment': '1',
        'comment': '用户信息表',
    }

    id = Column(mysql.INTEGER(10, unsigned=True), primary_key=True, comment='主键')
    sn = Column(mysql.INTEGER(10, unsigned=True), nullable=False, server_default=text('0'), comment='编号')
    avatar = Column(String(200), nullable=False, server_default='', comment='头像')
    real_name = Column(String(32), nullable=False, server_default='', comment='真实姓名')
    nickname = Column(String(32), nullable=False, server_default='', comment='用户昵称')
    username = Column(String(32), nullable=False, server_default='', comment='用户账号')
    password = Column(String(32), nullable=False, server_default='', comment='用户密码')
    mobile = Column(String(32), nullable=False, server_default='', comment='用户电话')
    salt = Column(String(32), nullable=False, server_default='', comment='加密盐巴')
    sex = Column(mysql.TINYINT(1, unsigned=True), nullable=False, server_default=text('0'),
                 comment='用户性别: [1=男, 2=女]')
    channel = Column(mysql.TINYINT(1, unsigned=True), nullable=False, server_default=text('0'),
                     comment='注册渠道: [1=微信小程序, 2=微信公众号, 3=手机H5, 4=电脑PC, 5=苹果APP, 6=安卓APP]')
    is_disable = Column(mysql.TINYINT(0, unsigned=True), nullable=False, server_default=text('0'),
                        comment='是否禁用: [0=否, 1=是]')
    is_delete = Column(mysql.TINYINT(1, unsigned=True), nullable=False, server_default=text('0'),
                       comment='是否删除: [0=否, 1=是]')
    last_login_ip = Column(String(30), nullable=False, server_default='', comment='最后登录IP')
    last_login_time = Column(mysql.INTEGER(10, unsigned=True), nullable=False, server_default=text('0'),
                             comment='最后登录时间')


class UserAuth(Base):
    """用户授权实体"""
    __tablename__ = 'la_user_auth'
    __table_args__ = (
        Index('openid', 'openid', unique=True),
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_general_ci',
            'mysql_row_format': 'Dynamic',
            'mysql_auto_increment': '1',
            'comment': '用户授权表',
        })

    id = Column(mysql.INTEGER(10, unsigned=True), primary_key=True, comment='主键')
    user_id = Column(mysql.INTEGER(10, unsigned=True), nullable=False, server_default=text('0'), comment='用户ID')
    openid = Column(String(200), unique=True, nullable=False, server_default='', comment='Openid')
    unionid = Column(String(200), nullable=False, server_default='', comment='Unionid')
    client = Column(mysql.TINYINT(1, unsigned=True), nullable=False, server_default=text('1'),
                    comment='客户端类型: [1=微信小程序, 2=微信公众号, 3=手机H5, 4=电脑PC, 5=苹果APP, 6=安卓APP]')
    create_time = Column(mysql.INTEGER(10, unsigned=True), nullable=False, server_default=text('0'), comment='创建时间')
    update_time = Column(mysql.INTEGER(10, unsigned=True), nullable=False, server_default=text('0'), comment='更新时间')


user_table = User.__table__
user_auth_table = UserAuth.__table__
