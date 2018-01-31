https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview

In the bottom-up approach, we calculate the smaller values of fib first, then build larger values from them.

This method also uses O(n) time since it contains a loop that repeats n − 1 times, but it only takes constant (O(1)) space,
in contrast to the top-down approach which requires O(n) space to store the map.


 function fib(n)
       if n = 0
           return 0
       else
           var previousFib := 0, currentFib := 1
           repeat n − 1 times // loop is skipped if n = 1
               var newFib := previousFib + currentFib
               previousFib := currentFib
               currentFib  := newFib
       return currentFib





Bellman Ford



Djikstra's
SHORTEST PATH B/W TWO POINTS

1. To start, each point's initial cost value is set.
2. Starting point set to 0 (user), all others to infinity
3. Starting from present location, we search for unexplored points.
    - once found, these points become candidates for moving to next
4. Cost of each candidate points is calculated.
    - The method of calculation is the current point's cost + the cost of moving to a candidate point
5. IF CALCULATED COST LESS THAN THE CURRENT VALUE (OF THE POINT), COST OF POINT IS UPDATED
6. WE CHOOSE THE ONE WITH THE LOWEST COST
7. Repeat from 3



Floyd Warshall





DYNAMIC PROGRAMMING DAVIS STAIRCASE

https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
https://www.hackerrank.com/challenges/ctci-recursive-staircase/forum


FIBONNACI USING MATRIX
https://www.nayuki.io/page/fast-fibonacci-algorithms




CPP STL


#include<vector>

VEC
vector<T> v;
v.push_back(T t) - O(1)
v[i] - O(1)
v.size() - O(1)
v.pop_back() - O(1)
=       Omega(n)


LIST
list<T> l;
l.push_front(T t)
l.push_back(T t)
l.pop_front()
L.pop_back()
L.front()
L.back()
L.size().          O(1)
=.          Omega(n)


MAP [BINARY SEARCH TREE]
map <key, value> M;
M[k]
bool M.count(k)
               O(logn)
M.size()
                O(1)
=.             Omega (n)
               


#include <algorithm>
ITR

vector <int>::iterator itr;
list <int>::iterator itr;
map <int,int>::iterator itr;

If the container object is a const (e.g., const vector<int>), we
need to use the corresponding const_iterator
(i.e., vector<int>::const_iterator) to access the
items in the const container object.

itr = d.begin(); itr!=d.end(); itr++

Set 100
*Itr = 100

Get(map)
(*Itr).first
(*Itr).second 


ALGO

sort()
binary_search()
lower_bound()
upper_bound()
random_shuffle()

void sort( RandomAccessIterator first, RandomAccessIterator last ,Compare comp);
- O(n log n)
- only on vector [random access iterator]
- However, list::sort() can do it,
- map organizes the <key,value> pair in sorted order of the key.

bool binary_search ( ForwardIterator first, ForwardIterator last, const T & target );
- needs sorted data
- forward iterator
-  O(logn) - vector
- O(n) - list,map

ForwardIterator lower_bound( ForwardIterator first, ForwardIterator last, const T & target );
ForwardIterator upper_bound( ForwardIterator first, ForwardIterator last, const T & target);

the distance between upper_bound( first, last, target ) and
lower_bound(first, last, target) is the number of occurrences 
of target in the range [first,last).

void random_shuffle( RandomAccessIterator first, RandomAccessIterator last);


SEED
#include <cstdlib>
#include <ctime>
srand( time(NULL) );



STACK
#include <stack>
stack<int> mystack;
mystack.empty()
mystack.size()
mystack.top()
mystack.push(int ele);
mystack.emplace ("Second sentence");
mystack.pop();
foo.swap(bar); - exchanges the contents of the two stacks wtf


QUEUE
#include <queue> 
queue<int> myqueue;
myqueue.empty()
size
front 
back
push
emplace
pop
swap


HEAP
vector<float> min_heap
make_heap(min_heap.begin(), min_heap.end());
min_heap.push_back(x);
max_heap.front();



Priority Queue
#include <queue>
priority_queue<int> mypq;
mypq.empty()
 mypq.pop();
push
mypq.top();
size
emplace
swap

SET
#include <set>
set <int> s;
begin 
end
size
max_size
insert
it = myset.begin();
myset.erase (it);
erase(int ele)
swap 
clear   -all
myset.find(20);
myset.count();


UNORDERED MAP - HASH TABLE
unordered_map<int,int> first;
first.empty()
for (auto& elem: first) {
cout << elem.first << ":" << elem.second;}
mymap.size() 
it = mymap.begin(); it != mymap.end()
mymap["Bakery"]="Barbara"; 
mymap.at("Mars") = 3396;
const_iterator got = mymap.find (input)
 if (mymap.count(x)>0)
mymap.bucket_count();


MULTISET
#include <set>
multiset<int> mymultiset

MULTIMAP
#include <map>
multimap<char,int> mymultimap;

