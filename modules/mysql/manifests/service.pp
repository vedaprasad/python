class mysql::service {
      service {"mysqld":
      ensure => running,
      require => Class["mysql::install"],
}
}
