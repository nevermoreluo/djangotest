  APP对接接口  
数据格式：  
数据采用JSON格式进行传输，UTF-8编码  

访问方式：  
访问路径为：{域名}/{方法名}/?{参数1}={值1}[&{参数2}={值2}]  

请求方式：  
GET查询接口数据,  
POST新增一个数据,  
PUT修改一个已有数据,  
DELETE删除一个数据  
`另外支持OPTIONS方法`  

API接口获取域名 http://222.73.0.213:8300/  

## 目录
 [1.User](#1users) `GET, POST, PUT, DELETE` 增删该查User,还在debug  
 [2.Room](#2rooms) `GET, POST, PUT, DELETE`  增删该查Room 

------------------

### 1. Users
...

------------------

### 2.Rooms  
请求方式： `GET`  
方法名： rooms  
ex：http://222.73.0.213:8300/rooms/?page=1
查询所有开启的房间  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| page | string | 选填 | 查询的页码，默认为1 |
| pageSize | string | 选填 | 每页返回的room数量，默认为30 |

请求样例：
ex：http://222.73.0.213:8300/rooms/?page=1&pageSize=3

返回参数：  

| 字段 | 类型 | 说明 |
| ------| ------ | ------ |
| pageSize | string | 返回房间的数量 |
| currentPage  | string | 当前页 |
| totalPage | string | 总页数 |
| total | string | 总记录条数 |
| results | list | 结果集 |
| id | string | server后台存储的唯一标识 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |
| user | string | 还在开发中，暂时为空 |

数据样例：  
```
成功返回：200
{
    "status": "SUCCESS",
    "code": "200",
    "pageSize": "30",
    "currentPage": "1",
    "totalPage": "1",
    "total": "2",
    "results": [
        {
            "id": "1",
            "roomid": "1262",
            "mcuser": null,
            "active": true
        },
        {
            "id": "2",
            "roomid": "1263",
            "mcuser": null,
            "active": true
        }
    ]
}

```

请求方式： `GET`  
方法名： rooms  
查询一个房间的信息  
ex：http://222.73.0.213:8300/rooms/1/

请求参数：  
无  

返回参数：  

| id | string | server后台存储的唯一标识 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |
| user | string | 还在开发中，暂时为空 |

数据样例：  
```
成功返回：200
{
  "status": "SUCCESS",
  "code": "200",
  "id": "1",
  "roomid": "1262",
  "mcuser": null,
  "active": true
}
```


请求方式： `POST`  
方法名： rooms  
修改一个房间的信息  
ex：http://222.73.0.213:8300/rooms/
请求格式： json
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| roomid | string | 必填 | 房间号 |
| active | boolen | 选填 | 房间是否开启 |
| user | string | 选填 | 还在开发中，暂时为空 |

请求样例：
```
{
    "roomid": "1263",
    "active": true
}
```

返回参数：  

| 字段 | 类型 | 说明 |
| ------| ------ | ------ |
| id | string | server后台存储的唯一标识 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |
| user | string | 还在开发中，暂时为空 |

数据样例：  
```
返回：201
{
  "status": "SUCCESS",
  "code": "201",
  "id": "1",
  "roomid": "1262",
  "mcuser": null,
  "active": true
}
```

请求方式： `PUT`  
方法名： rooms  
修改一个房间的信息  
ex：http://222.73.0.213:8300/rooms/1/
请求格式： json
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| roomid | string | 必填 | 房间号 |
| active | boolen | 选填 | 房间是否开启 |
| user | string | 选填 | 还在开发中，暂时为空 |

请求样例：
```
{
    "roomid": "1263",
    "active": true
}
```

返回参数：  

| 字段 | 类型 | 说明 |
| ------| ------ | ------ |
| id | string | server后台存储的唯一标识 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |
| user | string | 还在开发中，暂时为空 |

数据样例：  
```
返回：200
{
  "status": "SUCCESS",
  "code": "200",
  "id": "1",
  "roomid": "1262",
  "mcuser": null,
  "active": true
}
```

请求方式： `DELETE`  
方法名： rooms  
修改一个房间的信息  
ex：http://222.73.0.213:8300/rooms/1/

返回参数：  
无

数据样例：  
```
返回：204

```


