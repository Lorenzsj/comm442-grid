#!/usr/bin/perl
package Grid::Database;

use strict;
use warnings;
use lib "/home/stevie/perl5/lib/perl5/";
use DBI;

# Package variables
my $dbh;

#** @function public connect_database()
# @brief Open a connection to the MySQl database.
#
# Under construction. Connect to the MySQL database as root.
#*.
sub connect_database {
  my $dsn = "DBI:mysql:grid";
  my $username = "root";
  my $password = '';

  my %attr = (PrintError=>0, RaiseError=>1);
  my $dbh  = DBI->connect($dsn, $username, $password, \%attr);
}

#** @function public connect_database()
# @brief Closes a connection to the MySQl database.
#
# Under construction. Disconnect from the MySQL database.
#*.
sub disconnect_databse {
  $dbh->disconnect();
}

1;
