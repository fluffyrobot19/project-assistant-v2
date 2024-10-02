resource "aws_vpc" "main" {
	cidr_block = "10.0.0.0/16"
	
	tags = {
		Name = "PA VPC"
	}
}

resource "aws_subnet" "public_subnets" {
	count = 3
	vpc_id = aws_vpc.main.id
	cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)

	tags = {
		Name = "PA Public Subnet ${count.index + 1}"
	}
}

resource "aws_subnet" "private_subnets" {
	count = 3
	vpc_id = aws_vpc.main.id
	cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index+3)

	tags = {
		Name = "PA Private Subnet ${count.index + 1}"
	}
}

resource "aws_internet_gateway" "gw" {
	vpc_id = aws_vpc.main.id

	tags = {
		Name = "PA VPC IG"
	}
}

resource "aws_route_table" "second_rt" {
	vpc_id = aws_vpc.main.id

	route {
		cidr_block = "0.0.0.0/0"
		gateway_id = aws_internet_gateway.gw.id
	}

	tags = {
		Name = "PA RT for GW"
	}
}

resource "aws_route_table_association" "public_subnets_association" {
	count = 3
	subnet_id = "${element(aws_subnet.public_subnets.*.id, count.index)}"
	route_table_id = aws_route_table.second_rt.id
}
