from datetime import datetime


def remove_none(d):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.
    This alters the input so you may wish to ``copy`` the dict first.

    :return: dict
    """
    for key, value in d.items():
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            remove_none(value)
    return d


def time_now():
    """
    :return: str of time now like -20160906-1224
    """
    return datetime.strftime(datetime.now(), '-%Y%m%d-%H%M')


class Terraform:
    @staticmethod
    def set_provider(region):
        """
        :param region: str
        """
        return 'aws.' + region

    @staticmethod
    def set_id(resource, name):
        """
        :param resource: str
        :param name: str
        """
        return '${' + resource + '.' + name + '.id}'

    @classmethod
    def aws_instance(
            cls,
            name=None,
            region=None,
            ami=None,
            instance_type='m3.medium',
            subnet_id=None,
            key_name=None,  # the keypair name
            tags=None,
            vpc_security_group_ids=None,
            associate_public_ip_address=None,
            source_dest_check=None):
        """
        :param name: str
        :param region: str
        :param ami: str
        :param instance_type: str
        :param subnet_id: str
        :param key_name: str
        :param tags: dict
        :param vpc_security_group_ids: list
        :param associate_public_ip_address: bool
        :param source_dest_check: bool
        :return: Terraform
        """

        tags.update({'Name': name}) if tags else tags

        resource = 'aws_instance'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, ami=ami, subnet_id=subnet_id,
                       key_name=key_name, instance_type=instance_type,
                       vpc_security_group_ids=vpc_security_group_ids, tags=tags,
                       associate_public_ip_address=associate_public_ip_address,
                       source_dest_check=source_dest_check)}))

    @classmethod
    def aws_ami_from_instance(
            cls,
            name,
            region,
            source_instance_id,
            tags=None):
        """
        :param name: str
        :param region: str
        :param source_instance_id: str
        :param tags: dict
        :return: Terraform
        """
        name += time_now()
        tags.update({'Name': name}) if tags else None

        resource = 'aws_ami_from_instance'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, name=name,
                       source_instance_id=source_instance_id, tags=tags)}))

    @classmethod
    def aws_elb(
            cls,
            name,
            region,
            listeners,
            subnets,
            health_check=None,
            internal=None,
            security_groups=None,
            instances=None):
        """
        :param name: str
        :param region: str
        :param listeners: list
        :param subnets: list
        :param health_check: dict
        :param internal: bool
        :param security_groups: list
        :param instances: list
        :return: Terraform
        """
        resource = 'aws_elb'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, name=name, listener=listeners,
                       subnets=subnets, health_check=health_check,
                       internal=internal, security_groups=security_groups,
                       instances=instances)}))

    @classmethod
    def aws_elasticache_cluster(
            cls,
            name,
            region,
            node_type,
            num_cache_nodes,
            parameter_group_name,
            port,
            engine,
            subnet_group_name=None,
            security_group_ids=None):
        """

        :param name: str
        :param region: str
        :param node_type: str
        :param num_cache_nodes: str
        :param parameter_group_name: str
        :param port: int
        :param engine: str
        :param subnet_group_name: str
        :param security_group_ids: list
        :return: Terraform
        """
        resource = 'aws_elasticache_cluster'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, cluster_id=name, node_type=node_type,
                       num_cache_nodes=num_cache_nodes,
                       parameter_group_name=parameter_group_name, port=port,
                       subnet_group_name=subnet_group_name,
                       security_group_ids=security_group_ids, engine=engine)}))

    @classmethod
    def aws_rds(
            cls,
            name,
            region,
            instance_class,
            snapshot_id,
            allocated_storage=None,
            engine=None,
            engine_version=None,
            db_subnet_group_name=None,
            vpc_security_group_ids=None,
            parameter_group_name=None,
            publicly_accessible=False,
            username=None,
            password=''):
        """
        :param name: str
        :param region: str
        :param instance_class: str
        :param snapshot_id: str
        :param allocated_storage: str
        :param engine: str
        :param engine_version: str
        :param db_subnet_group_name: str
        :param vpc_security_group_ids: list
        :param parameter_group_name: str
        :param publicly_accessible: bool
        :param username:
        :param password:
        :return: Terraform
        """
        resource = 'aws_db_instance'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, identifier=name,
                       snapshot_identifier=snapshot_id,
                       allocated_storage=allocated_storage, engine=engine,
                       engine_version=engine_version,
                       instance_class=instance_class,
                       db_subnet_group_name=db_subnet_group_name,
                       vpc_security_group_ids=vpc_security_group_ids,
                       parameter_group_name=parameter_group_name,
                       publicly_accessible=publicly_accessible,
                       username=username, password=password)}))

    @classmethod
    def aws_security_group(
            cls,
            name,
            region,
            name_prefix=None,
            description=None,
            ingress=None,
            egress=None,
            vpc_id=None,
            tags=None):
        """
        :param name:
        :param region:
        :param name_prefix:
        :param description:
        :param ingress:
        :param egress:
        :param vpc_id:
        :param tags:
        :return:
        """
        resource = 'aws_security_group'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, name=name, name_prefix=name_prefix,
                       description=description, ingress=ingress, egress=egress,
                       tags=tags, vpc_id=vpc_id)}))

    # *** VPC (Networking) ***

    @classmethod
    def aws_vpc(
            cls,
            name,
            region,
            cidr_block,
            instance_tenancy=None,
            enable_dns_support=None,
            enable_dns_hostnames=None,
            enable_classiclink=None,
            tags=None):
        """
        :param name: str
        :param region: str
        :param cidr_block: str
        :param instance_tenancy: str
        :param enable_dns_support: str
        :param enable_dns_hostnames: str
        :param enable_classiclink: str
        :param tags: dict
        :return: Terraform
        """
        resource = 'aws_vpc'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, cidr_block=cidr_block,
                       instance_tenancy=instance_tenancy,
                       enable_dns_support=enable_dns_support,
                       enable_dns_hostnames=enable_dns_hostnames,
                       enable_classiclink=enable_classiclink, tags=tags)}))

    @classmethod
    def aws_internet_gateway(
            cls,
            name,
            region,
            vpc_id,
            tags=None):
        """
        :param name: str
        :param region: str
        :param vpc_id: str
        :param tags: dict
        :return: Terraform
        """
        resource = 'aws_internet_gateway'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, vpc_id=vpc_id, tags=tags)}))

    @classmethod
    def aws_subnet(
            cls,
            name,
            region,
            vpc_id,
            cidr_block,
            map_public_ip_on_launch=None,
            availability_zone=None,
            tags=None):
        """
        :param name: str
        :param region: str
        :param vpc_id: str
        :param cidr_block: str
        :param map_public_ip_on_launch: bool
        :param availability_zone: str
        :param tags: dict
        :return: Terraform
        """
        resource = 'aws_subnet'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, vpc_id=vpc_id, cidr_block=cidr_block,
                       map_public_ip_on_launch=map_public_ip_on_launch,
                       availability_zone=availability_zone, tags=tags)}))

    @classmethod
    def aws_eip(
            cls,
            name,
            region,
            vpc=None,
            instance=None,
            network_interface=None,
            associate_with_private_ip=None):
        """
        :param name: str
        :param region: str
        :param vpc: str
        :param instance: str
        :param network_interface: str
        :param associate_with_private_ip: bool
        :return: Terraform
        """
        resource = 'aws_eip'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, vpc=vpc, instance=instance,
                       network_interface=network_interface,
                       associate_with_private_ip=associate_with_private_ip)}))

    @classmethod
    def aws_nat_gateway(
            cls,
            name,
            region,
            allocation_id,
            subnet_id):
        """
        :param name: str
        :param region: str
        :param allocation_id: str
        :param subnet_id: str
        :return: Terraform
        """
        resource = 'aws_nat_gateway'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, allocation_id=allocation_id,
                       subnet_id=subnet_id)}))

    @classmethod
    def aws_route_table(
            cls,
            name,
            region,
            vpc_id,
            route=None,
            propagating_vgws=None,
            tags=None):
        """
        :param name: str
        :param region: str
        :param vpc_id: str
        :param route: dict
        :param propagating_vgws: bool
        :param tags: dict
        :return:
        """
        resource = 'aws_route_table'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, vpc_id=vpc_id, route=route,
                       propagating_vgws=propagating_vgws, tags=tags)}))

    @classmethod
    def aws_route(
            cls,
            name,
            region,
            route_table_id,
            destination_cidr_block,
            vpc_peering_connection_id=None,
            gateway_id=None,
            nat_gateway_id=None,
            instance_id=None,
            network_interface_id=None):
        """
        :param name: str
        :param region: str
        :param route_table_id: str
        :param destination_cidr_block: str
        :param vpc_peering_connection_id: str
        :param gateway_id: str
        :param nat_gateway_id: str
        :param instance_id: str
        :param network_interface_id: str
        :return: Terraform
        """
        resource = 'aws_route'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, route_table_id=route_table_id,
                       destination_cidr_block=destination_cidr_block,
                       vpc_peering_connection_id=vpc_peering_connection_id,
                       gateway_id=gateway_id, nat_gateway_id=nat_gateway_id,
                       instance_id=instance_id,
                       network_interface_id=network_interface_id)}))

    @classmethod
    def aws_route_table_association(
            cls,
            name,
            region,
            subnet_id,
            route_table_id):
        """
        :param name: str
        :param region: str
        :param subnet_id: str
        :param route_table_id: str
        :return: Terraform
        """
        resource = 'aws_route_table_association'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, subnet_id=subnet_id,
                       route_table_id=route_table_id)}))

    @classmethod
    def aws_main_route_table_association(
            cls,
            name,
            region,
            vpc_id,
            route_table_id):
        """
        :param name: str
        :param region: str
        :param vpc_id: str
        :param route_table_id: str
        :return: Terraform
        """
        resource = 'aws_main_route_table_association'
        id = Terraform.set_id(resource, name)
        provider = Terraform.set_provider(region)

        return cls(id, name, provider, resource, remove_none({
            name: dict(provider=provider, vpc_id=vpc_id,
                       route_table_id=route_table_id)}))

    def __init__(self, id, name, provider, resource, terraform):
        """
        :param id: str
        :param name: str
        :param provider: str
        :param resource: str
        :param terraform: dict
        """
        self.id = id
        self.terraform = terraform
        self.name = name
        self.resource = resource
        self.provider = provider

    def __str__(self):
        return self.id
