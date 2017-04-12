import urllib
import urllib2
import re
import os
class spider:
    def __init__(self):
        self.url = 'http://wh.lianjia.com/zufang/'
    def getpage(self,pageindex):
        URL = self.url+'pg'+str(pageindex)+'/'
        request = urllib2.Request(URL)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')
    def mkdir(self, path):
        path=path.strip()
        isExists= os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False
    def savetxt(self, content, filename):
        self.mkdir('wh')
        filename= 'wh'+'/'+str(filename)+'.txt'
        f=open(filename, "w+")
        f.write(content.encode('utf-8'))
        f.close()
    def getcontent(self, pageindex):
        response = self.getpage(pageindex)
        pattern = re.compile('<a target="_blank" href="http://wh.lianjia.com/zufang/(.*?).html" title="(.*?)">(.*?)</a>', re.S)
        items = re.findall(pattern, response)
        lines=''
        for item in items:
            print item[1]
            lines=lines+item[1]+'\n'
        self.savetxt(lines, pageindex)
    def pagescontent(self,pagefirst, pageend):
        for value in range(pagefirst, pageend):
            self.getcontent(value)
spider = spider()
spider.pagescontent(1, 101)



