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


Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
Grid::Network::sign_in($username, $password);
print <<EOT;
  <nav>
    <ul>
      <li><a href="index.cgi">Home</a></li>
      <li><a href="post.cgi">Post</a></li>
      <li><a href="login.cgi">Login</a></li>
      <li><a href="signup.cgi">Sign up</a></li>
    </ul>
  </nav>
  <form method="POST" action="login.cgi">
    <input type="text" name="username" required>
    <input type="text" name="password" required>
    <input type="submit">
  </form>
  <script src="js/scripts.js"></script>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
