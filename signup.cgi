#!/usr/bin/perl

use strict;
use warnings;
use CGI;

require("grid.pm");

my $query = CGI->new;

my $username = $query->param('username');
my $password = $query->param('password');

my $message; #debug variable
if ($username =~ /stephen/ and $password =~ /lorenz/) {
  $message = "Welcome $username";
}

Grid::begin_html("Sign up");
print<<EOT;
<body>
  @{[Grid::generate_header()]}
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
  $message
  <script src="js/scripts.js"></script>
</body>
EOT
Grid::end_html();
