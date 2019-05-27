import sys
import docker
#client = docker.DockerClient(base_url='193.193.192.25:2376')

client = docker.DockerClient(base_url='193.193.192.25:2376')
#print (client)

def show_all_container ():
    for container in client.containers.list():
#        value=container    
#        print("type of env",type(container))
#        print ("value=",value)
#        print (value.logs())
        list_of_container.append(container)
#        list_of_logs.append(container.logs())
        dic_of_logs.update({container.name:container.logs()})





#        int_str=int(list_of_container[0])
#    return list_of_container 
#        print(container.logs(stream=True))

#        for line in container.logs(stream=True):
#            print (line.strip())

#def show_logs():
#        ic3e6600a3a
#    all_id=show_all_container()
#    container=all_id[1]
#    print(container.logs(stream=True))


list_of_container = []
dic_of_logs = {}
#show_logs()
show_all_container()
print("len list_of_logs",len(dic_of_logs))
val=list_of_container[1]
#val=int(val)
print (dic_of_logs.get("affectionate_johnson"))
