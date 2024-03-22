# This Puppet manifest kills a process
exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],
  onlyif      => 'pgrep -f killmenow',
  refreshonly => false,
}
