#manifest that kills a process named killmenow
exec { 'killmenow':
  commande => 'pkill killmenow',
  path     => '/bin/',
}
