class ntp::install {
package { "ntp":
          name => $ntp::params::package_name,
          ensure => present,
}
}

