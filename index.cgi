#!/usr/bin/perl

use strict;
use CGI;

require("mylib.pl");

begin_html("Home");
print<<EOT;
<body>
  <script src="js/scripts.js"></script>
</body>
</html>
EOT
