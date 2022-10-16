- Boolean Identities

  - ```
    Commutative Laws
    (x AND y) = (y AND x)
    (x OR y) = (y OR x)
    
    Associative  Laws
    (x AND (y AND z)) = ((x AND y) AND z)
    (x OR (y OR z)) = ((x OR y) OR z)
    
    Distributive Laws
    (x AND (y OR z)) = (x AND y) OR (x AND z)
    (x OR (y AND z)) = (x OR y) AND (x OR z)
    
    De Morgan Laws
    NOT(x AND y) = NOT(x) OR NOT(y)
    NOT(x OR y) = NOT(x) AND NOT(y)
    
    Idempotence Law
    x AND x = x
    
    Double Negation Law
    NOT(NOT(x)) = x
    ```

- 如何由一个真值表构造一个布尔表达式

  - | x    | y    | z    | f    |
    | ---- | ---- | ---- | ---- |
    | 0    | 0    | 0    | 1    |
    | 0    | 0    | 1    | 0    |
    | 0    | 1    | 0    | 1    |
    | 0    | 1    | 1    | 0    |
    | 1    | 0    | 0    | 1    |
    | 1    | 0    | 1    | 0    |
    | 1    | 1    | 0    | 0    |
    | 1    | 1    | 1    | 0    |

  - 第一步：只需要构建所有 f 为 1 的行的布尔表达式，是的其只有当前行 f 为 1 ，其他行 f 为 0 。**注意只需要使用 AND 连接每一部分既可以实现该目的**

    - 第一行：NOT(x) AND NOT(y) AND NOT(z)
    - 第三行：NOT(x) AND y AND NOT(z)
    - 第四行：x AND NOT(y) AND NOT(z)

  - 第二步：**将所有得到的布尔表达式用 OR 连接**，最终得到的表达式即为满足真值表的布尔表达式

    - (NOT(x) AND NOT(y) AND NOT(z)) OR (NOT(x) AND y AND NOT(z)) OR (x AND NOT(y) AND NOT(z))
    - (NOT(x) AND NOT(z)) OR (x AND NOT(y) AND NOT(z))
    - (NOT(x) AND NOT(z)) OR (NOT(y) AND NOT(z))
    - NOT(z) AND (NOT(x) OR NOT(y))

  - 第三步：简化得到的布尔表达式，~~找到最短的布尔表达式 (NP问题) ，或者找到在设计计算机时最有效率的布尔表达式~~

- 所有的布尔表达式都可以使用 AND、OR、NOT组成

  - 实际上，**OR 不是必须的**，(x OR y) = NOT(NOT(x) AND NOT(y))

- 与非门 NAND

  - | y    | x    | NAND |
    | ---- | ---- | ---- |
    | 0    | 0    | 1    |
    | 1    | 0    | 1    |
    | 0    | 1    | 1    |
    | 1    | 1    | 0    |

  - x NAND y = NOT(x AND y)

- 实际上，**所有的布尔表达式都可以使用 NAND 来表示**

  - **OR 不是必须的，可以有 AND 和 NOT 组成**，(x OR y) = NOT(NOT(x) AND NOT(y))
  - **NOT 不是必须的**，NOT(x) = (x NAND x)
  - **AND不是必须的**，(x AND y) = NOT(x NAND y)

- 

