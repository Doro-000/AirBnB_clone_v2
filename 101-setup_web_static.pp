# sets up web servers for the deployment of web_static

$whisper_dirs = [ '/data/', '/data/web_static/',
                  '/data/web_static/releases/',
                  '/data/web_static/shared/',
                  '/data/web_static/releases/test/'
                  ]
$s = "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

package {'nginx':
  ensure  => installed,
}

file { $whisper_dirs:
        ensure  => 'directory',
        owner   => 'ubuntu',
        group   => 'ubuntu',
        recurse => 'remote',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Holberton School for the win!',
}

file_line {'deploy static':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => $s,
}

service {'nginx':
  ensure  => running,
}
