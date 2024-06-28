#Puppet Manifest
#change the soft and hard limits for holberton user

exec { 'set_holberton_hard_limit':
  command => '/bin/sed -i "s/holberton hard nofile [0-9]*/holberton hard nofile 4096/" /etc/security/limits.conf || echo "holberton hard nofile 4096" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}

exec { 'set_holberton_soft_limit':
  command => '/bin/sed -i "s/holberton soft nofile [0-9]*/holberton soft nofile 4096/" /etc/security/limits.conf || echo "holberton soft nofile 4096" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}
