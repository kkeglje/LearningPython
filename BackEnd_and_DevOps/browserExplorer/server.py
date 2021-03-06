#! /usr/bin/python3

import os, json
from flask import Flask

app = Flask(__name__)



def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


def createDir(path,name):
    try:
        os.mkdir(os.path.join(path,name))
        return {'code':0,'message':'Dir create successfully','name':name,'path':path}
    except FileExistsError:
        return {'code':-1,'message':'Dir already exists!'}
    except Exception as e:
        print("Unhandled exception in 'createDir' occured!\nException: ", e)
        return {'code':1,'message':'Internal server error!'}



@app.route("/")
def getFiles():
	return json.dumps(path_to_dict('.'),indent=2,sort_keys=True)     



def main():
    print("Starting server...")
    app.secret_key = "testing"
    app.run(host='0.0.0.0',debug=True)


if __name__=='__main__':
    main()

