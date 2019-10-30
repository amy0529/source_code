import web

urls = (
	'/','Index',
	'/login','Login',
	'/logout','Logout',
)

render = web.template.render("login\\")
firstSet= (
	('admin','123'),
)

web.config.debug = False
app=web.application(urls, locals())

cookie1=web.setcookie(name='test',value='False',expires=3600)
#session=web.session.Session(app, web.session.DiskStore('sessions'))

class Index:
    def GET(self):
        logOK=cookie1.get('value')
        if not logOK:
            return '<h1>登录成功!!!</h1><a href="/logout">Logout</a>'.encode("gb2312")
        else:
            raise web.seeother("/login") 
            
	

class Login:
	def GET(self):
		return render.login()
	def POST(self):
		i=web.input()
		username=i.get('username')
		passwd=i.get('passwd')
		if (username,passwd) in firstSet:
		    cookie1.value = True
		    cookie1['username']=username
		    cookie1['passwd']=passwd
		   
		    raise web.seeother('/')
		else:
		    return '<h1>登录出错!!!</h1></br><a href="/login">Login</a>'.encode("gb2312")

class Logout:
	def GET(self):
		cookie1.value= False
		raise web.seeother("/login")

if __name__ == '__main__':
	app.run()


