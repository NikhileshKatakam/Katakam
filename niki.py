{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "google.com\n",
      "{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}\n"
     ]
    }
   ],
   "source": [
    "# 1 question\n",
    "def char(str1):\n",
    "    dict = {}\n",
    "    for n in str1:\n",
    "        keys = dict.keys()\n",
    "        if n in keys:\n",
    "            dict[n] += 1\n",
    "        else:\n",
    "            dict[n] = 1\n",
    "    return dict\n",
    "n=input()\n",
    "print(char(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nikki wefejfef\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "# 3rd qustion\n",
    "n=list(map(str,input().split()))\n",
    "print(len(max(n)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "king nikki king nikki\n",
      "{'king': 2, 'nikki': 2}\n"
     ]
    }
   ],
   "source": [
    "# 4 th question\n",
    "def word_count(str):\n",
    "    counts = dict()\n",
    "    words = str.split()\n",
    "\n",
    "    for word in words:\n",
    "        if word in counts:\n",
    "            counts[word] += 1\n",
    "        else:\n",
    "            counts[word] = 1\n",
    "\n",
    "    return counts\n",
    "\n",
    "n=input()\n",
    "print( word_count(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PyThon wIth Ml\n",
      "PYTHON WITH ML\n"
     ]
    }
   ],
   "source": [
    "# 5 th question\n",
    "def to_uppercase(str1):\n",
    "    num_upper = 0\n",
    "    for letter in str1[:4]: \n",
    "        if letter.upper() == letter:\n",
    "            num_upper += 1\n",
    "    if num_upper >= 2:\n",
    "        return str1.upper()\n",
    "    return str1\n",
    "n=input()\n",
    "print(to_uppercase(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "king nikki\n",
      "3\n",
      "['i', 'i', 'i']\n"
     ]
    }
   ],
   "source": [
    "# 6th question\n",
    "def vowel(text):\n",
    "    vowels = \"aeiuoAEIOU\"\n",
    "    print(len([letter for letter in text if letter in vowels]))\n",
    "    print([letter for letter in text if letter in vowels])\n",
    "n=input()\n",
    "vowel(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "The list is empty\n"
     ]
    }
   ],
   "source": [
    "n=input()\n",
    "my_list = ()\n",
    "if len(my_list) == 0:\n",
    "    print(\"The list is empty\")\n",
    "else:\n",
    "    print(\"The list is not empty\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def common_data(list1, list2):\n",
    "     result = False\n",
    "     for x in list1:\n",
    "         for y in list2:\n",
    "             if x == y:\n",
    "                 result = True\n",
    "                 return result\n",
    "print(common_data([1,2,3,4,5], [5,6,7,8,9]))\n",
    "print(common_data([1,2,3,4,5], [6,7,8,9]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n"
     ]
    }
   ],
   "source": [
    "# python functions\n",
    "def maximum(a, b, c): \n",
    "  \n",
    "    if (a >= b) and (a >= b): \n",
    "        largest = a \n",
    "  \n",
    "    elif (b >= a) and (b >= a): \n",
    "        largest = b \n",
    "    else: \n",
    "        largest = c \n",
    "          \n",
    "    return largest \n",
    "  \n",
    "   \n",
    "a = 10\n",
    "b = 14\n",
    "c = 12\n",
    "print(maximum(a, b, c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many numbers: 5\n",
      "Enter number 2\n",
      "Enter number 3\n",
      "Enter number 4\n",
      "Enter number 3\n",
      "Enter number 2\n",
      "Sum of elements in given list is : 14\n"
     ]
    }
   ],
   "source": [
    "lst = []\n",
    "num = int(input('How many numbers: '))\n",
    "for n in range(num):\n",
    "    numbers = int(input('Enter number '))\n",
    "    lst.append(numbers)\n",
    "print(\"Sum of elements in given list is :\", sum(lst))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "112\n"
     ]
    }
   ],
   "source": [
    "def multiply(numbers):  \n",
    "    total = 1\n",
    "    for x in numbers:\n",
    "        total *= x  \n",
    "    return total  \n",
    "print(multiply((8, 2,1, 7)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original String :  The quick Brown Fox\n",
      "No. of Upper case characters :  3\n",
      "No. of Lower case Characters :  13\n"
     ]
    }
   ],
   "source": [
    "def string_test(s):\n",
    "    d={\"UPPER_CASE\":0, \"LOWER_CASE\":0}\n",
    "    for c in s:\n",
    "        if c.isupper():\n",
    "           d[\"UPPER_CASE\"]+=1\n",
    "        elif c.islower():\n",
    "           d[\"LOWER_CASE\"]+=1\n",
    "        else:\n",
    "           pass\n",
    "    print (\"Original String : \", s)\n",
    "    print (\"No. of Upper case characters : \", d[\"UPPER_CASE\"])\n",
    "    print (\"No. of Lower case Characters : \", d[\"LOWER_CASE\"])\n",
    "n=input()\n",
    "string_test(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "4\n",
      "66\n"
     ]
    }
   ],
   "source": [
    "list1 = [10, 21, 4, 45, 66, 93] \n",
    "def fin(list1):\n",
    "    for num in list1:  \n",
    "        if num % 2 == 0: \n",
    "            print(num) \n",
    "fin(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
