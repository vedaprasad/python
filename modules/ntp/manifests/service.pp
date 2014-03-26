class ntp::service {
service { "ntp":
          name => "ntpd",
          ensure => running,
          require => Class["ntp::install"],
}
}


