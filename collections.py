#namedtuple help reduce the chance for error through immutability
import collections

foo = collections.namedtuple("foo", [
		'age'
		'name'
		'colour'
	])

