def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing: None {}".format(type(object)))
	elif isinstance(object, float) and object != object:
		print("Cheese: nan {}".format(type(object)))
	elif isinstance(object, bool) and object == False:
		print("Fake: {}".format(type(object)))
	elif isinstance(object, int) and object == 0:
		print("Zero: 0 {}".format(type(object)))
	elif isinstance(object, str) and len(object) == 0:
		print("Empty: {}".format(type(object)))
	else:
		print("Type not Found")
		return 1
	return 0

