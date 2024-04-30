# Puppet manifest to configure Nginx with a custom HTTP header 'X-Served-By'
# 2-puppet_custom_http_response_header.pp
node default {
  class { 'nginx': }

  $hostname = $::hostname

  nginx::resource::server { $hostname:
    listen_port => 80,
    www_root => '/var/www/html',
    index_files => ['index.html'],
    autoindex => 'on',
    use_default_location => false,
    location_cfg_append => {
      'add_header' => "X-Served-By $hostname",
    },
    locations => {
      '/' => {
        location => '/',
        www_root => '/var/www/html',
      },
    },
  }
}
