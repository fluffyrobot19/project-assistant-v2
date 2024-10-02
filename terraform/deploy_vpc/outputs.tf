output "vpc_id" {
	value = aws_vpc.pa_vpc.id
}

output "public_subnet_id" {
	value = aws_subnet.pa_public_subnets[0].id
}

output "private_subnet_id" {
	value = aws_subnet.pa_private_subnets[0].id
}
