from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import verify as verify
import threading
import requests

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
	#listen to post
 	def do_POST(self):
 		try:
	 		content_length = int(self.headers['Content-Length'])
	 		post_data = self.rfile.read(content_length)
	 		image = json.loads(post_data.decode())["image"]
	 		isBase64 = verify.isBase64(image)
	 		isTest = verify.isTest(image)
	 		print(("\nverify: request from demo proxy %s " % ("is" if isBase64 else "is not(!)") + "base64 encoded"))
	 		print(("verify: encoded value from demo proxy %s " % ("is" if isTest["result"] else "is not(!)") + " test" + ("" if isTest["result"] else ("it is " + isTest["string"]))  ))

	 	except:
	 		print("oops")
 
def run(): 
  server_address = ('127.0.0.1', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print("Server running at http://" + str(server_address[0]) + ":" + str(server_address[1]))
  thread = threading.Thread(target=httpd.serve_forever)
  thread.daemon = True 
  thread.start()
 
run()

# Send request 
requests.post("http://127.0.0.1:8081/api/image", data=json.dumps({"image":"test"}))
