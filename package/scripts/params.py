#!/usr/bin/env python

from resource_management import *
import status_params

# server configurations
config = Script.get_config()
tmp_dir = Script.get_tmp_dir()

config_dir = "/etc/haproxy/"

# params from haproxy.cfg

haproxy_cfg_content = config['configurations']['haproxy-cfg']['content']
