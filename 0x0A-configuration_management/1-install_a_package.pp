# Ensure Flask version 2.1.0 is installed using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Update the Werkzeug library if necessary
package { 'werkzeug':
  ensure   => 'latest',
  provider => 'pip3',
  require  => Package['Flask'],
}
