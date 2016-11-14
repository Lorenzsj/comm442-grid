#!/usr/bin/perl
package Grid::Network;

use lib "/home/stevie/perl5/lib/perl5/";
use strict;
use warnings;
use Grid::Database;
#use CGI;
#use CGI::Session;
#use CGI::Session::Auth;

sub sign_in {
  my $username = $_[0];
  my $password = $_[1];

  if ($username =~ Grid::Database::get_username and Grid::Database::get_password) {
    print "Welcome " . Grid::Database::get_username;
  }

}

sub sign_out {

}

1;
