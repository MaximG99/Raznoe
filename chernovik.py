class Produkts:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0)
        self.name = name.strip
        if not len(self.hame)>-2:
            raise ValueError("Название товара должно быть 2 символа и более")
        self.price = abc(float(price))
        self.discount = abc(float(discount))
        self.stock = abc(int(stock))
        self.max_discount = abc(float(max_discount))
        if self.max_discount > 99:
            raise ValueError("Слишком большая скидка на товар этой категории")
        if self.discount > self.max_discount:
        self.discount = self.max_discount 
    
       