# executes a command
exec { 'kill' :
    command => 'pkilll -f killmenow',
    path    => ['/usr/bin', '/usr/sbin']
}

