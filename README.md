# Compression Algorithm
A text compression algorithm, where the input is a list of words, and the length of the given list may be much greater than the number of unique words.

## Overview
There are many strategies to compress data, reducing the volume of the data and run time of applications. I chose to focus on code-based compression technique called Huffman Code, but there are [many different methods out there](https://www.researchgate.net/publication/331399755_Test_Data_Compression_Methods_A_review).
### Huffman Code
* Huffman Code main principle is to replace the most frequently occurred symbols with shortest code word, and less frequently occurred symbols with higher length of code word. Therefore, it reduces the code word length average.
* Huffman code is obtained by forming Huffman tree in which the value of binary bits flow from root node to leaf node, produces the desired code word.
* I chose implementing it because it felt intuitive and fits to the mission - where a word can occur many times in a given input list.

<br>
<details open="open">
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#compression-ways">Compression Ways</a></li>
    <li><a href="#how-to-use">How To Use</a></li>
    <li><a href="#performance-estimation">Performance Estimation</a></li>

  </ol>
</details>
<br>

## Requirements
The Assignment baselines and requirements can be found and downloaded [here](https://github.com/OrenKov/compression-algorithm/blob/main/Compression%20algorithm.docx).
<br>
<br>

## Compression Ways
There system contains 2 ways for encoding and compressing the data:
* <strong>Encode and compress each word of the input list</strong>, outputting a list of encoded words, ordered by the appearances of the input words.
* <strong>Encode and compress the whole list as a unit</strong>, outputting a string. <br>A good startegy to do so, would be to encode each word separately ('normal' huffman coding), and then encode it again to 1 single string as follows:
  * <strong>Encoding:</strong><br>(1) Save the length of each word, in order to use that number as a delimiter between words in the list. <br>(2)	Add another delimiter ('$') right after the integer (in between the integer and the word itself), for each word.    <br>
  <strong> Input: </strong> `[Oren, Kov1Kov]`  <span>&#8594;</span> <strong> Output: </strong> `4$Oren7$Kov1Kov`

  * <strong>Encoding:</strong><br> Get to the first '$', and read exactly the amount of characters written before it. Add the encoded word to the list, and keep going until no more characters to read.<br>

<strong>NOTE: </strong> Even if a word consists of an integer or a '$' sign, we will just read them as part of the word while decoding the list.<br>
<strong>REMARK: </strong> By small modifications of the implementation, by using the same encoding method, it is possible to encode characters instead of complete words. 

## How To Use
* Download the KNN.py file, and import it to your python working-file.
* <strong>Initialize</strong>:
    ```sh
    $ my_tree = KDTree(list_of_points, K)
    ```
* <strong>Get the approximated KNN</strong>:
    ```sh
    $ my_tree.knn(my_point)
    ```
    where `my_point` is in `(x,y,z)` format.
* <strong>Get z-axis average in a given point segment </strong>:
    ```sh
    $ my_tree.get_z_avg(my_point)
    ```
<br>

## Performance Estimation
### get_z_avg method
* I wanted to see how 'fast' the function runs correlated to the number of points in the data set and K (the number of nearest neighbors).
* 
* The expectation is that the running time increases logarithmically to the amount of points that were used to build the tree, because running the function is a matter of searching in the tree, and then calculating average over O(K) instances.<br>
![equation](https://latex.codecogs.com/gif.latex?\textbf{O(f)}&space;=&space;O(log(n)-log(K)&space;&plus;&space;O(K))&space;=&space;O(log(\frac&space;nK)&space;&plus;&space;O(K)))
*  I ran few toy-checks (under my computer computational limitations) and found out that indeed - the time it takes to perform the function increases logarithmically to the amount of points used to build the tree (for a given K):
<p align="center">
  <img src="https://i.im.ge/2021/08/20/PG5ic.png">
</p>
<br>


