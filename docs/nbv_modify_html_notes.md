

# NBViewer 修改页面样式记录

首先找到NBViewer 源码所在位置，可通过以下两种方式快速查找：

+ conda 命令

  ```bash
  conda show nbviewer
  ```

+ pip 命令

  ```bash
  pip show nbviewer
  ```

上述命令执行完成后会出现源码所在目录路径，然后进入源码文件目录下进行修改．

修改的主要方式为注释，目前没有添加新代码进入．由于NBViewer是使用Python的Web框架构建，并采用了模板语法．注释的语法推荐使用模板语法中的注释而不是HTML中的注释，模板语法格式为`{# 需要注释的内容 #}` ．可跨行进行包裹需要注释的内容．编辑器常用快捷注释为`ctrl + /` ．

## templates/layout.html 文件

**导航栏**

在 NBViewer 源码目录下找到 `templates/layout.html` 文件，这是 NBViewer 页面的开始，可在此文件内部修改共有内容，首先在内部找到`<body class='nbviewer'>`标签，然后继续向下找到 `<nav id='menubar' class='navbar navbar-default nav-fixed-top' data-spy='affix'>` 所有的导航栏修改都在此处． 

**图标**

在导航栏的下面，首先是页面左上角的图标以及点击跳转当前服务首页的设置：

```html
<div class="navbar-header">
  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
    <span class="sr-only">Toggle navigation</span>
    <i class="fa fa-bars"></i>
  </button>
  <a class="navbar-brand" href="{{ from_base('/') }}">
    <img src="{{ static_url("img/nav_logo.svg") }}" width="159"/>
  </a>
</div>
```

跳转至首页的 URL 地址（` <a class="navbar-brand" href="{{ from_base('/') }}">`）在上面代码框中不需要更改，默认首页一般都是从跟路由开始，但是更换图标`<img src="{{ static_url("img/nav_logo.svg") }}" width="159"/>` 需要注意，需要将特换的图标文件放在 nbviewer 源码路径下的`static/img` 目录中，然后将`<img src="{{ static_url("img/nav_logo.svg") }}" width="159"/>`中的`nav_logo.svg` 替换为需要的文件名称．

**隐藏代码**

在展示的报告中要动态的隐藏 notebook 文件的代码单元格，主要分为两步：1）在导航栏中添加`隐藏/显示`功能键，2)为`隐藏/显示`功能键增加实现代码．

1. 增加 `隐藏/显示`功能键

   首先在导航栏代码中找到 `<ul>` 标签列表，这是页面导航栏右上角功能键的代码所在位置，第一个为 JUPYTER 官方链接，是以固定代码的形式写在导航栏代码中的 `<ul>` 标签下．

   在 JUPYTER 功能键的代码下方插入需要的`隐藏/显示`功能键代码：

   ```html
   <li>
     <a href="javascript:code_toggle()">
       <span id="toggleButton" >Show Code</span>
     </a>
   </li>
   ```

2. 实现 `隐藏/显示` 功能键点击切换

   实现功能的代码可在html文件中的`<html>`标签内部增加，建议在文件尾部的`html`标签上部增加，内容为：

   ```javascript
   <script>
       function code_toggle() {
          if (code_shown){
           $('div.input').hide('500');
           $('#toggleButton').html('Show Code');
           $('.output_prompt').hide();
           $('.output_execute_result pre').hide();
                   {#$("div.output_prompt").hide()#}
           } else {
           $('div.input').show('500');
           $('.output_prompt').show();
           $('.output_execute_result pre').show();
           $('#toggleButton').html('Hide Code');
                   {#$("div.output_prompt").show()#}
        }
           code_shown = !code_shown
        };
   
         $( document ).ready(function(){
         code_shown=false;
         $('div.input').hide();
               {# $('.output_prompt').empty();
         $('.output_execute_result pre').empty();#}
       });
   </script>
   ```

**隐藏其他功能键**

导航栏出 JUPYTER 功能键外还有一些其他功能键，不过其他的功能键有些不是固定代码的形式存在的，是以宏函数的形式动态创建的．在 JUPYTER 功能键代码继续向下查看其中`{{ head_text(from_base('/fap'), "FAQ")}}` 为帮助功能键等．

在导航栏`<ul>`表签中的功能键都可注释，但是注释从`<ul>`标签下的`<li>`标签开始．并且需要注意HTML标签多数为一对，有开始和结束，需要两者全部注释．

**取消页面底部信息**

在`templates/layout.html`文件中找到`{%block footer %} ... {%endblock%}` 关键词，在两个关键词中间部分都可注释．

## templates/index.html文件

在`templates/index.html` 文件中找到`{% for section in sections %}...{% endfor %}`关键词，此部位为显示当前NBViewer可支持展示的语言，图像效果等．



## templates/notebook.html文件

notebook.html文件主要为报告展示的主页面

**导航栏功能键**

在文件中找到`{% block otherlinks %}...{% endblock%}` 关键词，中间部分为导航栏右上角功能键的设置，可进行选择注释．

此部分全部为模板语法，和HTML语法一样，有开始和结束．在注释的时候需要注意找对对应的开始和结束．

**文件路径列表**

在文件中找到`{% block body %}...{% endblock %}` 中为notebook文件展示主体，注释其中`{{ link_breadcrumbs(breadcrumbs) }}` ．

在本文件底部同样还有管有NBViewer版本信息的`{% block version_info %}...{% endblock %}` 以及发布时间`{% block extra_footer %}...{% encblock %}` 可选择注释．

 

