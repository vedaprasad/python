node 'nod1.sqpr.com'{
include wget
include rsync
include  mysql
}
node 'node2.spqr.com' inherits 'nod1.sqpr.com' {
}
