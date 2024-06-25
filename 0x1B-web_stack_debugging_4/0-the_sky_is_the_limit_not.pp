#Puppet Manifest

file { '/etc/security/limits.conf':
  ensure  => file,
  mode    => '0644',
  content => template('limits/limits.conf.erb'),
}