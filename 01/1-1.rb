# https://adventofcode.com/2023/day/1

puts File.open('input.txt').reduce(0){|t,l|t+l.tr('^0-9','').split('').values_at(0,-1).join('').to_i}