from common import dbClient


def get_user_detail(user_id):
    sql = 'SELECT * FROM USERS WHERE UserId = ?'
    return dbClient.execute_query(sql, [user_id])


def user_login(user):
    sql = 'SELECT * FROM USERS WHERE LoginName = ? AND Password =?'
    return dbClient.execute_query(sql, [user.login_name, user.password])


def edit_profile(user):
    sql = 'UPDATE USERS SET UserName = ?, Email=? WHERE UserId = ?'
    return dbClient.execute_no_query(sql, [user.name, user.email, user.user_id])
