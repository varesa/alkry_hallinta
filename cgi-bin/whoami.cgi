#!/usr/bin/perl
use CGI qw(:standard);

charset('utf-8');

print header();
print start_html(-title=>"Sammuta kone", -encoding=>"utf-8");

open (STATUS, 'whoami 2>&1 |');
    $i=1;
    while (<STATUS>){
	print $_."<br>";
	$i++;
    }
close STATUS;



print end_html();
