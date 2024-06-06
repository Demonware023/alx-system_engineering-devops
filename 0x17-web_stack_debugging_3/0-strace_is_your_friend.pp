file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  command => '/path/to/your/fix/script.sh',
  path    => ['/usr/bin', '/usr/sbin'],
  mode    => '0755',
  recurse => true,
}
