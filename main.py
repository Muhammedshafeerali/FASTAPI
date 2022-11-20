# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# import uvicorn



# myapp=FastAPI()

# class Blog(BaseModel):
#     title: str
#     body: str
#     Published: Optional[bool]

 
# @myapp.get("/blog")
# def read_root(limit:int=10,published:bool=True,sort:Optional[str]=None):

#     return {"data":f"limit value {limit} and pulished {published}and sor{sort}"}

# @myapp.post("/blog")
# def create_blog(request:Blog):
#     return{"data":f"Blog creted with title {request.title} "}

# @myapp.get("/item/list")
# def item_lst():
#     return {"data":"list data presentiong"}
 
# @myapp.get("/item/{item_id}")
# def read_item(item_id:int,q:Union[str,None]=None):
#     return {"item_id":item_id,"q":q}

# # @myapp.put("/item/{item_id}")
# # def update_item(item_id:int,item: Item):
# #     return {"item_name": item.name, "item_id": item_id}

# if __name__=="__main__":
#     uvicorn.run(myapp,host='127.0.0.1',port=9000)







 