#Puppet Manifest

file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/default/nginx'],
}

exec { 'restart-nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe  => File['/etc/default/nginx'],
}