import requests
import argparse

def parse_additional_params(p):
	params = {}
	if p:
		for param in p.split(','):
			key, value = param.split('=')
			params[key] = value
	return params

def parse_cookies(c):
	cookies={}
	if c:
		for cookie in c.split(','):
			key, value = cookie.split('=')
			cookies[key] = value
	return cookies

def send_requests(url, param, other_params, cookies, wordlist_path):
	with open(wordlist_path, 'r') as file:
		line_no = 0
		for payload in file:
			payload.strip()
			data = {param: payload}
			data.update(other_params)
			response = requests.post(url, data=data, cookies=cookies)
			response_length = len(response.content)
			line_no += 1
			print(f"{line_no}: Payload {payload}Response length: {response_length}\n")

def main():
	parser = argparse.ArgumentParser(description="Automate sending HTTP requests with controllable parameters")
	parser.add_argument('-u', '--url', required=True, help="Target URL")
	parser.add_argument('-p', '--param', required=True, help="Parameter data will be inserted into")
	parser.add_argument('-w', '--wordlist', required=True, help="Path to wordlist file")
	parser.add_argument('-a', '--additional', help="Additional params that can be set statically in following format: param1=value1,param2=value2")
	parser.add_argument('-c', '--cookie', help="Cookies that will be added to request")
	
	args = parser.parse_args()
	
	additional_params = parse_additional_params(args.additional)	
	if args.cookie:
		cookies = parse_cookies(args.cookie) 
	send_requests(args.url, args.param, additional_params, cookies, args.wordlist)

if __name__ == "__main__":
	main()


