#!/usr/bin/awk -f
BEGIN {
	DEFOUTFILE = "tut2.nodoka"
	outfile = DEFOUTFILE
}
/^keymap TUT-Code-[^-]+-[ty]$/ {
	outfile = "tut3ty.nodoka"
	print >>outfile
	next
}
/^keymap TUT-Code-[^-]+-[gh]$/ {
	outfile = "tut3gh.nodoka"
	print >>outfile
	next
}
/^keymap TUT-Code-[^-]+-[vm]$/ {
	outfile = "tut3vm.nodoka"
	print >>outfile
	next
}
/^keymap TUT-Code-[^-]+-[bn]$/ {
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
