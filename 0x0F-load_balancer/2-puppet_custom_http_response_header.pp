# Automating project requirements using Puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
  require => Package['nginx'],
}

file_line { 'custom_404_error_page':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => '^error_page 404',
  line   => 'error_page 404 /404.html;',
}

file_line { 'custom_404_error_page_location':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'location = /404.html',
  line   => "location = /404.html {\n\troot /var/www/html;\n\tinternal;\n}",
}

file_line { 'redirect_permanent':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'rewrite ^/redirect_me',
  line   => 'rewrite ^/redirect_me https://www.github.com/besthor permanent;',
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
