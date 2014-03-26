#module for rsync
class rsync {
package { rsync:
          ensure => present,
}
service { rsync:
          ensure => stopped,
          require => Package["rsync"],
}
}
