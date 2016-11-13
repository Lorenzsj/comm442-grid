#!/usr/bin/perl

use strict;
use warnings;
use lib "/home/stevie/perl5/lib/perl5/";
use Grid::HTML5;

Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print <<EOT;
  <nav>
    <ul>
      <li><a href="index.cgi">Home</a></li>
      <li><a href="post.cgi">Post</a></li>
      <li><a href="login.cgi">Login</a></li>
      <li><a href="signup.cgi">Sign up</a></li>
    </ul>
  </nav>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
