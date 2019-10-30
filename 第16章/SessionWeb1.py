import web
web.config.debug=False
urls = (
    "/", "countUsers",
    "/reset", "resetSession"
)
db = web.database(dbn='sqlite', db='SessionDB')
app=web.application(urls,locals())
store = web.session.DBStore(db,'sessions')
session = web.session.Session(app,store,{'count': 0})
web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 86400, #24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'


class countUsers:
    def GET(self):
        session.count+= 1
        print(session.count)
        return str(session.count)
        
class resetSession:
    def GET(self):
        session.kill()
        return ""

if __name__ == "__main__":
    app.run()
    
