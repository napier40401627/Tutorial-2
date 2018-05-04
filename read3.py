import urllib2,json,base64
accesstoken = "EU8H3PSFYXL1UCSHGMTV"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
    institution,
    course
    )
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)
#print json.dumps(data,indent=2)
for c in data:
    if c['Code'] == "NSS" or c['Code'] == "SALARY":
        c = c['Details']
        for d in c:
            if d['Code'] == "Q1" or d['Code'] == "MED" or d['Code'] == "LDMED":
                print(d['Value'])
            else:
                pass
    else:
        pass
    
