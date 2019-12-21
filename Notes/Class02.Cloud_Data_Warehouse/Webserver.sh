#!/bin/bash

sudo yum update -y
sudo yum install -y httpd24 php70 mysql56-server php70-mysqlnd
sudo service httpd start
sudo chkconfig httpd on
cd /var/www/html
echo "<?php phpinfo(); ?>" > /var/www/html/index.php
