from aoc_utils import get_data
from typing import NamedTuple

class AOCFile(NamedTuple):
	name: str
	size: int
	

def change_dir(cur_dir, dest):
	"""Does not check if directory exists"""
	if dest == "/": 
		return ["/"]
	elif dest == "..":
		cur_dir = cur_dir[:len(cur_dir)-1]
	else:
		cur_dir.append(dest)
	return cur_dir

	
def get_cd_string(cur_dir_list):
	if cur_dir_list == ["/"]:
		cd_string = "/"
	else:
		cd_string = "/".join(cur_dir_list)[1:]
	return cd_string


def day_7():
	d = [i.strip() for i in get_data("day7.txt")]
	cur_dir = []
	directory_memory = {}
	all_files = set()
	for idx, i in enumerate(d):
		if i.startswith("$ cd"):
			dest = i.replace("$ cd ", "")
			cur_dir = change_dir(cur_dir=cur_dir, dest=dest)
			cd_string = get_cd_string(cur_dir)
			if cd_string not in directory_memory:
				directory_memory[cd_string] = {
					"total_size": 0, 
					"parents": cur_dir[:-1]
				}

		elif i.startswith("$ ls"):
			# listed files are lines after the current index until one starts with "$"
			next_lines = []
			for line in d[idx+1:]:
				next_lines.append(line.split())
				if line.startswith("$"):
					break
			files = [
				AOCFile(name=l[1], size=int(l[0])) 
				for l in next_lines 
				if l[0].isdigit()
			]
			# Update size of directory and its parents if file has not been encountered before
			for file in files:
				full_path = cd_string + file.name
				if full_path not in all_files:
					all_files.add(full_path)
					parent_to_update = []
					for subdir in cur_dir:
						parent_to_update.append(subdir)
						path = get_cd_string(parent_to_update)
						directory_memory[path]["total_size"] += file.size
	
	# part 1 - sum of directories whose size is <= 100k		
	at_most_100k = {
		k: v for k, v in directory_memory.items() 
		if v["total_size"] <= 100000
	}
	pt_1_answer = sum(
		v["total_size"] for k, v in at_most_100k.items()
	)
	
	# part 2 - Size of smallest directory which would free up 
	# at least 30M
	total_mem = 70000000
	available_mem = total_mem - directory_memory["/"]["total_size"]
	needed_mem = 30000000 - available_mem
	
	at_least_size_of_needed_mem = {
		k: v for k, v in directory_memory.items() 
		if v["total_size"] >= needed_mem
	}
	pt_2_answer = min(
		v["total_size"] for 
		k,v in at_least_size_of_needed_mem.items()
	)
	return pt_1_answer, pt_2_answer

	
print(day_7())
