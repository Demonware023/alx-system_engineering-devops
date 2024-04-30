# Puppet manifest to configure Nginx with a custom HTTP header 'X-Served-By'

# Automating project requirements using Puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/besthor permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'custom_http_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'add_header X-Served-By',
  line   => "add_header X-Served-By \$hostname;",
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
