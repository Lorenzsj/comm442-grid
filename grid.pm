#!/usr/bin/perl
package Grid;

use strict;
use warnings;
use DBI;
use Time::Piece;

# MySQL database configuration


# Global variables
our $version = "0.1.0";

# Package variables
my $dbh;

#** @function public begin_html($title, $about, $author, $style, $script)
# @brief Print the HTML5 <head>.
#
# Under construction. Used to dynamically generate the HTML5 head.
# @params $title  String. Sets <title> tag.
# @params $about String. Sets <title> tag.
# @params $author String. Sets <title> tag.
# @params $style String. Path to a  .css file tag.
# @params $script String. Path to a .js file.
#*.

sub begin_html {
    my $title  = $_[0];
    my $about  = $_[1] // "Grid $version";
    my $author = $_[2] // "Stephen Lorenz";
    my $style  = $_[3] // "css/styles.css?v=1.0";
    my $script = $_[4] // "js/scripts.js";

    print <<EOT;
Content-type: text/html

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>$title</title>
<meta name="description" content="$about">
<meta name="author" content="$author">

<link rel="stylesheet" href="$style">
<script src="$script"></script>

<!--[if lt IE 9]>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
<![endif]-->
</head>
EOT
}

#** @function public end_html()
# @brief Print the HTML <footer>.
#
# Under construction. Used to dynamically generate HTML5 footers.
#*.
sub end_html {
    my $year = localtime()->year;

    print <<EOT;
    <footer>
      <p>In development. $year</p>
      <nav>
        <ul>
          <li><a href="about.cgi">About</a></li>
          <li><a href="contact.cgi">Contact</a></li>
        </ul>
      </nav>
    </footer>
</html>
EOT
}

#** @function public generate_header()
# @brief Print a generic <header>.
#
# Under construction.Used to dynamically generate HTML5 headers.
#*.
sub generate_header {
  my $title = $_[0] // "Grid $version";
  my $about = $_[1] // "A simple forum application.";

  print <<EOT;
  <header>
    <h1>$title</h1>
    <p>$about</p>
  </header>
EOT
}

sub connect_database {
  my $dsn = "DBI:mysql:grid";
  my $username = "root";
  my $password = '';

  my %attr = (PrintError=>0, RaiseError=>1);
  my $dbh  = DBI->connect($dsn, $username, $password, \%attr);
}

sub disconnect_databse {
  $dbh->disconnect();
}

1
