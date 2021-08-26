# sets up web servers for the deployment of web_static
$s = "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

exec {'/usr/bin/apt-get update':
}

package {"nginx":
  ensure  => installed,
}

exec { "mkdir -p /data/web_static/releases/test/":
  path => ['/bin', '/usr/bin', '/usr/sbin',],
}

exec { "mkdir -p /data/web_static/shared/":
  path => ['/bin', '/usr/bin', '/usr/sbin',],
}

exec { "chown -hR ubuntu:ubuntu /data/":
  path => ['/bin', '/usr/bin', '/usr/sbin',],
}

file { "/data/web_static/current":
  ensure => link,
  target => "/data/web_static/releases/test/",
}

file {"/data/web_static/releases/test/index.html":
  ensure  => present,
  content => 'Holberton School for the win!',
}

file_line {'deploy static':
  path  => "/etc/nginx/sites-available/default",
  after => 'server_name _;',
  line  => $s,
}

service {'nginx':
  ensure  => running,
}
