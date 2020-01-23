import boto3
import time

region = 'us-east-1'
ec2 = boto3.resource('ec2',region_name=region)


# creating  VPC
vpc = ec2.create_vpc(CidrBlock='172.16.0.0/16')

vpc.create_tags(Tags=[{"Key": "Name", "Value": "Dont-DELETE-Rakesh-vpc"},
                	   {"Key": "Email", "Value": "rakesh.reddy@quantiphi.com"},
                	   	{"Key": "Project", "Value": "FrameworkEngineer-Trainingrole"}])

vpc.wait_until_available()
print(vpc.id)

# creating an internet gateway and attaching it to VPC
internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)

# creating a route table for public subnets and a public route
routetable1 = vpc.create_route_table()
route = routetable1.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)
print(routetable1.id)

#creating a route table for private subnets 

routetable2 = vpc.create_route_table()
route = routetable2.create_route(DestinationCidrBlock='', GatewayId=internetgateway.id)
print(routetable2.id)

#creating two public subnets - subnet1 and subnet2

subnet1 = ec2.create_subnet(CidrBlock = '172.16.1.0/24', VpcId= vpc.id)
routetable1.associate_with_subnet(SubnetId=subnet1.id)

subnet2 = ec2.create_subnet(CidrBlock = '172.16.2.0/24', VpcId= vpc.id)
routetable1.associate_with_subnet(SubnetId=subnet2.id)

# creating private subnets - subnet3 and subnet4

subnet3 = ec2.create_subnet(CidrBlock = '172.16.3.0/24', VpcId= vpc.id)
routetable2.associate_with_subnet(SubnetId=subnet3.id)

subnet4 = ec2.create_subnet(CidrBlock = '172.16.4.0/24', VpcId= vpc.id)
routetable2.associate_with_subnet(SubnetId=subnet4.id)

#CREATING SECURITY GROUPS

securitygroup = ec2.create_security_group(GroupName='SSH-ONLY', Description='only allow SSH traffic', VpcId=vpc.id)
securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)

#creating an ec2 instance inside our private subnet(subnet4)

instances = ec2.create_instances(
 ImageId='ami-0de53d8956e8dcf80',
 InstanceType='t2.micro',
 MaxCount=1,
 MinCount=1,
 NetworkInterfaces=[{
 'SubnetId': subnet4.id,
 'DeviceIndex': 0,
 'AssociatePublicIpAddress': True,
 'Groups': [securitygroup.group_id]
 }],
 KeyName='rakesh-key-pair')

#CREATING A NAT GATEWAY AND ASSOCIATING IT WITH PUBLIC SUBNET(subnet1)

addr = ec2.allocate_address(Domain='vpc')
c = addr['AllocationId']
natgateway = ec2.create_nat_gateway(AllocationId=c,SubnetId=subnet1)
print(natgateway)
time.sleep(100)




