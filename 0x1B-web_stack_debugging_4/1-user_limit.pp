#Puppet Manifest
#change the soft and hard limits for holberton user

file_line { 'change_hard_limit':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 4096',
  match => '^holberton hard nofile',
}

file_line { 'change_soft_limit':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 4096',
  match => '^holberton soft nofile',
}