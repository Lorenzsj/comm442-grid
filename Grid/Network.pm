#!/usr/bin/perl
package Grid::Network;

use lib "/home/stevie/perl5/lib/perl5/";
use strict;
use warnings;
use Grid::Database;
use CGI;
use CGI::Session;
#se CGI::Session::Auth;

my $session = new CGI::Session();

sub sign_in {
  my $username = $_[0] // "";
  my $password = $_[1] // "";

  #Grid::Database::connect_database();

  if ($username eq "") {
    return "Please enter your username and password.";
  }

  if ($username =~ Grid::Database::get_username) {
    if ($password =~ Grid::Database::get_password) {
      return "Welcome <b>$username</b>.";
    }
    else {
      return "Invalid password.";
    }
  }
  else {
    #print redirect(-url=>'Location: signup.cgi');
    return "Username does not exist.";
  }
}

sub sign_out {
  Grid::Database::disconnect_database();
}

1;
