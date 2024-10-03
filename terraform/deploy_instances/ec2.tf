resource "aws_security_group" "pa_ec2_sg" {
	vpc_id = local.vpc_id 

	ingress {
		from_port = var.my_port
		to_port = var.my_port
		protocol = "tcp"
		cidr_blocks = [var.my_ip] 
	}

	ingress {
		from_port = var.anywhere_port
		to_port = var.anywhere_port
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}

	egress {
		from_port = var.db_port
		to_port = var.db_port
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}

	tags = {
		Name = "pa-ec2-sg"
	}
}

resource "aws_instance" "pa_ec2" {
	ami = "ami-0fed63ea358539e44"
	instance_type = "t2.micro"
	subnet_id = local.public_subnet_id
	security_groups = [aws_security_group.pa_ec2_sg.id]
	key_name = var.my_key_pair 

	tags = {
		Name = "pa-ec2"
	} 
}
