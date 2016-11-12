#!/usr/bin/perl
#index.cgi

use strict;
use warnings;
use CGI;

require("mylib.pl");

begin_html("Grid");
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
