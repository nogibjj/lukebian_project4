# lukebian_project4

### This is the repo for individual project4 IDS706. 
### In this project, I built a NBA Players FastAPI and show the five members in celtics teams. After build the API on github, I deploy it on the AWS using lambda function, so that, you can access the heep endnote using the url: https://gk6ucblzl5u2wu4dio3mkc3ole0gsnwv.lambda-url.us-west-2.on.aws/ 


### We'll need to modify the API so that it has a Lambda handler. Use Mangum:
```
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
```

### We'll also need to install the dependencies into a local directory so we can zip it up.
```
pip install -t lib -r requirements.txt
```

### We now need to zip it up.
```
(cd lib; zip ../lambda_function.zip -r .)
```

### Now add our FastAPI file and the JSON file.
```
zip lambda_function.zip -u main.py
zip lambda_function.zip -u players.json
```
