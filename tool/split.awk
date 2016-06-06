#!/usr/bin/awk -f
BEGIN {
	DEFOUTFILE = "tut2.nodoka"
	outfile = DEFOUTFILE
}
/^keymap tutcode-[^-]+-[ty]$/ {
	outfile = "tut3ty.nodoka"
	print >>outfile
	next
}
/^keymap tutcode-[^-]+-[gh]$/ {
	outfile = "tut3gh.nodoka"
	print >>outfile
	next
}
/^keymap tutcode-[^-]+-[vm]$/ {
	outfile = "tut3vm.nodoka"
	print >>outfile
	next
}
/^keymap tutcode-[^-]+-[bn]$/ {
	outfile = "tut3bn.nodoka"
	print >>outfile
	next
}
/^$/ {
	print >>outfile
	outfile = DEFOUTFILE
	next
}
{
	print >>outfile
}
