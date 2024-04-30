# Puppet manifest to configure Nginx with a custom HTTP header 'X-Served-By'
class nginx_custom_header {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Define a file resource for the Nginx default site configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    require => Package['nginx'],
    content => template('nginx/default.erb'),
  }

  # Service resource to manage the Nginx service
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Include the nginx_custom_header class to apply the configuration
include nginx_custom_header
