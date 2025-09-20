def  domain_name(url):
     domain = url.replace("http://","").replace("https://","").replace("www.","")
     domain_name = domain.split(".")
     return domain_name[0]
   
   
print(domain_name("https://njp9gh6lk1s1dhd9gs.pro/"))