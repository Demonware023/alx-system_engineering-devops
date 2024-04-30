# Puppet manifest to automate the configuration of Nginx with a custom HTTP header

class nginx_custom_header {
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

  exec { 'add_custom_header':
    command => "sed -i '/server_name _;/a add_header X-Served-By \$HOSTNAME;' /etc/nginx/sites-available/default",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

include nginx_custom_header
