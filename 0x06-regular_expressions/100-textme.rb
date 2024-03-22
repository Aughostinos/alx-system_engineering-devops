#!/usr/bin/env ruby
puts ARGV[0].scan(/(to|from|flags)\W\W\d+\W\d?\W\d?\W\d?\W\d?\W\d?\W\d?/).join
