resource "aws_vpc" "pa_vpc" {
	cidr_block = "10.0.0.0/16"
	
	tags = {
		Name = "pa-vpc"
	}
}
