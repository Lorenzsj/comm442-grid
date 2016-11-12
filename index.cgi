#!/usr/bin/perl
#index.cgi

use strict;
use warnings;
use CGI;

require("grid.pm");

Grid::begin_html("Grid");
print<<EOT;
<body>
  <header>
    <h1>Grid $Grid::version</h1>
    <p>A simple forum application.</p>
  </header>
  <nav>
    <ul>
      <li><a href="index.cgi">Home</a></li>
      <li><a href="post.cgi">Post</a></li>
      <li><a href="login.cgi">Login</a></li>
      <li><a href="signup.cgi">Sign up</a></li>
    </ul>
  </nav>
  <script src="js/scripts.js"></script>
</body>
</html>
EOT
