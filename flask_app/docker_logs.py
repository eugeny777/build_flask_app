import sys
import docker
from flask import Flask, render_template

client = docker.DockerClient(base_url='193.193.192.25:2376')

def show_all_container (): 
    list_of_container = []
    for container in client.containers.list():
        list_of_container.append(container.name)
    return list_of_container

def show_logs(name):
    for container in client.containers.list():
      if container.name == name:
         return container.logs() 

app = Flask(__name__)
@app.route("/")
def index():
    res=show_all_container()
    return render_template('index.html', list_containers=res)

@app.route("/logs/<name>")
def show_log(name):
    return '<p>{0}</p>'.format(show_logs(name))  

if __name__ == '__main__':
   app.run(debug=True)
