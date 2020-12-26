import cherrypy
import os

class kwwwis(object):
    @cherrypy.expose
    def index(self):
        file = open("./public/kwwwis.html", 'r')
        text = file.read()
        return (text)




if __name__ == '__main__':
    print(os.getcwd())
    #os.chdir("/home/pi/Documents/")
    print(os.getcwd())
    conf = os.path.join(os.path.dirname(__file__),'kwwwis.conf')
    cherrypy.quickstart(kwwwis(),config=conf)