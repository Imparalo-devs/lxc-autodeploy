import requests
import json

def create_lxc_container(container_name, memory, network, disks):
    url = 'https://proxmox.example.com/api2/json/nodes/YOUR_NODE/lxc'
    headers = {'Authorization': 'PVEAPIToken=YOUR_TOKEN'}
    data = {
        'vmid': 100,
        'hostname': container_name,
        'memory': memory,
        'net0': network,
        'mp0': disks
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'Successfully created container: {container_name}')
    else:
        print(f'Failed to create container: {container_name}, Error: {response.text}'