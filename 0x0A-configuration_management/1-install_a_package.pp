# Install puppet-lint version 2.5.0
package { 'puppet-lint':
    ensure => '2.5.0',
    provider => 'apt',
    require => Exec['update apt'],
}

exec { 'update apt':
    command => '/usr/bin/apt-get update',
    refreshonly => true,
}
