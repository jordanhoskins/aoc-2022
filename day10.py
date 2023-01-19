from aoc_utils import get_data

class Cmd:
	def __init__(self, cycles, value):
		self.cycles = cycles
		self.value = int(value)
		
	@classmethod
	def from_line(cls, l):
		if l == "noop":
			return cls(cycles=1, value=0)
		else:
			_, val = l.split()
			return cls(cycles=2, value=val)


def day_10():
	d = get_data("day10.txt", strip=True)
	x = 1
	cyc = 0
	signal_str = {}
	crt = []
	crt_line = ""
	for line in d:
		sprite = {x-1, x, x+1}
		cmd = Cmd.from_line(line)
		for _ in range(cmd.cycles):
			crt_line += "#" if len(crt_line) in sprite else "."
			cyc += 1 
			signal_str[cyc] = cyc * x
			if len(crt_line) == 40:		
				crt.append(crt_line)
				crt_line = ""
		x += cmd.value
		
	pt_1_ans = sum([signal_str[20], signal_str[60], signal_str[100], signal_str[140], signal_str[180], signal_str[220]])
	pt_2_ans = crt
	
	return pt_1_ans, pt_2_ans
	
	
print(day_10())