from aoc_utils import get_data


def get_view_distance(current_tree: int, neighbors: list):
	"""Return the number of elements encountered in `neighbors` before one exceeds `current_tree`"""
	for idx, neighbor_tree in enumerate(neighbors):
		if current_tree > neighbor_tree:
			continue
		else:
			return idx + 1
	return len(neighbors)


def day_8():
	d = get_data("day8.txt", strip=True, astype="str")
	trees_visible_from_outside = 0
	scenic_scores = []
	for row_idx, row in enumerate(d):
		for col_idx, col in enumerate(row):
			tree_height = int(d[row_idx][col_idx])
			dist_top = row_idx
			dist_bot = len(d) - row_idx
			dist_left = col_idx
			dist_right = len(row) - col_idx
			
			trees_up = [
				int(d[row_idx-i][col_idx]) 
				for i in range(1, dist_top + 1)
			] 
			trees_down = [
				int(d[row_idx+i][col_idx])
				for i in range(1, dist_bot)
			] 
			trees_left = [
				int(d[row_idx][col_idx-i])
				for i in range(1, dist_left + 1)
			] 
			trees_right = [
				int(d[row_idx][col_idx+i])
				for i in range(1, dist_right)
			] 
			
			# Pt 1 - Is the current tree visible from outside
			is_vis_from_top = all(tree_height > i for i in trees_up)
			is_vis_from_bot = all(tree_height > i for i in trees_down)
			is_vis_from_left = all(tree_height > i for i in trees_left)
			is_vis_from_right = all(tree_height > i for i in trees_right)
			trees_visible_from_outside += any([
				is_vis_from_top, is_vis_from_bot, is_vis_from_left, is_vis_from_right
			])
			
			# Pt 2 - How many trees can the current tree see based on their height
			view_up = get_view_distance(tree_height, trees_up)
			view_down = get_view_distance(tree_height, trees_down)
			view_right = get_view_distance(tree_height, trees_right)
			view_left = get_view_distance(tree_height, trees_left)
			score = view_up * view_down * view_left * view_right
			scenic_scores.append(score)
	
	pt_1_answer = trees_visible_from_outside
	pt_2_answer = max(scenic_scores)
	
	return pt_1_answer, pt_2_answer
	
day_8()
