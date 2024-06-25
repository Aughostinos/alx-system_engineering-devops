#Puppet Manifest

exec { 'Increase_limits':
  command => "echo 'worker_rlimit_nofile 4096;' >> /etc/nginx/nginx.conf",
  path    => ['/usr/local/bin', '/bin'],
  unless  => "grep -q 'worker_rlimit_nofile 4096;' /etc/nginx/nginx.conf",
  notify  => Service['nginx']
}