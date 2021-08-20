class Node:
    """
    A node of a tree that is being used to encode and compress data into symbols.
    """

    def __init__(self, symbol=None, weight=0, left=None, right=None):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.weight = weight


class HEncoder:
    """
    Huffman encoder for lists of words.
    """
    def __init__(self):
        self.symbols = {}
        self.encoding_table = {}
        self.tree = []
        self.list = None

    # ************ #
    #     API      #
    # ************ #
    def encode(self, l, output_list=True):
        """
        compresses and encodes a given list of words.
        :param l: a list of words.
        :param output_list: a flag parameter. by-default, encoding each word in the list. if assigned False, encodes
                            the all list to one word.
        :return: encoding_table and list_encoded
                 if return_list=True (default), list_encoded is a list of the encoded words.
                 if return_list=False, list_encoded is a string that encodes that list.
        """
        self.list = l
        self._calc_frequencies()
        self.tree = []
        self._create_nodes_and_sort_by_frequencies()
        self._create_frequencies_tree()                 # self.tree is not a list anymore.
        self._create_encoding_table()
        list_encoded = self._create_encoded_list(output_list)
        return self.encoding_table, list_encoded

    def decode(self, encoding_table, list_encoded, input_list=True):
        """
        decodes a compressed-encoded list of words.
        :param encoding_table: An encoding table. expected to be of type 'dict', with at least one element.
        :param list_encoded: An encoded list. expected to be of type 'list', with at least one element.
        :param input_list: A flag parameter. by-default, decodes each word in the list. If assigned False, decodes
                           a string to a list.
        :return: a decoded list of the list_encoded, by the encoding_table. if the input is invalid, return an empty
                 list.
        """
        decoded = []
        if not self._check_encoding_table(encoding_table) or not self._check_list_encoded(list_encoded):
            return decoded

        # Create the decoding table based on the encoding one.
        decoding_table = {v: k for k, v in encoding_table.items()}

        # If a string is given, first make it to a list of encoded words.
        if not input_list:
            list_encoded = self._decode_as_list(list_encoded)

        # Decode the words and add to a list.
        for word in list_encoded:
            decoded.append(decoding_table[word])
        return decoded

    # ************ #
    #   HELPERS    #
    # ************ #
    def _pre_traverse(self, node, cur_path=""):
        """
        Preorder-Traversing a tree (ROOT, LEFT, RIGHT).
        :return:
        """
        if not node.left:
            self.encoding_table[node.symbol] = cur_path
        else:
            self._pre_traverse(node.left, cur_path=cur_path + '0')
            self._pre_traverse(node.right, cur_path=cur_path + '1')

    def _calc_frequencies(self):
        """
        calculating the frequencies of the appearance of the words in the input list.
        making a dictionary for easy quick retrieval of that information.
        :return:
        """
        self.symbols = {}
        for symbol in self.list:
            self.symbols[symbol] = self.symbols.get(symbol, 0) + 1

    def _encode_as_list(self, l):
        """
        encodes a list to a single string, representing it.
        :param l: The list to be encoded.
        :return: The string representing the input list.
        """
        encoded = ""
        for word in l:
            encoded += str(len(word)) + "$" + word
        return encoded

    def _decode_as_list(self, encoded):
        """
        decodes a string representing a list full of words, to the original.
        :param l: The encoded list.
        :return:  The original, decoded list.
        """
        decoded, i = [], 0
        while i < len(encoded):
            j = i
            while encoded[j] != "$":
                j += 1
            length = int(encoded[i:j])
            decoded.append(encoded[j + 1: j + 1 + length])
            i = j + 1 + length
        return decoded

    def _create_frequencies_tree(self):
        """
        Join couples of nodes, with the new parent node's label being the combined frequency of the 2 nodes:
        :return:
        """
        while 2 <= len(self.tree):
            left = self.tree.pop(0)
            right = self.tree.pop(0)
            self.tree.append(
                Node(  # symbol=left.symbol + right.symbol,
                    weight=left.weight + right.weight,
                    left=left, right=right))
            self.tree.sort(key=lambda node: node.weight)
        self.tree = self.tree[0]

    def _create_nodes_and_sort_by_frequencies(self):
        """
        Create a node for each character and label each with the frequency, sort the nodes in ascending order:
        :return:
        """
        # Create the Nodes:
        for symbol in self.symbols.keys():
            self.tree.append(Node(symbol=symbol, weight=self.symbols[symbol]))

        # Arrange these nodes in ascending frequency:
        self.tree.sort(key=lambda node: node.weight)

    def _create_encoding_table(self):
        """
        Create the encoding table out of the tree.
        Each symbol/word gets a unique binary representation. The length of the representation depends on the frequency
        of the symbol/word appearence.
        :return:
        """
        self.encoding_table = {}
        self._pre_traverse(self.tree)

    def _create_encoded_list(self, output_list):
        """
        Create the encoded list, depending on return_list value.
        :return:
        """
        list_encoded = []
        for word in self.list:
            list_encoded.append(self.encoding_table[word])

        if not output_list:
            encoded_as_list = self._encode_as_list(list_encoded)
            return encoded_as_list

        return list_encoded

    # ************ #
    #   CHECKS     #
    # ************ #
    def _check_encoding_table(self, encoding_table):
        """
        Basic checks for an encoding_table. Checks that it is of type 'dict' and that it is not empty.
        :param encoding_table: The encoding table.
        :return: True for a valid table, else False
        """
        if not isinstance(encoding_table, dict):
            print("encoding_table is expected to be of type 'dict'")
            return False
        if len(encoding_table) < 1:
            print("encoding_table is expected not to be empty")
            return False
        return True

    def _check_list_encoded(self, list_encoded):
        """
        Basic checks for an encoding_table. Checks that it is of type 'dict' and that it is not empty.
        :param encoding_table: The encoding table.
        :return: True for a valid table, else False
        """
        if not isinstance(list_encoded, list):
            print("list_encoded is expected to be of type 'list'")
            return False
        if len(list_encoded) < 1:
            print("list_encoded is expected not to be empty")
            return False
        return True