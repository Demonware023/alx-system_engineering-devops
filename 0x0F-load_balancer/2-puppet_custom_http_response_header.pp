# Puppet manifest to configure Nginx with a custom HTTP header 'X-Served-By'
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

# Configure Nginx virtual host with custom HTTP header
nginx::resource::vhost { 'default':
  ensure      => present,
  www_root    => '/var/www/html',
  server_name => $::hostname, # Use the hostname of the server
  custom_fragment => "
    add_header X-Served-By $::hostname;
  ",
}

# Ensure index.html file exists
file { '/var/www/html/index.html':
  content => 'Hello World!',
}
