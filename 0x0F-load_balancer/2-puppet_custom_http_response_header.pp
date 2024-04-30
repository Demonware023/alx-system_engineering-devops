# Puppet manifest to configure Nginx with a custom HTTP header 'X-Served-By'

# Automating project requirements using Puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'nginx_custom_header':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "add_header X-Served-By ${::hostname};",
  match  => '^add_header X-Served-By',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
