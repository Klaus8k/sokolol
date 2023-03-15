from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', 'sokolol.urls', name=' '),
    host(r'dev', 'dev.urls', name='dev'),
)