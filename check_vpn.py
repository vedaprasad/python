#!/usr/bin/python
import boto
import boto.ec2
import boto.vpc
ec2_region='us-east-1'
aws_access_key_id='XXXXXXXXXXX'
aws_secret_access_key='XXXXXXXXXXX'
tunnel_list = [ 'XXX' , 'XXXX' , 'XXXX' ]
ac8d99cd_shared = []
b5a177_owners = []
bd5f38_prod   = []


def test_vpn_status():
    try:
        ec2_conn = boto.vpc.connect_to_region(ec2_region, 
        aws_access_key_id= aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)
    except Exception as error:
        print str(error)

    for vpn_connection in ec2_conn.get_all_vpn_connections():
        for tunnel in vpn_connection.tunnels:
            for _list in tunnel_list:
                if vpn_connection.id == _list:
                    if vpn_connection.id == 'XXXXX':
                        ac8d99cd_shared.append(tunnel.status)
                    elif vpn_connection.id == 'XXXXX':
                         b5a177_owners.append(tunnel.status)
                    else:
                        bd5f38_prod.append(tunnel.status)

    if ac8d99cd_shared[0] == 'DOWN' and ac8d99cd_shared[1] == 'DOWN':
        print 'Both the tunnels of Shared VPN are Down'
    if b5a177_owners[0] == 'DOWN' and b5a177_owners[1] == 'DOWN':
        print  'Both the tunnels of Owners VPN are Down'
    if bd5f38_prod[0] == 'DOWN' and bd5f38_prod[1] == 'DOWN':
        print 'Both the tunnels of Prod VPN are Down'


if __name__ == "__main__":
        test_vpn_status()
