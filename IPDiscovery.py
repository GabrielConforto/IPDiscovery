import nmap
print("Tool made by: https://github.com/GabrielConforto")
print("----------------------")
class Network(object):
    def __init__(self):
        ip = input('Enter the IP address of the target router')
        self.ip = ip

    def networkscanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network =self.ip + '/24'

        print('Starting the scan')

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print("Host\t{}".format(host))
if __name__ == "__main__":
    D = Network()
    D.networkscanner()





