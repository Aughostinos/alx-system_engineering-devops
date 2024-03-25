#set up your client SSH configuration file so that you can connect to a server without typing a password.
#SSH client configuration must be configured to use the private key ~/.ssh/school
#SSH client configuration must be configured to refuse to authenticate using a password

file { '/etc/ssh/ssh_config':
 content => " host 54.167.150.12
              IdentityFile ~/.ssh/school
              PasswordAuthentication no"
}
