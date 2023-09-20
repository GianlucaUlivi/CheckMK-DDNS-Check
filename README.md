# CheckMK DDNS Check
A custom CheckMK plugin to verify your current Public IP against a DNS Record, useful for checking the correct update of a DDNS Service and Record.

### How to install
Copy the python file into your CheckMK host at this location:  
`/opt/omd/sites/<SITE>/local/lib/nagios/plugins/ddns_check.py`  

Install or Update requests and dnspython via pip:  
`pip3 install requests dnspython`  

### Test and Verify
You can test and verify the plugin by executing it directly with Python via the CLI:  
`python3 ddns_check.py <hostname> <DNS Server>`

### Use in your CheckMK Installation
You can create a rule to implement this plugin as a Service under `Setup > Services > Other services >Integrate Nagios plugins`  
Configure the Command line as: `python3 /opt/omd/sites/<SITE>/local/lib/nagios/plugins/ddns_check.py <hostname> <DNS Server>`
