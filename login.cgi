#!/usr/bin/perl

use strict;
use warnings;
use CGI;

require("mylib.pl");

my $query = CGI->new;

my $username = $query->param('username');
my $password = $query->param('password');

my $message #debug variable
if ($username =~ /stephen/ and $password =~ /lorenz/) {$message = "Welcome " . $username;}

begin_html("Login");
print<<EOT;
<body>
  <header>
    <h1>Grid 0.1.0</h1>
    <p>A simple forum application.</p>
  </header>
  <nav>
    <ul>
      <li><a href="home.cgi">Home</a></li>
      <li><a href="post.cgi">Post</a></li>
      <li><a href="login.cgi">Login</a></li>
      <li><a href="signup.cgi">Sign up</a></li>
    </ul>
  </nav>
  <script src="js/scripts.js"></script>
</body>
</html>
EOT
