#set up your client SSH configuration file so that you can connect to a server without typing a password.
#SSH client configuration must be configured to use the private key ~/.ssh/school
#SSH client configuration must be configured to refuse to authenticate using a password

file_line { 'path':
 ensure => 'present,
 path   => '/etc/ssh/ssh_config',
 line   => '	path ~/.ssh/school',
}

file_line {' disabled password',
 path => '/etc/ssh/ssh_config',
 line => '	PasswordAuthentication no',
}
