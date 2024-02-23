#manifest that kills a process named killmenow
exec { 'killmenow':
  path     => '/bin/',
  commande => 'pkill killmenow',
}
