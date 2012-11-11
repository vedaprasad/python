class ntp::install {
package { "ntp":
          name => "ntp",
          ensure => present,
}
}

