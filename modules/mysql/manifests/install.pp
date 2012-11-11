class mysql::install{
package { "mysql":
          name => "mysql-server",
          ensure => present,
          require => User["mysql"],
}
 user { "mysql":
        ensure => present,
        gid    => "mysql",
        shell  => "/bin/false",
        require => Group["mysql"],
}
group { "mysql":
       ensure => present,
}
}
         

