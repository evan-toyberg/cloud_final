import pymysql
conn = pymysql.connect(
        host= 'blog-database.cok7rmmo3rxv.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'password',
        db = 'blog',

       	)

#Table Creation
#cursor=conn.cursor()
#create_table="""
#create table Posts (name varchar(200),email varchar(200),title varchar(20),comment varchar(200) )
#"""
#cursor.execute(create_table)


def insert_details(name,email,title,comment):
    cur=conn.cursor()
    cur.execute("INSERT INTO Posts (name,email,title,comment) VALUES (%s,%s,%s,%s)", (name,email,title,comment))
    conn.commit()

def get_posts():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Posts")
    posts = cur.fetchall()
    return posts
