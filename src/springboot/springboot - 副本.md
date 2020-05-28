---
layout: post
title: import excel to mysql2
slug: import-excel-to-mysql2
date: 2020-05-28 12:35
status: publish
author: LifeAlsoIsGG
categories: 
  - springboot
tags: 
  - springboot
excerpt: import excel to mysql in springboot
---



Github:[import excel to mysql](https://github.com/LifeAlsoIsGG/MyPractice-Neusoft/tree/master/import-Excel)



## 1.准备

### 1.1添加所需要的的依赖

```xml
<!-- excel需要的包-->
<!-- https://mvnrepository.com/artifact/org.apache.poi/poi -->
<!--文件上传组件-->
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.3.1</version>
</dependency>
<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.5</version>
</dependency>
<!--读取excel文件-->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>3.17</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>3.17</version>
</dependency>
```



### 1.2根据excel的字段添加对应字段的表

excel表

![](https://cdn.jsdelivr.net/gh/lifealsoisgg/MyPractice-Neusoft/import-Excel/images/excel字段.jpg)

mysql表

![](https://cdn.jsdelivr.net/gh/lifealsoisgg/MyPractice-Neusoft/import-Excel/images/excel字段.jpg)



### 1.3在IDEA使用easycode插件对此表使用生成MVC

目录图如下

<div align=center><img src="https://cdn.jsdelivr.net/gh/lifealsoisgg/MyPractice-Neusoft/import-Excel/images/目录.jpg"/></div>

## 2.核心代码

### 2.1创建能处理excel转换为`List<Object>`的方法

创建`ExcelForList`类并创建`ExcelForList`方法用于处理excel表各个记录并返回

```java
package com.example.demo.excelUtils;

import com.example.demo.entity.Course;
import com.example.demo.dao.CourseDao;
import com.example.demo.service.CourseService;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import java.beans.PropertyDescriptor;
import java.io.InputStream;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
public class ExcelForList {
    public static List<Object> ExcelForList(MultipartFile file, Class<?>  beanclazz, Boolean titleExist, String excelType) {
        List<Object> list = new ArrayList<Object>();
        Workbook wb;
        try {
            // IO流读取文件
            InputStream input = file.getInputStream();
            // 创建文档
            if(excelType.equals("xls")) {
                wb = new HSSFWorkbook(input);
            } else if(excelType.equals("xlsx")){
                wb = new XSSFWorkbook(input);
            }else{
                System.out.println("错误！---------------------文件不含xls或xlsx！-----------------");
                return  null;
            }
            // 得到第一张工作表
            Sheet sheet = wb.getSheetAt(0);
            int i;
            if (titleExist) {
                i = 2;
            } else {
                i = 0;
            }
            // 行的遍历
            //excels是从0开是的，getLastRowNum是获取最后一行的行数
            for (; i <= sheet.getLastRowNum(); i++) {
                // 得到行
                Row row = sheet.getRow(i);
                // 单元格的遍历
                // 实例化对象
                Object object = beanclazz.newInstance();

                Field[] fields = beanclazz.getDeclaredFields();
                int j = 0;
                for (Field field : fields) {
                    String fieldName = field.getName();
                    PropertyDescriptor pd = new PropertyDescriptor(fieldName, beanclazz);
                    Method getMethod = pd.getWriteMethod();
                    Cell cell = row.getCell(j++);
                    try{
                        int type = cell.getCellType();

                        if (type == cell.CELL_TYPE_BOOLEAN) {
                            // 返回布尔类型的值
                            boolean value = cell.getBooleanCellValue();
                            getMethod.invoke(object, value);
                            System.out.println(object);
                            System.out.println(value);
                        } else if (type == cell.CELL_TYPE_NUMERIC) {
                            // 返回数值类型的值
                            Double d = cell.getNumericCellValue();
                            int value = d.intValue();
                            getMethod.invoke(object, new Integer(value));
                        } else if (type == cell.CELL_TYPE_STRING) {
                            // 返回字符串类型的值
                            String value = cell.getStringCellValue();
                            getMethod.invoke(object, new String(value));
                        }

                    }catch (Exception e) {
                        System.out.println("");
                    }
                }
                list.add(object);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return list;
    }


}
```



### 2.1创建接口

> - 获取到文件
> - 调用上述方法获取到List<Object>
> - 循环List<Object>转换为一个个course对象再插入到数据库中



```java
//    导入excel到数据库
@RequestMapping(value="/import",method = RequestMethod.POST,produces = { "application/json;charset=UTF-8"})
    public  String imporCourse(@RequestParam("excelFile") MultipartFile excelFile, HttpSession httpSession) throws IOException {
        InputStream in =excelFile.getInputStream();
        String fileOriginalName=excelFile.getOriginalFilename();
        String fileName=excelFile.getName();
        String excelType=fileOriginalName.substring(fileOriginalName.indexOf(".")+1);

        //记录插入多条记录到了数据库；
        int importSuccessNum=0;
        int importAllNum=0;
        boolean importSuccess;

        System.out.println("in:::"+in);
        System.out.println("fileOriginalName:::"+fileOriginalName);
        System.out.println("fileName:::"+fileName);
        System.out.println("excelType:::"+excelType);
        List<Object> forlist= ExcelForList.ExcelForList(excelFile,Course.class,true,excelType);
        for (Object object: forlist) {
//            在这里对每个Object转换为course对象
            Course course=(Course) object;
            importAllNum++;
            importSuccess=courseService.importExcel(course);
            if(importSuccess)
                importSuccessNum++;

        }
        httpSession.setAttribute("importAllNum",importAllNum);
        httpSession.setAttribute("importSuccessNum",importSuccessNum);

        if(importSuccessNum>0)
            return "success!"+"应处理"+importAllNum+"条,已成功处理"+importSuccessNum+"条！";
        else{
            return "error!";
        }
```



## 3.Console

### 3.1POSTMAN

调用接口http://localhost:8886/course/import

method="POST"

> - HEADERS中添加KEY:`Content-Type`,VALUE:`multipart/form-data`
> - BODY中选择类型为`form-data`并上传文件



### 3.2MYSQL



### 3.3IDEA

