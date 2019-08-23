# api

**简要描述：** 

- 斗鱼直播实时top120主播信息

**请求URL：** 
- ` http://api.cuijianhui.com/v1/douyu/top120 `
  
**请求方式：**
- GET 

**参数：** 

|参数名|必选|类型|说明|默认值
|:----    |:---|:----- |:-------|-----   |
|start |否  |int |开始位置   |0|
|count |否  |int | 返回条数    |20|

 **返回示例**

``` 
  {
  "types": "DouYu",
  "total": 20,
  "content": [
    {
      "room_id": 71819,
      "anchor_name": "Q老钱",
      "anchor_type": "王者荣耀",
      "room_name": "先上个荣耀！12点送手机！",
      "od": "国服最强典韦",
      "hot": 2976170,
      "url": "https://www.douyu.com/91888",
      "anchor_id": 1130108
    },
	...
```

 **返回参数说明** 

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|types |string   |直播平台  |
|total |int |返回的数据条数|
|content|list|主播信息列表|
 **备注** 
 
 ----------------------------------------------------
 
 **简要描述：** 

- 英雄联盟英雄属性查询

**请求URL：** 
- ` http://api.cuijianhui.com/v1/game/league `
  
**请求方式：**
- GET

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|key |是  |string |查询的关键字   |

 **返回示例**
http://api.cuijianhui.com/v1/game/league?key=卡莎
``` 
{
  "total": 1,
  "heros": [
    {
      "称号": "虚空之女",
      "名字": "卡莎",
      "tags": [
        "Marksman"
      ],
      "背景故事": "在孩童时期就被虚空夺走的卡莎，凭着纯粹的固执和意志力活了下来。她的历练让她成为了一位夺命的猎手，或者也有人会称她为黑暗未来的使者。她与一副有生命的虚空生物甲壳形成了一种不得安宁的共生状态，而很快她就将面临一个重大的抉择，究竟是原谅那些称她为怪物的凡人并协力抵御压境的黑暗……还是干脆忘记，放任虚空吞噬这个已将她抛弃的世界。",
      "使用技巧": "尝试抓住对方落单的输出，并用艾卡西亚暴雨来将其轰杀。,与你的队友一起发动你的终极技能，并利用你的被动来充分输出伤害。,确保购买那些能够至少进化你1到2个技能的装备。",
      "对线技巧": "卡莎非常善于带走落单的敌人。要对付她就得保持抱团。,卡莎很容易就会在对抗法师和超远程输出时陷入射程劣势。,请时刻保证自己已在盲区布置了守卫，这样一来就能看到卡莎的到来了。",
      "皮肤": [
        {
          "id": "145001",
          "皮肤名称": "弹幕天使 卡莎",
          "皮肤图片": "http://ossweb-img.qq.com/images/lol/web201310/skin/big145001.jpg"
        },
        {
          "id": "145014",
          "皮肤名称": "K/DA 卡莎",
          "皮肤图片": "http://ossweb-img.qq.com/images/lol/web201310/skin/big145014.jpg"
        },
        {
          "id": "145015",
          "皮肤名称": "K/DA 卡莎 至臻",
          "皮肤图片": "http://ossweb-img.qq.com/images/lol/web201310/skin/big145015.jpg"
        },
        {
          "id": "145016",
          "皮肤名称": "iG 卡莎",
          "皮肤图片": "http://ossweb-img.qq.com/images/lol/web201310/skin/big145016.jpg"
        }
      ],
      "技能介绍": {
        "被动": "体表活肤",
        "被动图片": "http://ossweb-img.qq.com/images/lol/img/passive/Kaisa_Passive.png",
        "Q技能": "艾卡西亚暴雨",
        "Q技能图片": "http://ossweb-img.qq.com/images/lol/img/spell/KaisaQ.png",
        "W技能": "虚空索敌",
        "W技能图片": "http://ossweb-img.qq.com/images/lol/img/spell/KaisaW.png",
        "E技能": "极限超载",
        "E技能图片": "http://ossweb-img.qq.com/images/lol/img/spell/KaisaE.png",
        "R技能": "猎手本能",
        "R技能图片": "http:猎手本能"
      }
    }
  ]
} 
```

 **返回参数说明** 

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|total |int   |查询匹配的结果数  |
|heros|list|所有匹配的英雄信息|

 **备注** 

- 缺少参数的返回信息
``` 
{
  "description": "缺少参数 key",
  "error_code": 10005,
  "request": "GET /v1/game/league"
}
```

------------------------------------------------
**简要描述：** 

- 豆瓣高分榜电影

**请求URL：** 
- ` http://api.cuijianhui.com/v1/highscore/ `
  
**请求方式：**
- GET

**参数：** 

|参数名|必选|类型|说明|默认值|
|:----    |:---|:----- |:-----|-------   |
|count |否  |int |获取的数目   |20|

 **返回示例**
http://api.cuijianhui.com/v1/highscore/?count=1
``` 
// 20190823153640
// http://api.cuijianhui.com/v1/highscore/?count=1

{
  "total": 1,
  "subjects": [
    {
      "影片名": "疯狂的麦克斯4：狂暴之路",
      "类型": "动作,科幻,冒险",
      "宣传海报": "http://img1.doubanio.com/view/photo/s_ratio_poster/public/p2236181653.jpg",
      "收藏数": "338377",
      "原影片名": "Mad Max: Fury Road",
      "上映年份": "2015",
      "豆瓣评分": "8.6",
      "id": "3592854",
      "演员": [
        {
          "name": "汤姆·哈迪",
          "avatars": "http://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p5110.jpg",
          "star_id": "1049489"
        },
        {
          "name": "查理兹·塞隆",
          "avatars": "http://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p44470.jpg",
          "star_id": "1018991"
        },
        {
          "name": "尼古拉斯·霍尔特",
          "avatars": "http://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1371701601.6.jpg",
          "star_id": "1036341"
        }
      ],
      "导演": [
        {
          "name": "乔治·米勒",
          "avatars": "http://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p33507.jpg",
          "star_id": "1056046"
        }
      ]
    }
  ]
}
```

 **返回参数说明** 

|参数名|类型|说明|
|:-----  |:-----|:-----|
|total |int   |返回条数 |
|subjects|list|电影条目|

 -------------------------------------------------
 
    
**简要描述：** 

- 验证码图片生成器

**请求URL：** 
- ` http://api.cuijianhui.com/v1/validatecode/<width>/<high> `
  
**请求方式：**
- GET

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|width |是  |int |图片的宽度   |
|high |是  |int | 图片的高度    |

 **返回示例**
http://api.cuijianhui.com/v1/validatecode/100/100
``` 
{ 
  "code": "rom5",
  "content": "data:image/png;base64,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"
}
```

 **返回参数说明** 

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|code |string   |验证码的值  |
|content|string|图片的base64数据|


**使用示例**

ajax请求url获取到数据后,将img标签中src的值设置为回调函数结果的content  

<img src="">
