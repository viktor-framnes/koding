import tkinter as tk

class MoveCanvas(tk.Canvas):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.x = 15
		self.y = 15
		self.dx = 0
		self.dy = 0
		self.ds = 3

		self.box = self.create_rectangle(5, 5, 15, 15, fill="black")

		self.dt = 25
		self.tick()
	
	def tick(self):
		self.x += self.dx
		self.y += self.dy
		self.move(self.box, self.dx, self.dy)
		self.sjekkKolisjon()
		self.after(self.dt, self.tick)

	def sjekkKolisjon(self):
		if self.x >= 300:
			self.move(self.box,-self.dx,self.dy)
			self.x += self.dx
			self.y += self.dy
			self.change_heading(-self.ds,0)

		if self.y >= 300:
			self.move(self.box,self.dx,-self.dy)
			self.x += self.dx
			self.y += self.dy
			self.change_heading(0,-self.ds)


	def change_heading(self, dx, dy):
		self.dx = dx
		self.dy = dy


if __name__ == "__main__":

	root = tk.Tk()
	root.geometry("300x300")


	cvs = MoveCanvas(root)
	cvs.pack(fill="both", expand=True)

	ds = 3

	root.bind("<KeyPress-Left>", lambda _: cvs.change_heading(-ds, 0))
	root.bind("<KeyPress-Right>", lambda _: cvs.change_heading(ds, 0))
	root.bind("<KeyPress-Up>", lambda _: cvs.change_heading(0, -ds))
	root.bind("<KeyPress-Down>", lambda _: cvs.change_heading(0, ds))
	
	root.mainloop()
