class git::install {
         package { "git":
         name => "git",
         ensure => present,
}
}
