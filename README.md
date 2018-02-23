# ambari-haproxy-service
Ambari service for HAProxy

Steps: 

1. To download the HAproxy service folder, run below


```
# On Ambari Server Host
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/saumilmayani/ambari-haproxy-service.git   /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/HAPROXY
```

2. Restart Ambari-server

```
# On Ambari Server host
ambari-server restart
```

3. Login to Ambari Server Web UI and click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard

4. Select "HAProxy" and click Next

5. Select the Host where you would want to run "HAProxy Server" and click "Next"

6. Choose to customize "haproxy.cfg" now or later and Hit "Next"

7. Navigate to "Review" Screen and Hit "Deploy"

8. "Install, Start and Test" will complete "Installing HAProxy" and "Starting HAProxy" Service
Click Next once you see "Success" Message

9. Once "Complete", You will see "HAProxy" Service on "Ambari Dashboard"

10. For any changes to "haproxy.cfg", navigate to "Configs" page, 

```
Modify the "haproxy.cfg template".
Save
Restart HAProxy
```
