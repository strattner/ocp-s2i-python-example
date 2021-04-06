"""
Given a host IP and prefix (mask bits), return
the network address and subnet mask. Example:
/192.168.1.34/24
192.168.1.0 255.255.255.0
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
        return str(ip_net.network_address) + ' ' + str(ip_net.netmask)
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
    app.run(host="0.0.0.0", port=8088, debug=True)
