# self-SpiderDoubanMovieTop250  

爬虫入门程序，静态网页[豆瓣电影top250](https://movie.douban.com/top250)爬取  

程序设计有冗余，在结构上借鉴scrapy的结构，将下载、爬虫、存储独立开，主要目的是为了全面的向新入坑爬虫的程序员展示爬虫流程  

本人实力有限，程序不完美指出还望包容、批评、指正  

目录结构及文件功能如下：
> 项目根目录  
> > data（存放已爬取数据用文件夹）  
> > > douban_data_example.csv（已爬取数据样例文件）  
> >
> > logs（存放程序运行日志用文件夹）  
> > > douban_log_example.txt（运行日志样例文件）  
> >
> > utils（存放自定义package用文件夹）  
> > > __init__.py（自定义package初始化文件）  
> > > downloader.py（下载器文件）  
> > > logger.py（日志重定向文件）  
> > > pipeline.py（存储器文件）  
> > > spider.py（爬虫文件）  
> >
> > main.py（主程序文件）  
> > README.md（项目自述文件）  
> > requirements.txt（项目依赖文件）  
