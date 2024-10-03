resource "aws_security_group" "pa_database_sg" {
	vpc_id = local.vpc_id	

	ingress {
		from_port = var.db_port
		to_port	= var.db_port
		protocol = "tcp"
		security_groups = [aws_security_group.pa_ec2_sg.id]
	}

	tags = {
		Name = "pa-database-sg"
	}
}

resource "aws_db_instance" "pa_database" {
	engine = var.db_engine
	db_name = var.db_name
	instance_class = "db.t4g.micro"
	allocated_storage = 5
	username = var.db_username
	password = var.db_password
	vpc_security_group_ids = [aws_security_group.pa_database_sg.id]
	skip_final_snapshot = true
	publicly_accessible = false
	db_subnet_group_name = aws_db_subnet_group.pa_db_subnet_group.name	

	tags = {
		Name = "pa-database"
	}
}

resource "aws_db_subnet_group" "pa_db_subnet_group" {
	name = "pa-db-subnet-group"
	subnet_ids = [local.private_subnet_1, local.private_subnet_2, local.private_subnet_3]	

	tags = {
		Name = "pa-db-subnet-group"
	}
}
