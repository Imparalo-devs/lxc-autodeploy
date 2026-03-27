import requests
import json

# Function to create an LXC container using Proxmox API

def create_lxc_container(container_name, memory, network, disks, node):
    # Proxmox API endpoint and authentication details
    proxmox_url = 'https://proxmox.example.com/api2/json'
    token = 'YOUR_API_TOKEN'
    headers = {'Authorization': f'PVEAPIToken={token}'}

    # Prepare the payload for container creation
    payload = {
        'vmid': 100,
        'hostname': container_name,
        'memory': memory,
        'net0': network,
        'mp0': disks
    }

    # Make the API call to create the container
    response = requests.post(f'{proxmox_url}/nodes/{node}/lxc', headers=headers, json=payload)
    if response.status_code == 200:
        print(f'Container {container_name} created successfully.')
    else:
        print(f'Failed to create container {container_name}: {response.text}')