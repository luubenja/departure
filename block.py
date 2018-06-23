class Block:
	def __init__(self,num, offset_x,offset_y, top, right, left, btm):
		self.num = num
		self.offset_x = offset_x #position in the block where the edge is
		self.offset_y = offset_y #position in the blokc where the edge is
		
		self.top_edge = top
		self.right_edge = right
		self.left_edge = left
		self.btm_edge = btm

