#  coding:utf-8
#哈哈哈,上面一句必须加，不然中文备注会报错
import urllib2
import re
import os
class spider:
    def __init__(self, city):
        self.city=city
        self.url = 'http://'+city+'.lianjia.com/zufang/'
    '''
    def getpage(self,pageindex):
        URL = self.url+'pg'+str(pageindex)+'/'
        request = urllib2.Request(URL)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')
    '''
        #为上面函数添加页面链接报错提示
    def getpage(self, pageindex):
        URL = self.url + 'pg' + str(pageindex) + '/'
        request = urllib2.Request(URL)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            print e.code
            print e.reason
        except urllib2.URLError, e:
            print e.reason
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
        self.mkdir('lianjia'+'/'+self.city)
        filename= 'lianjia'+'/'+self.city+'/'+str(filename)+'.txt'
        f=open(filename, "w+")
        f.write(content.encode('utf-8'))
        f.close()
    def getcontent(self, pageindex):
        response = self.getpage(pageindex)
        pattern = re.compile('<a target="_blank" href="http://'+self.city+'.lianjia.com/zufang/(.*?).html" title="(.*?)">(.*?)</a>', re.S)
        items = re.findall(pattern, response)
        lines=''
        for item in items:
            print item[1]
            lines=lines+item[1]+'\n'
        self.savetxt(lines, pageindex)
    def pagescontent(self,pagefirst, pageend):
        for value in range(pagefirst, pageend):
            self.getcontent(value)
spider = spider('bj')
spider.pagescontent(1, 101)


