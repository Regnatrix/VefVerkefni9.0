import json
myndir = {"animals": [
		{
			"id":"Cutepig",
			"name":"Cutepig",
			"type":"animal",
			"url":"https://en.wikipedia.org/wiki/Pig#/media/File:Pig_in_a_bucket.jpg",
		},
		{
			"id":"Fatdog",
			"name":"fatdog",
			"type":"fat animal",	"url":"http://www.petguide.com/wp-content/uploads/2015/01/fat-dog.jpg",
		},
    {
			"id":"highcow",
			"name":"highcow",
			"type":"Highland animal",
			"url":"https://www.google.is/search?q=highland+cow&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj-8t_SnpnXAhVHC8AKHcCiDZ4Q_AUICigB&biw=1920&bih=959#imgrc=wi8aqWTd7HRRLM:",
		}
] }
myndir['animals'].append({"id":"Shark","name":"Shark","type":"Water animal","url":"https://scontent-sea1-1.cdninstagram.com/t51.2885-19/s150x150/12357699_178857835801943_1130607807_a.jpg",})
with open("myndir.json","a") as skra:
    json.dump(myndir,skra)

with open("myndir.json","r") as skra:
    gogn = json.load(skra)

print(gogn)