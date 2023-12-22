#create a manifest that kills a process named killmenow
exec { 'killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
}
