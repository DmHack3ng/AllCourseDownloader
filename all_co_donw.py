# coding: utf-8
#Coded By Dm_Hack3ng.py
#Use Python2 

import requests
from BeautifulSoup import BeautifulSoup
import urlparse
import re
import optparse

class Finder():
    def __init__(self):
        self.url="https://google.com"
        self.dm=raw_input("Entrez votre Cours >> ")
        self.method=raw_input("methode de recherche = rapide | lent >> ")
        self.payloads=["intext:","allintitle:","inurl:"]
        self.website=[] 
        self.link_list=[]

    def opener(self):
        with open("result.txt","r") as zeu:
            for site in zeu:
                self.website.append(site)


    def perfect_v2(self,url):
        for wbsite in self.website:
            url="site:'"+wbsite+"' "+self.dm
            print(url+"\n-------------------------------------\n\n") 
            self.post_data(url)
        
    def perfect_url(self,url):
        for payload in self.payloads:
            get_data=payload+"'"+url+" free"+"'" 
            print(get_data+"\n-------------------------------------\n\n")
            self.post_data(get_data) 
        

    
    def show_links(self,page):
        links=re.findall('(?:href=")(.*?)"',page.content)
        for link in links:
            details=["www","http"]
            for word in details:
                if word in link and link not in self.link_list and "google"  not in link and "+" not in link:
                    link=link.replace("/url?q=","")
                    link=link.replace("/search?q=site:%27","") 
                    link=link.split("&")
                    self.link_list.append(link)
                    print("\n"+"Possible Url --->" +link[0]+"\n")
            
            
    def post_data(self,data):
        reponse=requests.get(self.url)
        search=BeautifulSoup(reponse.content)
        all_form=search.findAll("form")
        for form in all_form:
            post_dict={}
            action=form.get("action")
            post_url=urlparse.urljoin(self.url,action)
            input_list=form.findAll("input")
            for input in input_list:
                classe=input.get("class")
                input_value=input.get("value")
                input_name=input.get("name") 
                if classe=="lst tiah":
                    input_value=data
        
                post_dict[input_name]=input_value
        result=requests.get(post_url,params=post_dict)
        self.show_links(result)

    def find_all_course(self):    
        self.opener()
        if self.method=="rapide":
            self.perfect_url(self.dm)
            self.banner()
        elif self.method=="lent":
            self.perfect_v2(self.dm)
            self.banner()

    
    def banner(self):
        print("\n\nCoded By :")
        print("*****************************************************************************************************")
        print("*****************************************************************************************************")                                                                                       
        print("-----     --    --      --   --       --      -------  --   --  --   --      --  --------    ********")
        print("-----     --    --      --   --       --      -------  --  --   --   -- --   --  -           ********")
        print("--   --   -- -- --      -------     --  --    -        --       --   --  --  --  - ------    ********")
        print("--   --   -- -- --      --   --    --------   -------  --  --   --   --    - --  -      -    ********")
        print("-----     --    --      --   --   --      --  -------  --   --  --   --      --  ------ -    ********")
        print("                                                                                             ********")
        print("*****************************************************************************************************")
        print("*****************************************************************************************************")


