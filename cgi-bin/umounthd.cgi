#!/usr/bin/perl
use CGI qw(:standard);

charset('utf-8');

print header();
print start_html(-title=>"Irroita kiintolevy", -encoding=>"utf-8");
    
print 'Valmistellaan tikkua irroitettavaksi<br><br><br>';

open (STATUS, 'sudo umount /media/BACKUPLEVY* 2>&1 |');
    $i=1;
    while (<STATUS>){
	print $_."<br>";
	$i++;
    }
close STATUS;

print 'Jos edellä ei esiintynyt virheitä, tikku on nyt valmis irroitettavaksi';


print '<br><br><hr><br><a href="http://192.168.0.101/index.html">takaisin alkusivulle</a>';

print end_html();
