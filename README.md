#                                                                                       接口自动化项目  

> 1. 环境准备
>
> > + 安装jdk [下载地址](https://www.oracle.com/in/java/technologies/javase-downloads.html) 
> > + 安装python3.9 [下载地址](https://www.python.org/downloads/)
> > + 安装allure客户端 [下载地址](https://github.com/allure-framework/allure2/releases)
> > + 安装navicat客户端 [下载地址](https://www.navicat.com.cn/download/navicat-premium)

> 2. 下载源码

<!-- > > * git clone http://git.kfang.com/test-process-system/module-summary/kfw_infra_api.git -->

> 3. 安装依赖包

> > * 设置工程python解释器
> >
> >   ![](https://i.loli.net/2021/08/10/kUzxH1rKte7G5ow.png)

> > * 打开工程终端，pip安装第三方包    pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt

> >  ![](https://i.loli.net/2021/08/10/jnC4IpsE2gHRcOV.png)

>  	4. 运行脚本

> > ![](https://i.loli.net/2021/08/10/vn9ZlX7eKyN4sp5.png)

> 5. 添加测试用例

> > * 数据库建库，建表(提供了建表sql)

![](https://i.loli.net/2021/08/10/862Owi9ZKbFcTle.png)

> >* excel添加用例，导入模板见下图 

​	![](https://i.loli.net/2021/08/10/mDyAxYsXCgJHl7T.png)		![](https://i.loli.net/2021/08/10/8o3ZNQaUGY5k1BD.png)

> > * 用例导入数据库
> >
> >   <font color=red>注意：①创建ImportData对象所传的参数是对应excel底部的工作表名称</font>
> >
> >   ​           <font color=red>②不要重复导入</font>
> >
> >   ​           <font color=red>③导入时需关闭excel文件</font>
> >
> >   ![](https://i.loli.net/2021/08/10/iOfpcxj2MwtKdmU.png)

> 6. 执行环境切换

​			![](https://i.loli.net/2021/08/10/fINJLmqreysv3jd.png)
