#!/usr/bin/perl
package Grid::Network;

use lib "/home/stevie/perl5/lib/perl5/";
use strict;
use warnings;
use CGI;
use CGI::Session;
use CGI::Session::Auth;

sub sign_in {
  my $username = ARGV[0];
  my $password = ARGV[1];
  
  if ($username =~ /stephen/ and $password =~ /lorenz/) {
    $message = "Welcome $username";
  }
}

sub sign_out {

}

1;
