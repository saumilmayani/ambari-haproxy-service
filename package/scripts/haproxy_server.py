#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Ambari Agent

"""
import sys
import os
import datetime
from resource_management import *

from haproxy_service import haproxy_service

class HAPROXY(Script):
  def install(self, env):
    self.install_packages(env)
    print 'Install the HAPROXY Service';

  def configure(self, env, isInstall=False):
    import params
    import status_params
    env.set_params(params)
    env.set_params(status_params)
        
    # backup haproxy.cfg
    FilePath= '/etc/haproxy/haproxy.cfg'
    modifiedTime = os.path.getmtime(FilePath) 
    timeStamp =  datetime.datetime.fromtimestamp(modifiedTime).strftime("%b-%d-%y-%H:%M:%S")
    os.rename(FilePath,FilePath+"_"+timeStamp)

    #write out haproxy.cfg    

    properties_content=InlineTemplate(params.haproxy_cfg_content)
    File(format("/etc/haproxy/haproxy.cfg"), content=properties_content)

  def start(self, env):
    self.configure(env)
    haproxy_service(daemon_name='haproxy', action='start')

  def stop(self, env):
    haproxy_service(daemon_name='haproxy', action='stop')

  def status(self, env):
    haproxy_service(daemon_name='haproxy', action='status')


if __name__ == "__main__":
  HAPROXY().execute()

