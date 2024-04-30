# Puppet manifest to configure Nginx with a custom HTTP header 'X-Served-By'

# Automating project requirements using Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'custom_http_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'add_header X-Served-By',
  line   => "add_header X-Served-By \$hostname;",
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Include the nginx_custom_header class to apply the configuration
include nginx_custom_header
