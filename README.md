# Get network address
A very simple Flask app that, given a host IP and prefix, returns the network address and subnet mask.
One step above "Hello, World", the purpose is to demonstrate the Source to Image (S2I) functionality of
OpenShift.

## Example
To test this, run directly with *python app.py* and access via curl:
```
$ curl http://127.0.0.1:8080/192.168.45.10/17
192.168.0.0 255.255.128.0
```
## Inspiration
More than just inspired by, this was started by a git clone of
https://github.com/ocp-power-demos/s2i-pyflask-demo
But since the app.py was changed completely, it didn't seem right
to treat it just as a fork.
