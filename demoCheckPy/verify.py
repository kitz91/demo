import base64

def isBase64(image):
	try:
		if base64.b64encode(base64.b64decode(str.encode(image))).decode() == image:
			return True
		return False
	except:
		return "ladida"

def isTest(image):
	try:
		return {"result":(base64.b64decode(str.encode(image)) == image), "string":str((base64.b64decode(image)).decode("utf-8"))}
	except:
		pass
	return False
