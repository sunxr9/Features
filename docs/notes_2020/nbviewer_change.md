# NBViewer 修改

增加隐藏代码功能和修改 NBViewer 样式。

+ 确认源码文件目录

  使用 `pip show nbviewre` 命令查看源码详情，确定源码目录并进入。

## 增加隐藏代码功能

+ 增加页面隐藏代码功能

  编辑源码目录下 `templates/notebook.html` 文件，定位到`{% block otherlinks %}...{% endblock %}` 代码，该部分是页面导航栏右上角按钮代码所在位置。
  
  + 添加`隐藏/显示`功能代码
  
    将以下代码增加到`{% block otherlinks %}` 代码下方：
  
    ```js
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
    
  + 添加`隐藏/显示` 功能按钮
  
  在上述所添加的代码下方添加功能按钮代码：
  
    ```html
    <li>
      <a href="javascript:code_toggle()">
        <span id="toggleButton" >Show Code</span>
      </a>
    </li>
    ```
  
    

## 修改页面样式

+ 首页展示样例介绍隐藏

  编辑 `templates/index.html` 文件，对 `{% for section in sections %}...{% endfor %}` 区块进行注释。

+  首页底部nbv信息隐藏/移除

  在`templates/layout.html`文件中找到`{%block footer %} ... {%endblock%}` 关键词，在两个关键词中间部分都可注释．

+ 渲染后notebook页面的 **导航路径** 隐藏/移除

  编辑 `templates/notebook.html` 文件， 注释其中 `{{ link_breadcrumbs(breadcrumbs) }}` 部分。

+  渲染后notebook 页面下载等功能移除

  编辑 `templates/notebook.html` 文件， 注释其中 `{% block otherlinks}`  部分中代码。需注意其中`隐藏/显示` 功能代码。

## localfile 文件列表页面注释

+ 取消localfile 文件列表页面

  编辑 `providers/local/handlers.py` 文件，定位以下代码：

  ```python
  if os.path.isdir(fullpath):
  	html = self.show_dir(fullpath, path)
      raise gen.Return(self.cache_and_finish(html))
  ```

  替换为：

  ```python
  if os.path.isdir(fullpath):
  	raise web.HTTPError(404)
  ```

  

