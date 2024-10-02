resource "aws_subnet" "pa_public_subnets" {
	count = 3
	vpc_id = aws_vpc.pa_vpc.id
	cidr_block = cidrsubnet(aws_vpc.pa_vpc.cidr_block, 8, count.index)

	tags = {
		Name = "PA-public-SN-${count.index + 1}"
	}
}

resource "aws_subnet" "pa_private_subnets" {
	count = 3
	vpc_id = aws_vpc.pa_vpc.id
	cidr_block = cidrsubnet(aws_vpc.pa_vpc.cidr_block, 8, count.index+3)

	tags = {
		Name = "PA-private-SN-${count.index + 1}"
	}
}

resource "aws_internet_gateway" "pa_igw" {
	vpc_id = aws_vpc.pa_vpc.id

	tags = {
		Name = "PA-VPC-IGW"
	}
}

resource "aws_route_table" "pa_public_rt" {
	vpc_id = aws_vpc.pa_vpc.id

	route {
		cidr_block = "0.0.0.0/0"
		gateway_id = aws_internet_gateway.pa_igw.id
	}

	tags = {
		Name = "PA-public-RT"
	}
}

resource "aws_route_table_association" "pa_public_subnets_association" {
	count = 3
	subnet_id = "${element(aws_subnet.pa_public_subnets.*.id, count.index)}"
	route_table_id = aws_route_table.pa_public_rt.id
}

resource "aws_route_table" "pa_private_rt" {
	vpc_id = aws_vpc.pa_vpc.id

	tags = {
		Name = "PA-private-RT"
	}
}

resource "aws_route_table_association" "pa_private_subnets_association" {
	count = 3
	subnet_id = "${element(aws_subnet.pa_private_subnets.*.id, count.index)}"
	route_table_id = aws_route_table.pa_private_rt.id
}
