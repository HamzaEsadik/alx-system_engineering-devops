#make changes to our configuration file
exec { 'update_configuration':
  path    => '/etc/ssh/'
  command => "sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/'
              /etc/ssh/ssh_config && echo 'IdentityFile ~/.ssh/school' >>
              /etc/ssh/ssh_config",
}
