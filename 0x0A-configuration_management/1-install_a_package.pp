# This Puppet manifest installs Flak
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
