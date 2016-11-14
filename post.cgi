#!/usr/bin/perl

use strict;
use warnings;
use lib "/home/stevie/perl5/lib/perl5/";
use Grid::HTML5;
use CGI;

Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Post</h2>";
print <<EOT;
  <p>Under construction</p>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
