---
layout: post
title: Java-方法汇总
slug: Java-方法汇总
date: 2020/08/08 12:40:33
status: publish
author: LifeAlsoIsGG
categories: 
  - Java
tags: 
  - Java

---



# Java集合



## Collection



### 排序操作

```java
void reverse(List list)//反转
void shuffle(List list)//随机排序
void sort(List list)//按自然排序的升序排序
void sort(List list, Comparator c)//定制排序，由Comparator控制排序逻辑
void swap(List list, int i , int j)//交换两个索引位置的元素
void rotate(List list, int distance)//旋转。当distance为正数时，将list后distance个元素整体移到前面。当distance为负数时，将 list的前distance个元素整体移到后面。
```

示例代码

```java
ArrayList<Integer> arrayList = new ArrayList<Integer>();
		arrayList.add(-1);
		arrayList.add(3);
		arrayList.add(3);
		arrayList.add(-5);
		arrayList.add(7);
		arrayList.add(4);
		arrayList.add(-9);
		arrayList.add(-7);
	System.out.println("原始数组:");
	System.out.println(arrayList);
	// void reverse(List list)：反转
		Collections.reverse(arrayList);
		System.out.println("Collections.reverse(arrayList):");
		System.out.println(arrayList);


		Collections.rotate(arrayList, 4);
		System.out.println("Collections.rotate(arrayList, 4):");
		System.out.println(arrayList);

		// void sort(List list),按自然排序的升序排序
		Collections.sort(arrayList);
		System.out.println("Collections.sort(arrayList):");
		System.out.println(arrayList);

		// void shuffle(List list),随机排序
		Collections.shuffle(arrayList);
		System.out.println("Collections.shuffle(arrayList):");
		System.out.println(arrayList);

		// void swap(List list, int i , int j),交换两个索引位置的元素
		Collections.swap(arrayList, 2, 5);
		System.out.println("Collections.swap(arrayList, 2, 5):");
		System.out.println(arrayList);

		// 定制排序的用法
		Collections.sort(arrayList, new Comparator<Integer>() {

			@Override
			public int compare(Integer o1, Integer o2) {
				return o2.compareTo(o1);
			}
		});
		System.out.println("定制排序后：");
		System.out.println(arrayList);
```



### 查找,替换操作

```java
int binarySearch(List list, Object key)//对List进行二分查找，返回索引，注意List必须是有序的
int max(Collection coll)//根据元素的自然顺序，返回最大的元素。 类比int min(Collection coll)
int min(Collection coll)//最小值
int max(Collection coll, Comparator c)//根据定制排序，返回最大元素，排序规则由Comparatator类控制。类比int min(Collection coll, Comparator c)
void fill(List list, Object obj)//用指定的元素代替指定list中的所有元素。
int frequency(Collection c, Object o)//统计元素出现次数
int indexOfSubList(List list, List target)//统计target在list中第一次出现的索引，找不到则返回-1，类比int lastIndexOfSubList(List source, list target).
boolean replaceAll(List list, Object oldVal, Object newVal)//用新元素替换旧元素
```



**示例代码**

```java
ArrayList<Integer> arrayList = new ArrayList<Integer>();
		arrayList.add(-1);
		arrayList.add(3);
		arrayList.add(3);
		arrayList.add(-5);
		arrayList.add(7);
		arrayList.add(4);
		arrayList.add(-9);
		arrayList.add(-7);
		ArrayList<Integer> arrayList2 = new ArrayList<Integer>();
		arrayList2.add(-3);
		arrayList2.add(-5);
		arrayList2.add(7);
		System.out.println("原始数组:");
		System.out.println(arrayList);

		System.out.println("Collections.max(arrayList):");
		System.out.println(Collections.max(arrayList));

		System.out.println("Collections.min(arrayList):");
		System.out.println(Collections.min(arrayList));

		System.out.println("Collections.replaceAll(arrayList, 3, -3):");
		Collections.replaceAll(arrayList, 3, -3);
		System.out.println(arrayList);

		System.out.println("Collections.frequency(arrayList, -3):");
		System.out.println(Collections.frequency(arrayList, -3));

		System.out.println("Collections.indexOfSubList(arrayList, arrayList2):");
		System.out.println(Collections.indexOfSubList(arrayList, arrayList2));

		System.out.println("Collections.binarySearch(arrayList, 7):");
		// 对List进行二分查找，返回索引，List必须是有序的
		Collections.sort(arrayList);
		System.out.println(Collections.binarySearch(arrayList, 7));
```



ArrayList



### 共有方法

1. **boolean add(E e)**

   > 添加一个元素

2. **boolean addAll(Collection<? extends E> c)**

   > 将集合中的所有元素添加到其他集合中

3. **clear()**

   > 暴力清除集合中所有元素

4. **boolean contains(Object o)**

   > 判断集合是否包含某个元素，包含返回true

5. **boolean isEmpty()**

   > 如果此集合不包含元素，则返回true

6. **int size()**

   > 返回集合个数

7. **Iterator iterator()**

   > 迭代器，返回Iterator类型

   

### List特有







# String字符串



参考

> - https://www.cnblogs.com/windbyside/p/9393716.html







## char charAt(int index)

返回指定索引位置的字符

```java
String str = new String("String");
System.out.println(str.charAt(0));
//return "S";
```



## String substring(int beginIndex)

返回指定起始位置至字符串末尾的字符串

```java
String str = new String("String");
System.out.println(str.substring(1));
//return "tring";
```



## **String** substring(int beginIndex, int endIndex)

返回指定起始位置（含）到结束位置（不含）之间的字符串

```java
String str = new String("String");
System.out.println(str.substring(1, 3));
//return "tr";
```



## int indexOf(String str)

返回指定字符串的索引位置， 没有则返回-1

```java
String str = new String("String");
System.out.println(str.indexOf("i"));
//return "3";

System.out.println(str.indexOf("ing"));
//return "3";
```



## int indexOf(String str, int fromIndex)

返回从指定索引位置fromIndex开始的str的索引位置,如果没有返回-1

```java
String str = new String("String");
System.out.println(str.indexOf("ing", 2));
//return "3";
```



## int lastIndexOf(String str)

返回子字符串最后出现的位置。没有找到，则返回 -1。

```java
String str = new String("StringString");
System.out.println(str.indexOf("String"));
//return "6";
```





## String replace(CharSequence oldString, CharSequence newString):

用newString替换字符串中的oldString，注意相当于new了个新的String，原String不变

```java
String str = new String("String");
System.out.println(str.replace("g", "gs"));
//return "Strings";
```



## String trim()

返回一个去除两头空格的新字符串

```java
String str1 = new String();
　　str1 =  " "+"string"+" ";
　　System.out.println(str1.length());
　　//return "8"
　　str1 = str1.trim();
　　System.out.println(str.length());
　　//return "6"
```



## String[ ] split(String regex)

指定正则表达式分隔符，返回一个字符串数组

```java
String str2 = new String();
　　str2 = "A/B/C";
　　String s[] = str2.split("/");
　　System.out.println("s[0] = "+s[0]);
　　//return"A"
　　for(String ss: s) {
　　System.out.print(ss+" ");
　　}
　　//return"A B C"
```



## String[ ] split(String regex, int limit)

指定正则表达式分隔符regex和分隔份数limit，返回一个字符串数组

```java
String str2 = new String();
　　str2 = "A/B/C";
　　String s[] = str2.split("/", 2);
　　for(String ss: s) {
　　System.out.print(ss+" ");
　　}
　　//return"A B/C"
```



## String.copyValueOf(char[] charArray)

将字符数组转换为字符串

```java
char[] arr=['a','b','c'];
String string =String.copyValueOf(arr);
System.out.println(string);          //abc
```





## String toLowerCase()

转换为小写字母



## String toUpperCase()：

转换为大写字母



## boolean contains(String s)

该方法是判断字符串中是否有子字符串。如果有则返回true，如果没有则返回false。



## boolean startsWith(String prefix)

如果字符串以prefix开头返回true，否则返回false



## boolean endsWith(String suffix)

如果字符串以suffix结尾返回true，否则返回false



## boolean equals(Object other)

如果字符串与other相等返回true，否则返回false



## boolean equalsIgnoreCase(String other)

如果字符串与other相等（忽略大小写）返回true，否则返回false





## StringBuffer | StringBuilder



通用于StringBuilder



### StringBuffer append(String s)

将其他类型拼接操作。可用于字符串数组转

![](images/Java常用方法汇总/StringBuffer_append().jpg)



### String toString()

转换为String。也可以通过构造方法进行转换

```java
StringBuffer stringBuffer = new StringBuffer("String");
stringBuffer.toString()
```





## 字符串 | 数组 | 其它类型 互转



### char[] toCharArray()

字符串 -> 字符数组

```java
String str = new String("String");
System.out.println(str.toCharArray());
```





### String.copyValueOf(char[] charArray)

字符数组 -> 字符串

```java
char[] arr=['a','b','c'];
String string =String.copyValueOf(arr);
System.out.println(string);          //abc
```





### String String.valueOf(char[] c);

将其它类型转换为字符串

![](images/Java常用方法汇总/valueOf.jpg)



### String[] split(String s)

字符串转字符串数组。split() 方法根据匹配给定的正则表达式来拆分字符串。 **. 、 | 和 *** 等转义字符，必须得加 \ \。多个分隔符，可以用 | 作为连字符。

```java
// 字符串转数组  java.lang.String
String str = "0,1,2,3,4,5";
String[] arr = str.split(","); // 用,分割
System.out.println(Arrays.toString(arr)); // [0, 1, 2, 3, 4, 5]
```

> 字符串数组转字符串可以使用**StringBuffer**的拼接操作**append(String s)**进行遍历拼接





### String | StringBuffer/StringBuilder 互转



#### String 转 StringBuffer/StringBuilder

```java
String s = "abc";

//通过构造方法
StringBuffer sb = new StringBuffer(s);

//通过append()方法
StringBuffer sb = new StringBuffer();
sb.append(s);
```



#### StringBuffer/StringBuilder 转 String

```java
StringBuffer sb = new StringBuffer("abc");

//通过构造方法
String s = new String(sb);

//通过toString()方法
String s = sb.toString();
```

