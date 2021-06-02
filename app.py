"""
Given a host IP and prefix (mask bits), return
JSON output of network details:
'network_address'
'network_mask'
'first_host'
'last_host'
'broadcast'

For example, given:
 /192.168.1.34/24
return:
 {'network_address': 192.168.1.0,
  'network_mask': 255.255.255.0,
  'first_host': 192.168.1.1,
  'last_host': 192.168.1.254,
  'broadcast': 192.168.1.255,
 }
"""
import inspect
import ipaddress
from flask import Flask
app = Flask(__name__)

@app.route('/<host_ip>/<prefix>')
def netaddr(host_ip, prefix):
    """Return network address and subnet mask."""
    ip_address = host_ip + '/' + prefix
    try:
        ip_net = ipaddress.ip_network(ip_address, False)
        output = {'network_address': str(ip_net.network_addressi),
                  'network_mask': str(ip_net.netmask),
                  'first_host': str(ip_net[1]),
                  'last_host': str(ip_net[-2]),
                  'broadcast': str(ip_net[-1]),
                 }
        return output
    except ValueError:
        return 'Invalid IP/prefix format'

@app.route('/')
def directions():
    """Provide help."""
    help_screen = inspect.cleandoc("""
        Call this service with URL containing: /<ip_address>/<prefix>
        Example: /192.168.1.34/24""")
    return help_screen

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
