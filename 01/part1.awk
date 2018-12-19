#!/usr/bin/awk -f

BEGIN {
    i = 0
}

{
    i += $0
}

END {
    print "the sum is: " i
}
