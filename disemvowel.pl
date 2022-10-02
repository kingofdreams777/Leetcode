#!/usr/bin/perl
use strict;
use warnings;

my @vowels = ("a","e","i","o","u","A","E","I","O","U");

# my $input = "quick brown fox";
my $input = "@ARGV";
$input =~ tr/aeiouAEIOU//d;
print $input;

# foreach my $c ($input){
#     foreach my $v (@vowels){
#         if ($c eq $v){
#             print $c
#             next;
#         }
#     }
#     push @res, $c;

# }