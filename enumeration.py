import core

# start
if __name__ == '__main__':
	core.banner()
	# input domain name
	dom_name = input("Domain Name:")
	print('\n')

	# open subdomain text file
	with open('subdomain.txt','r') as file:
	
		# read the file
		name = file.read()

		# splitted strings
		sub_dom = name.splitlines()
		
	# call the function
	core.domain_scanner(dom_name,sub_dom)

