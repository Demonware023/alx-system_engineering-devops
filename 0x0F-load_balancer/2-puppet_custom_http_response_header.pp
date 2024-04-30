# Updating Packages before performing installations
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  require => Package['nginx'],
}

# Installing Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

# Creating an index.html page
file { '/var/www/html/index.html':
  content => 'Hello World!',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
}

# Performing a "moved permanently redirection" (301)
$rewrite_rule = 'server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/besthor permanent;'
file_line { 'nginx_redirect_rule':
  path    => '/etc/nginx/sites-enabled/default',
  line    => $rewrite_rule,
  require => Package['nginx'],
}

# Creating a 404 Custom error page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
}

# Creating an HTTP response header
$hostname = $facts['hostname']
$custom_header = "add_header X-Served-By $hostname;"
file_line { 'nginx_custom_header':
  path    => '/etc/nginx/sites-enabled/default',
  line    => $custom_header,
  require => Package['nginx'],
}

# Testing configurations for syntax errors
exec { 'nginx_syntax_check':
  command => '/usr/sbin/nginx -t',
  path    => '/usr/sbin',
  require => Package['nginx'],
}

# Restarting Nginx after implementing changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => [
    File_line['nginx_redirect_rule'],
    File_line['nginx_custom_header'],
    Exec['nginx_syntax_check'],
  ],
  require   => [
    Package['nginx'],
    File['/var/www/html/index.html'],
    File['/var/www/html/404.html'],
  ],
}
