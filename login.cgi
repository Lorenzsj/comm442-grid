#!/usr/bin/perl

use strict;
use warnings;
use lib "/home/stevie/perl5/lib/perl5/";
use Grid::HTML5;
use Grid::Network;
use CGI;

my $query = CGI->new;

my $username = $query->param('username');
my $password = $query->param('password');

my $network = Grid::Network::sign_in($username, $password);

#print "<img src=\"/home/stevie/public_html/grid/data/img/logo.png\">";
Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Sign in</h2>";
print <<EOT;
  <p>$network</p>
  <form method="POST" action="login.cgi">
    <input type="text" name="username" required>
    <input type="text" name="password" required>
    <input type="submit">
  </form>
  <script src="js/scripts.js"></script>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
