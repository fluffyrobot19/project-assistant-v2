output "vpc_id" {
	value = aws_vpc.pa_vpc.id
}

output "public_subnet_id" {
	value = aws_subnet.pa_public_subnets[0].id
}

output "private_subnet_id_1" {
	value = aws_subnet.pa_private_subnets[0].id
}

output "private_subnet_id_2" {
	value = aws_subnet.pa_private_subnets[1].id
}

output "private_subnet_id_3" {
	value = aws_subnet.pa_private_subnets[2].id
}
