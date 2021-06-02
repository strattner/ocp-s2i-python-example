# Get network address
Given a typical network interface of the form ip/bit (like 192.168.1.45/27),
return network details in JSON:
```
 {'network_address': 192.168.1.0
  'network_mask': 255.255.255.224
  'first_host': 192.168.1.1
  'last_host': 192.168.1.30
  'broadcast': 192.168.1.31
 }
```
Purpose of this is to demonstrate OpenShift 'Source to Image' capability.

## Example
To test this, run directly with *python app.py* and access via curl:
```
$ curl http://127.0.0.1:8080/192.168.45.10/17
```
## Inspiration
This was started by a git clone of
https://github.com/ocp-power-demos/s2i-pyflask-demo
But since the app.py was changed completely, it didn't seem right
to treat it just as a fork.
