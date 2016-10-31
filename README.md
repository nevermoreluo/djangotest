  APP对接接口  
数据格式：  
数据采用JSON格式进行传输，UTF-8编码  

访问方式：  
访问路径为：{域名}/{方法名}/?{查询参数1}={值1}[&{查询参数2}={值2}]  

请求方式：  
GET查询接口数据,  
POST新增一个数据,  
PUT修改一个已有数据,  
DELETE删除一个数据  
`另外支持OPTIONS方法`  

API接口获取域名 http://222.73.0.213:8300/  

## 目录  
 [1.Register](#1register) `POST` 普通注册  
 [2.SnsLogin](#2snslogin) `POST` 第三方登录  
 [3.Login](#3login) `POST` 普通登录  
 [4.Logout](#4logout) `POST` 注销  
 [5.Room](#5rooms) `GET, POST, PUT, DELETE`  增删改查Room  
 [6.UserIcon](#6usericon) `PUT` 修改用户头像,`待修改为二进制流读取头像信息`  
 [7.UserPassword](#7userpassword) `PUT` 修改密码  
 [8.UserInfo ](#8userinfo) `PUT` 修改用户基本信息  
 [9.PhoneCaptcha](#9phonecaptcha) `POST` 手机验证码生成接口  
 [10.PhoneLogin](#10phonelogin) `GET` 手机验证码登录接口  

------------------

### 1. Register  
普通注册  
请求方式： `POST`  
方法名： users  
ex: http://222.73.0.213:8300/users/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| username | string | 必填 | 用户名 |
| password | string | 必填 | 密码 |
| nickname | string | 必填 | 昵称 |
| sex | string | 选填 | 0:男,1:女,2:未知 |
| age | string | 选填 | 年龄 |
| email | string | 选填 | email |
| phone | string | 选填 | 手机 |
| country | string | 选填 | 国家 |
| province | string | 选填 | 省/直辖市 |
| city | string | 选填 | 市 |
| career | string | 选填 | 职业 |


返回参数：

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| password | string | 加密后密码 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token |

数据样例：  
```
成功返回：200
{
  "pk": "1",
  "username": "12345",
  "password": "00faa0de2651c8b54e5ab54173cda706",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "1",
  "nickname": "never",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.jpg",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "创建成功",
  "code": "200"
}

```
------------------

### 2.Snslogin  
第三方登录  
请求方式： `POST`  
方法名： snslogin  
ex: http://222.73.0.213:8300/snslogin/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| username | string | 必填 | 用户名 |
| nickname | string | 必填 | 昵称 |
| login_type | string | 必填 | 登录类型:0.普通,1.微信,2.QQ,3.微博 |
| snsid | string | 必填 | 第三方唯一码 |
| access_token | string | 必填 | 第三方登录口令 |
| icon | string | 必填 | 第三方头像地址 |
| sex | string | 选填 | 0:男,1:女,2:未知 |
| age | string | 选填 | 年龄 |
| email | string | 选填 | email |
| phone | string | 选填 | 手机 |
| country | string | 选填 | 国家 |
| province | string | 选填 | 省/直辖市 |
| city | string | 选填 | 市 |
| career | string | 选填 | 职业 |


返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| password | string | 加密后密码 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token |

数据样例：  
```
成功返回：第一次第三方登录用户status_code返回201,其余返回200
{
  "pk": "2",
  "username": "12345",
  "password": "",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "1",
  "nickname": "never",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.jpg",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "登录成功",
  "code": "200"
}
```

------------------

### 3.Login  
普通登录  
请求方式： `POST`  
方法名： snslogin  
ex: http://222.73.0.213:8300/login/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| username | string | 必填 | 用户名 |
| password | string | 必填 | 密码 |

返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| password | string | 加密后密码 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |

数据样例：  
```
{
  "pk": "1",
  "username": "12345",
  "password": "",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "0",
  "nickname": "neverluo",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.jpg",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "登录成功",
  "code": "200"
}
```

------------------

### 4.Logout  
注销  
请求方式： `POST`  
方法名： snslogin  
ex: http://222.73.0.213:8300/logout/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| token | string | 必填 | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |

返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |



------------------

### 5.Rooms  
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
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pageSize | string | 返回房间的数量 |
| currentPage  | string | 当前页 |
| totalPage | string | 总页数 |
| total | string | 总记录条数 |
| results | list | 结果集 |
| pk | string | server后台存储的唯一标识 |
| room_alias | string | 与roomid对应的标识 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |

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
            "pk": "1",
            "roomid": "1263",
            "room_alias": "1262",
            "active": true
        }
    ]
}

```

请求方式： `GET`  
方法名： rooms  
查询一个房间的信息  
ex：http://222.73.0.213:8300/rooms/1/ `1是room的pk` 

请求参数：  
无  

返回参数：  

| 字段 | 类型 | 说明 |
| ------| ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | server后台存储的唯一标识 |
| room_alias | string | 房间标识与roomid对应 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |

数据样例：  
```
成功返回：200
{
  "status": "SUCCESS",
  "code": "200",
  "pk": "1",
  "roomid": "1263",
  "room_alias": "1262",
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
| room_alias | string | 必填 | 房间标识与roomid对应 |
| active | boolen | 选填 | 房间是否开启 |

请求样例：  
```
{
    "room_alias": "1262",
    "active": true
}
```

返回参数：  

| 字段 | 类型 | 说明 |
| ------| ------ | ------ |
| pk | string | server后台存储的唯一标识 |
| room_alias | string | 房间标识与roomid对应 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |

数据样例：  
```
返回：201
{
  "status": "SUCCESS",
  "code": "201",
  "pk": "1",
  "roomid": "1263",
  "room_alias": "1262",
  "active": true
}
```

请求方式： `PUT`  
方法名： rooms  
修改一个房间的信息  
ex：http://222.73.0.213:8300/rooms/1/  `1是room的pk`  
请求格式： json  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| active | boolen | 选填 | 房间是否开启 |

请求样例：  
```
{
    "active": true
}
```

返回参数：  

| 字段 | 类型 | 说明 |
| ------| ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | server后台存储的唯一标识 |
| room_alias | string | 房间标识与roomid对应 |
| roomid | string | 房间号 |
| active | boolen | 房间是否开启 |

数据样例：  
```
返回：200
{
  "status": "SUCCESS",
  "code": "200",
  "pk": "1",
  "roomid": "1263",
  "room_alias": "1262",
  "active": true
}
```

请求方式： `DELETE`  
方法名： rooms  
修改一个房间的信息  
ex：http://222.73.0.213:8300/rooms/1/ `1是room的pk` 

返回参数：  
无  

数据样例：  
```
返回：204

```
------------------

### 6.UserIcon  
修改用户头像  
请求方式： `PUT`  
方法名： users/icon  
ex: http://222.73.0.213:8300/users/icon/1/ `1是用户的pk`  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| icon | string | 必填 | 下载url |
| token | string | 必填 | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |

返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |

数据样例：  
```
返回：200
{
  "pk": "1",
  "username": "12345",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "1",
  "nickname": "never",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.png",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "修改成功",
  "code": "200"
}
```

------------------

### 7.UserPassword  
修改用户密码  
`注意修改用户密码将导致原有token失效，用户需重新登录获取新的token`  
请求方式： `PUT`  
方法名： users/password  
ex: http://222.73.0.213:8300/password/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| username | string | 必填 | 用户名 |
| old_password | string | 必填 | 旧密码 |
| password | string | 必填 | 新密码 |
| token | string | 必填 | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |


返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| password | string | 密码 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |

数据样例：  
```
返回：200
{
  "pk": "1",
  "username": "12345",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "1",
  "nickname": "never",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.png",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "修改成功",
  "code": "200"
}
```

------------------

### 8.UserInfo  
修改用户基本信息  
请求方式： `PUT`  
方法名： users  
ex: http://222.73.0.213:8300/users/1/ `1是用户的pk`  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| token | string | 必填 | 用户验证口令,下一次登录或修改密码时将获取新的token，有效期24H |
| username | string | 选填 | 用户名 |
| nickname | string | 选填 | 昵称 |
| sex | string | 选填 | 0:男,1:女,2:未知 |
| age | string | 选填 | 年龄 |
| email | string | 选填 | email |
| phone | string | 选填 | 手机 |
| country | string | 选填 | 国家 |
| province | string | 选填 | 省/直辖市 |
| city | string | 选填 | 市 |
| career | string | 选填 | 职业 |


返回参数：

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| password | string | 加密后密码 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token |

数据样例：  
```
成功返回：200
{
  "pk": "1",
  "username": "12345",
  "password": "00faa0de2651c8b54e5ab54173cda706",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "1",
  "nickname": "never",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.jpg",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "修改成功",
  "code": "200"
}

```

------------------

### 9.PhoneCaptcha  


发送手机短信验证码  
请求方式： `POST`  
方法名： phonelogin  
ex: http://222.73.0.213:8300/phonelogin/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| phone | string | 必填 | 手机 |

返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |

------------------

### 10.PhoneLogin  

手机验证码登录  
请求方式： `GET`  
方法名： phonelogin  
ex: http://222.73.0.213:8300/phonelogin/  
请求格式： JSON  
请求参数：  

| 字段 | 类型 | 需求 | 说明 |
| ------| ------ | ------ | ------ |
| phone | string | 必填 | 手机 |
| captcha | string | 必填 | 验证码 |

返回参数：  

| 字段 | 类型 | 说明 |
| ------ | ------ | ------ |
| code | string | HTTP状态码 |
| status | string | 状态 |
| msg | string | 详细信息 |
| pk | string | 唯一标识 |
| username | string | 用户名 |
| password | string | 加密后密码 |
| nickname | string | 昵称 |
| sex | string | 0:男,1:女,2:未知 |
| age | string | 年龄 |
| email | string | email |
| phone | string | 手机 |
| country | string | 国家 |
| province | string | 省/直辖市 |
| city | string | 市 |
| career | string | 职业 |
| login_type | string | 登录类型 |
| img | string | 头像地址 |
| date_joined | string | 注册日期 |
| roomid | string | 分配房间号 |
| token | string | 用户验证口令,下一次登录或修改密码时将获取新的token |

数据样例：  
```
成功返回：200
{
  "pk": "1",
  "username": "12345",
  "password": "00faa0de2651c8b54e5ab54173cda706",
  "token": "8ca6dd209e7f780229cdee74ef525dfe",
  "login_type": "1",
  "nickname": "never",
  "sex": "0",
  "age": "0",
  "email": "never@gmail.com",
  "phone": "18752000500",
  "img": "static/mcuser/img/tests1.jpg",
  "country": "",
  "province": "",
  "city": "",
  "career": "",
  "roomid": "8696",
  "date_joined": "2016-10-28T02:27:15.211240Z",
  "status": "SUCCESS",
  "msg": "修改成功",
  "code": "200"
}

```






