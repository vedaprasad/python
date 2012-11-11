class ntp::config{
file { "config":
       path => "/etc/ntp.conf", 
       source => "puppet:///modules/ntp/ntp.conf",
       ensure => "present",
       mode  => 0440,
       owner => "root",
       require => Class["ntp::install"],
       notify  => Class["ntp::service"],

}
}
