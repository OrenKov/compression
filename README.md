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
The assignment baselines and requirements can be found and downloaded [here](https://github.com/OrenKov/compression-algorithm/blob/main/Compression%20algorithm.docx).
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
<br>

## How To Use
* Download the `Compression.py` file, and import it to your python working-file.
* <strong>Initialize</strong>:
    ```sh
    $ my_compressor = HEncoder()
    ```
* <strong>Encode and compress a list of words</strong> (return a list of encoded words):
    ```sh
    $ encoding_table, encoded_list = my_compressor.encode(my_list)
    ```
* <strong>Decode and compress a list of words</strong> (input is a list of encoded words):
    ```sh
    $ original_list = my_compressor.encode(encoding_table, encoding_list)
    ```
* <strong>Encode and compress the list as a unit </strong> (outputs a string):
    ```sh
    $ encoding_table, encoded_list = my_compressor.encode(my_list, output_list=False)
    ```
* <strong>Decode and compress a list of words</strong> (input is a string):
    ```sh
    $ original_list = my_compressor.encode(encoding_table, encoding_list, input_list=False)
    ```
<br>

## Compression Method Testing
Assuming all inputs are legal and valid, I will perform features testing:
* <strong>Encoding properly: </strong> `(functional)`
  * Returning a list of encoded words and an encoding-table if it was asked to.
  * Returning an encoding (string) of a list and an encoding-table if it was asked to.
* <strong>Decoding properly: </strong> `(functional)`
  * Decoding an encoded list that was encoded by the system (could be a list of encoded words or a string that encodes a list of words - according to the user's request), and that the output is indeed the original list. 
* <strong>Expected-Encoding: </strong> `(functional)`
  * Deals with a list that contains only one unique word (of length 1, and of length > 1). Should encode them both as expected (as an empty string) and decode it back to original.
  * Deals with the same word that is written differently (for example: `['Oren', 'oren']`). Should encode each of the words differently.
  * Deals with repetitions by giving it random input-lists that contains words with repetitions. Should encode the same words with the same code.
  * Decoding an encoded list that was not encoded by the system, and that the output is indeed the original list.
* <strong>The system Compresses its input</strong>: `(functional)` <br>Giving it various types of different lists, generated randomly (with and without repetitions), and checking the size of the original list compared to the encoded list.
  * Can be helpful to determine not just if the system compresses, but also how well it compresses generally, and in different use cases.
* <strong> 'Long' inputs: </strong> `(performance)`
  * Deals with lists that contains many words (with repetitions, and without): Starting with 'small' lists (lets say, 100 words), and increase the amount of words by a constant factor every time. Checking the time of the running CPU and memory usage (are the parameters being checked linear/logarithmic to the input size?).
* <strong>Outputs in a reasonable time:</strong> `(performance)` <br>Can measure the actual time of a query and compare it to other compressors run-time out there.
* <strong>Continuity:</strong> `(performance)` <br>  When it is 'online', see how well it works with lots of requests, for a long time.



