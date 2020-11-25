
from netmiko import ConnectHandler, SCPConn
from getpass import getpass
import time 
import os
import datetime
import ipaddress
import netaddr
import threading
from netaddr import *




# Entering the IP addresses for the machines that will scan the network
kali1 = input("Enter the IP address of the First Kali: ")
ip1 = ipaddress.ip_address(kali1)
kali2 = input("Enter the IP address of the Second Kali: ")
ip2 = ipaddress.ip_address(kali2)

# Adding the Targeted Network Address and Divide it 

network = IPNetwork(input('ENTER THE Network IP Address: '))
ip_list = list(network)
a=len(ip_list)
b = int(a/2)
iprange1 = IPRange(ip_list[0] , ip_list[b])
ip2 = IPRange(ip_list[b+1] , ip_list[a-1])
cidrs = netaddr.iprange_to_cidrs(ip_list[0], ip_list[b-1])
cidrs1 = netaddr.iprange_to_cidrs(ip_list[b], ip_list[a-1])
c = cidrs[0]
d = cidrs1[0]
f= IPNetwork(network).__str__()
e = str(c)
g = str(d)
j = str(f)
print ("### Network Sections that will be Scanned: #####")
print("## Network Section One: ", c)
print("## Network Section Two: ", d)

# Replacing Network Addresses in the files

# Editing the second Line in the First file
fin1 = open("commands_file_for_linux_automation", "rt")
data1 = fin1.read()
data1 = data1.replace('192.168.45.0' , e)
fin1.close()
fin1 = open("commands_file_for_linux_automation", "wt")
fin1.write(data1)
fin1.close()
#close the First file

# Editing the First Line 
fin = open("commands_file_for_linux_automation", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace('192.168.44.0/24' , f)
#close the input file
fin.close()
#open the input file in write mode
fin = open("commands_file_for_linux_automation", "wt")
#overrite the input file with the resulting data
fin.write(data)
fin.close()

# Editing the Second File 
fin2 = open("commands_file_for_linux_automation2", "rt")
data2 = fin2.read()
data2 = data2.replace('192.168.45.0' , g)
fin2.close()
fin2 = open("commands_file_for_linux_automation2", "wt")
fin2.write(data2)
fin2.close()

# Automation Starts From here
with open('commands_file_for_linux_automation') as f:
     commands_to_send = f.read().splitlines()
with open('commands_file_for_linux_automation2') as f:
     commandss_to_send = f.read().splitlines()



# Connection Information for the first machine
iosv_l2_s1 = {
    'device_type': 'linux',
    'ip': kali1,
    'username': input("Enter Your SSH username 1st Kali: "),
    'password': getpass(),
    #'global_delay_factor': 140,
    #'timeout':140,
    'blocking_timeout':2080,
}

iosv_l2_s2 = {
    'device_type': 'linux',
    'ip': kali2,
    'username': input("Enter Your SSH username 2nd Kali: "),
    'password': getpass(),
    'blocking_timeout': 2080,
    
}

all_devices = [iosv_l2_s1, iosv_l2_s2]


def ssh_session(router, commands):
    
    net_connect = ConnectHandler(**router)
    output = net_connect.send_config_set(commands) 


ssh_session(iosv_l2_s1,commands_to_send)
ssh_session(iosv_l2_s2,commandss_to_send)

#  Open secure copy protocol to transfer backup file to server
ssh_conn = ConnectHandler(**iosv_l2_s1)
scp_conn = SCPConn(ssh_conn)
# Define source and destination file locations and names
s_file = '/root/devices_inventory_report.html'
s1_file = '/root/vulnerability_report_section1.html'
d_file = './devices_inventory_report.html'
d1_file = './vulnerability_report_section1.html'
#  Transfer file
scp_conn.scp_get_file(s_file, d_file)
scp_conn.scp_get_file(s1_file, d1_file)
#  Close secure copy protocol session
scp_conn.close()
#  Close ssh session
ssh_conn.disconnect()
# Renaming Files To add DATES To File names
old_file_name1 = "./devices_inventory_report.html"
new_file_name1 =  time.strftime('devices_inventory_report_%d_%m_%Y.html')
os.rename(old_file_name1, new_file_name1)
old_file_name = "./vulnerability_report_section1.html"
new_file_name =  time.strftime('vulnerability_report_section1_%d_%m_%Y.html')
os.rename(old_file_name, new_file_name)
print("** Inventory and First Section Scanned Successfully!**")
print("** Reports Transferred for the First Section!**")





#  Open secure copy protocol to transfer backup file to server
ssh_conn1 = ConnectHandler(**iosv_l2_s2)
scp_conn1 = SCPConn(ssh_conn1)
# Define source and destination file locations and names
s2_file = '/root/vulnerability_report_section2.html'
d2_file = './vulnerability_report_section2.html'
#  Transfer file
scp_conn1.scp_get_file(s2_file, d2_file)
#  Close secure copy protocol session
scp_conn1.close()
#  Close ssh session
ssh_conn1.disconnect()
old_file_name2 = "./vulnerability_report_section2.html"
new_file_name2 =  time.strftime('vulnerability_report_section2_%d_%m_%Y.html')
os.rename(old_file_name2, new_file_name2)
print("** Second Section scanned Successfully!**")
print("** Report Transferred for the Second Section!**")


# Resorting Network Addresses in the files

# Editing the second Line in the First file
fin1 = open("commands_file_for_linux_automation", "rt")
data1 = fin1.read()
data1 = data1.replace(e, '192.168.45.0')
fin1.close()
fin1 = open("commands_file_for_linux_automation", "wt")
fin1.write(data1)
fin1.close()
#close the First file

# Editing the First Line 
fin = open("commands_file_for_linux_automation", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace(j, '192.168.44.0/24')
#close the input file
fin.close()
#open the input file in write mode
fin = open("commands_file_for_linux_automation", "wt")
#overrite the input file with the resulting data
fin.write(data)
fin.close()

# Editing the Second File 
fin2 = open("commands_file_for_linux_automation2", "rt")
data2 = fin2.read()
data2 = data2.replace(g, '192.168.45.0')
fin2.close()
fin2 = open("commands_file_for_linux_automation2", "wt")
fin2.write(data2)
fin2.close()



