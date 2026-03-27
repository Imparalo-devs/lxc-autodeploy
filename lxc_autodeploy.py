import time
from database import fetch_lxc_parameters
from lxc_manager import create_lxc_container

def main():
    while True:
        lxc_params = fetch_lxc_parameters()
        for param in lxc_params:
            container_name = param['containername']
            memory = param['memory']
            network = param['network']
            disks = param['disks']
            create_lxc_container(container_name, memory, network, disks)
        time.sleep(3600)  # Run every hour

if __name__ == '__main__':
    main()