from common import dbClient


def get_post_detail(post_id):
    sql = 'SELECT * FROM POSTS WHERE PostId = ?'
    return dbClient.execute_query(sql, [post_id])


def add_post(post):
    sql = 'INSERT INTO POSTS(PostId,Title,Body,PostDate,UserId) VALUES (?,?,?,?)'
    return dbClient.execute_no_query(sql, [post.PostId, post.Title, post.Body, post.UserId])


def edit_post(post):
    sql = 'UPDATE POSTS SET Title = ? ,Body =? WHERE PostId = ?'
    return dbClient.execute_no_query(sql, [post.Title, post.Body, post.PostId])
