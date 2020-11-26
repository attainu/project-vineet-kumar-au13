<p align = "center"><img src ="python.png" width="100" height="100">
</p>

# MazeSolver Python Project
```
Project Name : Maze Solver 
Author : Vineet kumar   
Author Email : vineet9717306243@gmail.com
```


## Maze Solver

The `Maze Solver` is a program that takes input as an MxN matrix and outputs the path of the maze denoting 1 as path and 0 as block/wall.


## First step after opening **Python Project**

Github Python Project consists of 3 contents.

1. README.md
2. mazeSolver.py
3. generateMaze.py

### README.md 
Is a User Manual for mazeSolver.py


### mazeSolver.py
Raw code of mazeSolver.py

## How to run MazeSolver In Windows Operating System

Firstly, in the `python project` directory you can see input.txt file give your maze combination to that file.


> You can also Generate maze By using generateMaze.py 
>> Do install numpy before generating the maze

1. It takes the input from the user In the Form M * N
2. By Default 4 *4 matrix auto generates
3. If you don't want to generate the u can edit Input.txt  
4. Thus it will genrate your maze



## How Does code work?

It takes the input matrix , By using BFS finds all the shortest path, By using dijkastra find the shortest path. It gives the output in the form of matrix in the output file output.txt  

> Code is self explanatory as all the comments are well written

## Input commanad to use in your console

>>python mazeSolver.py input.txt output.txt --s=0,0 --d=3,3 it is for the default matrics
and if you put a matrics of M*N then enter --d as M-1,N-1 because as matrics starts from (0,0) and at last the output matrics will be present at output.txt 

> Output.txt will generate your answere. if the answere is there then there will be Matrix if not then the Ans will be -1. 

`THANK YOU`
