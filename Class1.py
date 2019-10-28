class Market:
  def __init__(self, wood, stone):
    self.wood = wood
    self.stone = stone

Market1 = Market(2, 2)

def Market1_buy(x,y):
  if x >= Market1.wood and y >= Market1.stone:
    print("Buy!")
  else:
    print("Too expensive!")

Market1_buy(2,1)

