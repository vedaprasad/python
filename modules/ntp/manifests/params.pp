class ntp::params {
case $operatingsystem {
solaris:{
$package_name ='ntp'
}
centos:{
$package_name ='ntp'
}
}
