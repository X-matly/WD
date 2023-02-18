# TO-DO LIST 开发日志

[TOC]

## 1：项目构想

### 用户在主页面可以：

* 点击”点击创建新事项“以显示添加新事项界面
* 点击”点击显示所有事项“以显示已有事项展示界面
* 在页面左侧输入事项的ID以跳转至待办事件详情页面

### 用户在"创建新事项界面"可以：

* 创建新的待办事项，设置相应的截止时间和重要程度，并为待办事项添加详细的内容说明

### 用户在"显示所有事项界面"可以：

* 用户可以查看已有的所有事项，并选择将其按照开始日期、结束日期或重要程度进行排序显示

### 用户在"待办事件详情页面"可以：

* 查看待办事项的所有信息
* 修改待办事项的相关信息，包括设置该事项是否已完成，点击提交后保存修改到后台
* 点击删除移除待办事项

## 2：前端页面布局

### 2.1：主页面（homepage）

div块主页面分为三块，分别为

```html
<div id="tag">              <!--顶部标签栏 -->
<div id="button_place">     <!--左侧按钮栏 -->
<div id="code" >			<!--主内容栏 -->
```

其中，code栏包含了两个子div块

```html
<div id="hidden_note"  style="display: none">       <!--隐藏的查看事项栏 -->
<div id="hidden" style="display: none">    			<!--隐藏的新建事项栏 -->
```
分别是"显示所有事项界面"和"显示所有事项界面"


### 2.2：事项详情页（information-page）

包括一个主要的div块，负责详细内容的展示和修改表单的提交

```html
<div>
    <form id="modify" action="{{url_for('modify')}}" method="post">
```

## 3：路由

* **/**：主页面加载（homepage.html）
* **/return**：返回主界面
* **/register**：添加事项
* **/delete**：删除特定事项
* **/modify**：修改特定事项
* **/jump**：跳转至特定事项详情页面 \
前端输入ID信息后发出跳转请求，后端完成详情页加载并将获取到的ID传回前端用于进一步读取事项信息
* **/tempdata.json**：读取全部事项信息
* **/get_single_data**：读取全部事项信息 \
前端传递事项唯一ID，后端查询并返回该事项信息

## 4： 数据结构

* `ID`: 事项的编号
* `headline`：事项名称
* `start_date`：事项创建/开始日期          其中包括：`start_year` `start_month` `start_day`
* `end_date`：事项结束日期                       其中包括：`end_year` `end_month` `end_day`
* `significance`：事项的重要程度
* `note`: 事项的具体内容

##5：一些更新进度

* 2022/01/17 21:05 ：接受项目"TO-DO LIST"
* 2022/01/18 00:15 ：创建了第一个主页面雏形；增加了新建事项页面
* 2022/01/18 02:50 ：实现了查看全部事项功能的前端部分
* 2022/01/18 12:33 ：增加了查看全部事项页面
* 2022/01/18 19:38 ：实现已有事项按添加日期、截止日期、重要度排序的前端部分
* 2022/01/18 20:40 ：完善了创建新事项页面，增加设置重要度功能
* 2022/01/19 00:45 ：增加了事项详情页
* 2022/01/19 01:30 ：完善了详情页的显示；实现了在详情页修改、删除事项的前端部分
* 2022/01/19 02:44 ：实现事项的增加功能；实现事项读取动作的前后端交互(stage1&2 completed)
* 2022/01/19 11:02 ：实现根据ID查找已有事项的前后端交互；完善输入ID跳转至详情页的功能
* 2022/01/19 12:19 ：实现事项的删除、修改功能(stage3 completed)
* 2022/01/19 18:04 ：修复了一些BUG，项目基本完成