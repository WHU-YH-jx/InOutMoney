from app.models.User import User
from app.utils.DBHelper import MyHelper
import json


class UserDao:
    @classmethod
    def to_dict(cls, data):
        result = []
        for row in data:
            res = {}
            res['account'] = row[0]
            res['password'] = row[1]
            res['companyId'] = row[2]
            res['ID'] = row[3]
            res['position'] = row[4]
            res['openid'] = row[5]
            result.append(res)
        return result

    def query_all(self):
        connection = MyHelper()
        result = connection.executeQuery('select * from User')
        return result

    def add(self, account, password, companyid):
        connection = MyHelper()
        row = connection.executeUpdate('insert into User(account, \
        password, CompanyId) \
         values (%s,%s,%s)', [account, password, companyid])
        return row

    def query_by_account(self, account):
        helper = MyHelper()
        return helper.executeQuery("select * from User where account=%s", [account])

    def query_check_login(self, account, password):
        helper = MyHelper()
        return helper.executeQuery("select * from User where account=%s and password=%s ",
                                   [account, password])

    def query_by_openid_account(self, account, openid):
        _param = []
        _sql = "select * from User where 1=1"
        if account:
            _sql += " and account = %s"
            _param.append(account)
        if openid:
            _sql += " and openid = %s"
            _param.append(openid)
        helper = MyHelper()
        return helper.executeQuery(_sql, _param)

    def bind_wx(self, account, openid):
        helper = MyHelper()
        return helper.executeUpdate("update User set openid = %s where account = %s",
                                    [openid, account])
