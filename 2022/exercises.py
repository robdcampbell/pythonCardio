import math


# length of a line, give two graph positions in ascending order.
def line_length(dot1, dot2):
	return round(math.sqrt( math.pow(dot2[0]-dot1[0], 2) + math.pow(dot2[1]-dot1[1], 2)),2)