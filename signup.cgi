#!/usr/bin/perl

use strict;
use warnings;
use lib "/home/stevie/perl5/lib/perl5/";
use Grid::HTML5;
use CGI;

my $query = CGI->new;

Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Sign up</h2>";
print <<EOT;
  <p>Under construction</p>
  <form method="POST" action="signup.cgi">
    <input type="text" name="username" required>
    <input type="text" name="password" required>
    <input type="submit">
  </form>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
