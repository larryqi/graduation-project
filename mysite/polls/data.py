import requests
import re

def get_data():
	URL = 'http://localhost:80/auth/login/'
	client = requests.session()

	# Retrieve the CSRF token first
	client.get(URL)  # sets cookie
	csrftoken = client.cookies['csrftoken']

	login_data = dict(username='admin', password='password', csrfmiddlewaretoken=csrftoken, next='/admin/instances/',region="http://127.0.0.1:5000/v2.0")
	r = client.post(URL, data=login_data, headers=dict(Referer=URL))
	content = r.text.encode("utf-8")
	name =  re.findall(r'data-display="(.+?)"',content)
	#print name
	object_id = re.findall(r'data-object-id="(.+?)"',content)
	#print object_id
	#flavor = re.findall(r'data-original-title.+?>(.+?)<',content)
	#print flavor
	others = re.findall(r'sortable normal_column">(.+?)</td>',content)
	other = []
	project = []
	ip = []
	for i in range(len(object_id)):
		other.append(others[i*len(others)/len(object_id):(i+1)*len(others)/len(object_id)])
	for i in range(len(other)):
		project.append(other[i][0])
		ip.append(other[i][2].strip('</li></ul>'))

	#print project
	#print ip

	next_url = []
	for i in object_id:
		next_url.append('/admin/instances/'+i+'/detail?tab=instance_details__console')
	vnc = []
	for url in next_url:
		client = requests.session()
		client.get(URL)
		csrftoken = client.cookies['csrftoken']
		login2_data = dict(username='admin', password='password', csrfmiddlewaretoken=csrftoken, next=url,region="http://127.0.0.1:5000/v2.0")
		s = client.post(URL, data=login2_data, headers=dict(Referer=URL))
		vnc_content=s.text.encode("utf-8")
		vnc_url = re.findall(r'src="(.+?vnc.+?)"',vnc_content)
		vnc.append(vnc_url[0])
	#print vnc
	return object_id,name,project,ip,vnc

if __name__ == '__main__':
	get_data()
