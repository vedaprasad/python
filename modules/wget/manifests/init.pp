class wget {
package { wget:
          ensure => present,
}
user { "vedu":
       ensure => "present",
       uid    => "1000",
       home   => "/home/vedu",
       shell  =>  "/bin/bash",
}
}
