import tf_models
import boto_tool
import json

def tfNatInstance(args=None):
    '''
    Required Variables from args:
        region                    : string of source instance region
        name                      :  string of instance tag:Name
        subnetId                  : string of subnet to assign NAT instance too
        keyName                   : string of aws keypair name
        tags                      : list of dicts [{'Key':'Value'},...]
        vpcSecurityGroupIds       : list of strings of SGs
        sourceDestCheck           : boolean (NAT = False, Bastion = True)
    '''
    
    try:  # Gather required variables
        if not args:
            print 'No args passed'
            return
        else:
            data = args
            
        region                      = data.get('region')
        name                        = data.get('name')
        subnetId                    = data.get('subnetId')
        keyName                     = data.get('keyName')
        tags                        = data.get('tags')
        vpcSecurityGroupIds         = data.get('vpcSecurityGroupIds')
        associatePublicIpAddress    = True
        sourceDestCheck             = data.get('sourceDestCheck')
            
    except Exception as e:
        print str(e)
        return
    
    errSet = set()  # Record errors
    msgSet = set()  # Record warnings 
    
    # Check for requirements
    required = [name, region]
    if None in required:
        errSet.add('Required variables are missing')
    
    try:
        tags = json.loads(tags) if tags else None
    except Exception as e:
        errSet.add(str(e))
    
    try:
        vpcSecurityGroupIds = json.loads(
            vpcSecurityGroupIds) if vpcSecurityGroupIds else None
    except Exception as e:
        errSet.add(str(e))
    
    # Quit if error in inputs
    if len(errSet) > 0:
        print list(errSet)
        return
    
    ami             = boto_tool.latestVpcNatImageId(region)
    instanceType    = 't2.micro'
            
    return tf_models.Terraform.awsInstance(
        name,
        region,
        ami,
        instanceType,
        subnetId,
        keyName,
        tags,
        vpcSecurityGroupIds,
        associatePublicIpAddress)
