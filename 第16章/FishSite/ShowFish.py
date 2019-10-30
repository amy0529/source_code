import web
import sqlite3
render=web.template.render('templates\\') 
urls = (
    '/', 'index'
)
    
class index:
    def GET(self):
        gets=[]
        conn=sqlite3.connect('First.db')
        cur=conn.cursor()
        cur.execute("select * from T_fish")
        for get in cur.fetchall():
            gets.append(get)
        conn.close()
        return render.Show_temp(gets)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
