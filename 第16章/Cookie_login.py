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
session=web.session.Session(app, web.session.DiskStore('sessions'))

class Index:
	def GET(self):
		if session.get('logged_in',False):
		    return '<h1>登录成功!!!</h1><a href="/logout">Logout</a>'.encode("gb2312")
		raise web.seeother('/login')

class Login:
	def GET(self):
		return render.login()
	def POST(self):
		i=web.input()
		username=i.get('username')
		passwd=i.get('passwd')
		if (username,passwd) in firstSet:
		    session.logged_in = True
		    web.setcookie('test', '', 3600)
		    
		    raise web.seeother('/')
		else:
		    return '<h1>登录出错!!!</h1></br><a href="/login">Login</a>'.encode("gb2312")

class Logout:
	def GET(self):
		session.logged_in = False
		raise web.seeother("/login")

if __name__ == '__main__':
	app.run()


