## 项目说明
项目结构如下：

```
.
├── app.py
├── config.py
├── database.py
├── models.py
├── static
│   ├── css
│   │   └── common.css
│   └── js
│       └── common.js
└── templates
	  └── homepage.htm

```

这里是各个文件作用的简单说明：

* app.py: 在flask中，app.py是默认的程序入口，这里包含了flask应用的创建、一些依赖库的引用和简单的路由；
* database.py: 这里用flask的数据库扩展类构建了一个实例；
* models.py: 数据库表模型的创建，具体请参见手册；
* config.py: 项目和远程数据库的配置信息，你需要谨慎修改（通常不需要）；
* static/
  * css/: 在此处存放网页模板的层叠样式表文件；
  * js/: 在此处存放网页模板的脚本文件；
* templates: 在此处存放网页模板文件。

