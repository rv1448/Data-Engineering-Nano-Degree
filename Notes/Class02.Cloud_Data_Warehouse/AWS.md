single availabilty zone 
-----------------------
single instance running on single AZ

single region & multiple instances 
----------------------------------
Load balance two AZ's 

multiple region & multiple instances 
------------------------------------
load two AZ's in each region and Route 53 for two regions 

##VPC - Belong to region and spread across AZ's
- Each VPC has multiple subnets 
* Ingress and Egress Control 
- Security groups determine allowed traffic to from instance by port 
* NACL - Network access control lists 
- Control traffic to a subnet 
##VPC design patterns 
- Internet-accesible VPC 
- VPC with public and private subnets 
	- Nat Gate way is used by private subnet instan for patches 
- VPN access to private subnets 
- internal-only VPC 
- VPC peering 


Private Data Center 
Subnets 
IP address 
Access control 
