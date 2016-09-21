## 目录
 *[1.PnListHandler]*(#PnListHandler)  
 *[2.ApisHandler]*(#ApisHandler)  
 *[3.PnHandler]*(PnHandler) 
 



### PnListHandler

#### `GET` http://127.0.0.1:8000

```
Headers 
Tan14-Key: 必选，tan14key
```

接受可选数据without_channels=true，即不返回channels数据，提升查询速度，EX：  

>`GET` http://if.tan14.cn/mc/useful/pnlist?without_channels=true



return results
