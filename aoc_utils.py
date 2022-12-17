def get_data(path, astype="int", strip=False):
	with open(path) as ifp:
		if strip:
			d = [l.strip() for l in ifp]
		else:
			d = [l for l in ifp]
	if astype == "int":
		new = []
		for i in d:
			try:
				i = int(i)
				new.append(i)
			except:
				new.append(i)
		return new
	return d
