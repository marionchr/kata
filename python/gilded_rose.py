# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        item_values={"+5 Dexterity Vest": [1,1] , "Aged Brie":[-1,1] , "Elixir of the Mongoose":[1,1] , "Sulfuras, Hand of Ragnaros":[0,0] , "Backstage passes to a TAFKAL80ETC concert":[0,1], "Conjured Mana Cake":[2,1]}        
        for item in self.items:      
            item.quality = item.quality - item_values[item.name][0]                      
            if item.quality < 50 and item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality + 1                
                if item.sell_in <= 10 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in <= 5 and item.quality < 50:
                    item.quality = item.quality + 1          
            if item.sell_in <= 0 and item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality = item.quality + 1 
                else: 
                    item.quality = 50              
            elif item.sell_in <= 0 and not "Sulfuras" in item.name:
                item.quality = 0                         
            item.sell_in = item.sell_in - item_values[item.name][1]                                                             

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
