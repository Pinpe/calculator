# calculator
简易的基于字典计算器，支持四则运算、增删改查、数据类型。

## 必要环境
- Python 3.x解释器
- conkits第三方库

## 语句列表
### LET
用于对单元赋值，语法为`LET <单元名称>,<值>`
- 单元名称：想要赋值到的单元名称。
- 值：想要赋值的值。
### DEL
用于删除单元，语法为`DEL <单元名称>`
- 单元名称：想要删除的单元名称。
### ADD
用于进行加法运算，语法为`ADD <值1>,<值2>,<单元名称>`
- 值1：参加运算的第一个数。
- 值2：参加运算的第二个数。
- 单元名称：想要保存结果的单元名称。
### SUB
用于进行减法运算，语法为`SUB <值1>,<值2>,<单元名称>`
- 值1：参加运算的第一个数。
- 值2：参加运算的第二个数。
- 单元名称：想要保存结果的单元名称。
### MUL
用于进行乘法运算，语法为`MUL <值1>,<值2>,<单元名称>`
- 值1：参加运算的第一个数。
- 值2：参加运算的第二个数。
- 单元名称：想要保存结果的单元名称。
### DIV
用于进行除法运算，语法为`DIV <值1>,<值2>,<单元名称>`
- 值1：参加运算的第一个数。
- 值2：参加运算的第二个数。
- 单元名称：想要保存结果的单元名称。

**注意：目前只能有两个数参与运算**
### INT
对单元的值转换成整型，语法为`INT <单元名称>`
单元名称：想要转换的单元名称
### STR
对单元的值转换成字符串，语法为`STR <单元名称>`
单元名称：想要转换的单元名称

## 开源协议
针对此项目，你有以下权利：
- 自由使用
- 二次开发
- 二次发布原版或经过修改的版本，且不需要署名

但是，请不要：
- 公然售卖
- 冒充项目的作者

无论是合同、侵权还是其他方式引起的任何索赔、损害或其他责任，在任何情况下作者都不承担责任。
