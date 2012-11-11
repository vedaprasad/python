node 'nod1.sqpr.com'{
include wget
include rsync
include  mysql
include ntp
}
node 'node2.spqr.com' inherits 'nod1.sqpr.com' {
}
node 'node3.spqr.com' inherites 'node2.spqr.com'{
}
