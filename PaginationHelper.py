# TODO: complete this class
import math
# page of values and an integer

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self._collection = collection
      self._items_per_page = items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self._collection)
  
  # returns the number of pages
  def page_count(self):
      return math.ceil((len(self._collection)/self._items_per_page))
    
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    if page_index*self._items_per_page > len(self._collection):
        return -1
    else:
        items = page_index*self._items_per_page+self._items_per_page
        num_of_items = len(self._collection)
        if items > len(self._collection):
            return self._items_per_page - (items-len(self._collection))
        else:
            return self._items_per_page
        
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    pg_index = math.floor(item_index/self._items_per_page)
    if item_index<0:
        return -1
    else:
        page_item_count = self.page_item_count(pg_index)
        if (page_item_count == -1):
            return -1
        else:
            remainder = item_index%self._items_per_page
            if remainder+1 <= page_item_count:
                return pg_index
            else:
                 return -1

