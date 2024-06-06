file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

exec { 'fix-apache':
  command => '/path/to/your/fix/script.sh',
  path    => ['/usr/bin', '/usr/sbin'],
}

