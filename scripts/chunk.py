#!/usr/bin/python

class chunk:
    def __init__(self):
        self.data = []
        self.tags = {}

    def append(self, x):
        self.data.append(x)

    def get(self):
        return self.data

    def addTag (self, tag):
        if(not tag in self.tags):
             self.tags[tag]=0
        self.tags[tag]+=1

    def getTags(self):
        return self.tags

    def serialize(self):
       data="<chunk>\n"
       data+="<data>\n"
       for ln in self.get():
           data+=ln
           data+= "\n"
       data+="</data>\n"
       data+="<tags>"
       data+=str(self.tags.keys())
       data+="</tags>\n"
       data+="<size>"
       data+=str(len(self.get()))
       data+="</size>\n"
       data+="</chunk>\n"
       return data


