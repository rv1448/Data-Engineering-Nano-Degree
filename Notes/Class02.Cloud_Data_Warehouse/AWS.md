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

[Overview](https://paiml.github.io/awsbigdata/topics/security)
__AWS security best practices__

AWS storage:
	Object Storage
	Scale and flexibilty and no OS
	File storage
	Block storage - DB's

AWS block storage:
	- EC2 can have two types of block storages
	- EBS and Instance store
	- Instance volumes temp
	- Bound to single to EC2 instance
	- They are not persistent
	- No encrytion and backup

Storage Options: 
	- S3, S3 glasier
	- EFS
	- EBS
EC2 volumes:
	- Root volumes - EBS has snapshots and everything
	- Ephemaral volume - Temporary
	- lsblk - to list the boot volmes

Mounting the filesystems:
	- Boot volumes can be mounted to /dev/xvda

** VPC

	VPC - virtual private cloud
	subnets - 
	Route tables - one per a VPC
	SG - Permit and deny
	Network ACL - Deal with IP addresses
	NAT gateway - Netweork address translation
	


* Special Question
	Seperate accounts
