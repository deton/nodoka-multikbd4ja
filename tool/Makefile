all: tut.nodoka tut2.nodoka tut3ty.nodoka tut3gh.nodoka tut3vm.nodoka tut3bn.nodoka

tut.nodoka: tutcode.2 tutcode.3
	cat tutcode.? | python mk4nodoka.py tutcode >tut.nodoka

tut2.nodoka tut3ty.nodoka tut3gh.nodoka tut3vm.nodoka tut3bn.nodoka: tut.nodoka
	LANG=C /usr/bin/gawk -f split.awk tut.nodoka

clean:
	-rm -f tut.nodoka tut2.nodoka tut3ty.nodoka tut3gh.nodoka tut3vm.nodoka tut3bn.nodoka
