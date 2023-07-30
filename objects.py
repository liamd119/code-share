class StrList(list):
	"""A list child that implements casting to strings differently to parent, and implements some extra methods.

	Examples:
		Create a new StrList instance:
			new = StrList([1,2,"text"])
		Cast a StrList instance to a CSV string, called using the normal string casting function:
			str(new)  # -> '1, 2, text'
	"""

	def __str__(self):
		"""Important: Is recursive when called on a StrList containing StrList(s)."""
		output = []
		for str_list_item in self:
			if type(str_list_item) == StrList:
				str_list_item = str(str_list_item)
			# when 'self' contains another 'StrList' instance, recursively casts that instance to string
			output.append(str(str_list_item))
		return ", ".join(output)

	@property
	def string_items(self):
		"""StrList with the items cast to strings."""
		return StrList(map(str, self))

	@property
	def list(self) -> list:
		"""List equivalent of StrList instance."""
		return list(self)
