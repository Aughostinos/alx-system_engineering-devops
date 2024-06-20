# 0-strace_is_your_friend.pp
# a manifest that fix extension name of php file

exec { 'fix_typo_in_files':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-includes/js/zxcvbn.min.js /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-includes/js/zxcvbn.min.js /var/www/html/wp-settings.php',
}
