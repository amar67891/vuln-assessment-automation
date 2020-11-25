# vuln-assessment-automation


Automation Script for Internal Network Vulnerability Management 

This small script helps network administrator and Information security engineers to automate making an inventory for all devices on the internal network and perform a  the vulnerability assessment for each one of these devices and report back in a form of HTML.
This python code divides the network into two equal segments and uses Netmiko to connect to two different Kali machines (the number of network segments and Kali machines can be easily scaled) through SSH, and then the one of the two Kali machines perform the inventory scan (using Nmap) and after that this machine will continue to Scan the first segment of the network devices looking for vulnerabilities taking advantage of the Vulners module and others in Nmap. While this scan is running the second machine will start its scan parallelly and start searching for vulnerabilities in the second segment of the network. Lastly the three reports will be transferred to the machine that is running the code through SCP connection.
   
This script will produce three HTML reports:
1.	An inventory report is generated as a list of the devices currently running on the network with MAC address and IP address and this report called (device_inventory_report).
2.	The first segment of the network vulnerability assessment report which shows the vulnerabilities on the devices of the first segments of the network and the report is called (vulnerability_report_section1).
3.	The second segment of the network vulnerability assessment report which shows the vulnerabilities on the devices of the second segment of the network and the report is called(vulnerability_report_section2). 
