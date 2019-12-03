# pinger
wrapped a "pign a server" action within a python decorator


To allow an aws machine to be pinged:

https://stackoverflow.com/questions/21981796/cannot-ping-aws-ec2-instance

Add a new EC2 security group inbound rule:
  Type: Custom ICMP rule
  Protocol: Echo Request
  Port: N/A
  Source: your choice (I would select Anywhere to be able to ping from any machine)
