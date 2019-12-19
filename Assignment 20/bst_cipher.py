#  File: bst_cipher.py

#  Description: Encrypts and decrypts phrases using the binary tree

#  Student's Name: Derek Wu

#  Student's UT EID: dw29924

#  Partner's Name: Victor Li

#  Partner's UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 15 November, 2019

#  Date Last Modified: 15 November, 2019

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
        self.root = None
        for ch in encrypt_str:
            ascii_val = ord(ch.lower())
            if (( ascii_val >= 97 and ascii_val <= 122)):
                self.insert(ch)
            elif (ascii_val == 32):
                self.insert(ch)
            else:
                continue

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    new_node = Node(ch)
    parent = self.root
    current = self.root
    if current == None:
        self.root = new_node
    else:
        while current != None:
            if ch == current.data:
                parent = current
                break
            elif ch < current.data:
                # go to the left of the tree
                parent = current
                current = current.lchild
            elif ch > current.data:
                # go to the right of the tree
                parent = current
                current = current.rchild
        if ch < parent.data:
            # place node on the left of the tree
            parent.lchild = new_node
        elif ch > parent.data:
            # place node on the right of the tree
            parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
      output = ''
      current = self.root
      if ch == self.root.data:
          return '*'
      else:
        while current != None:
            if ch == current.data:
                return output
            elif ch < current.data:
                output += '<'
                current = current.lchild
            elif ch > current.data:
                output += '>'
                current = current.rchild
        return ''

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    for ch in st:
        if current == None:
            return ''
        else:
            if ch == '<':
                current = current.lchild
            if ch == '>':
                current = current.rchild
    return current.data
            
          
  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
      output = ''
      st = st.lower()
      for ch in st:
            if ((ord(ch) == 32) or ((ord(ch) >= 97) and (ord(ch) <= 122))):
                output = output + self.search(ch) + '!'
      output = output[:-1] 
      return output            
    
  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
      output = ''
      st_arr = st.split('!')
      for ch in st_arr:
          output += self.traverse(ch)
      return output

def main():
    #encrypt_key = 'the quick brown fox jumps over the lazy dog'
    #encrypt_key = 'meet me'
    encrypt_key = input('Enter encryption key:')
    tree = Tree(encrypt_key)
    print()
    encrypt_st = input('Enter string to be encrypted: ')
    print('Encrypted string: ', tree.encrypt(encrypt_st))
    print()
    decrypt_st = input('Enter string to be decrypted: ')
    print('Decrypted string: ', tree.decrypt(decrypt_st))  

main()
