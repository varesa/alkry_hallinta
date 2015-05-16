#!/usr/bin/perl
use CGI qw(:standard);

charset('utf-8');

print header();
print start_html(-title=>"Varmuuskopioi", -encoding=>"utf-8");
    
open (STATUS, 'sudo ./vtigerbackup_hdd 2>&1 |');
    $i=1;
    while (<STATUS>){
	print $_."<br>";
	$i++;
    }
close STATUS;

print '<br><br><hr><br><a href="http://192.168.0.101/index.html">takaisin alkusivulle</a>';

print end_html();
