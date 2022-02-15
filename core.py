# importing library
import requests

def banner():
	print(
"""
 _           _                             
| |_ ___ _ _| |_ ___ ___ ___ ___ _ _ _____ 
| . |  _| | |  _| -_|___| -_|   | | |     |
|___|_| |___|_| |___|   |___|_|_|___|_|_|_|
Dagimal - 2022
"""
)

# function for scanning subdomains
def domain_scanner(domain_name,sub_domain):
	print('-----------Scanner Started-----------')
	
	# loop
	for subdomain in sub_domain:
		url = f"https://{subdomain}.{domain_name}"
		
		try:
		
			# get request to the url
			requests.get(url)
			print(f'[+] {url}')
			
		# if url is invalid then pass it
		except requests.ConnectionError:
			pass
	print('\n')
	print('----Scanning Finished----')
	print('-----Scanner Stopped-----')
